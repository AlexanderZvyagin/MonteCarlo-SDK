import os, requests
import mcsdk as sdk

server = f'http://{os.getenv("SERVER_ADDRESS","naz.hopto.org")}:{os.getenv("SERVER_PORT","8001")}'

def test_server_available():
    for endpoint in ('/','/functions','/metrics'):
        response = requests.get(f'{server}{endpoint}')
        assert response.status_code==200

def BuildModel_Simple():
    m = sdk.Model()

    m.TimeStart = 0
    m.TimeSteps = 10
    m.NumPaths = 10000
    m.Add(sdk.IndependentGaussian())
    m.Add(sdk.BrownianMotion(0.1,0.2,2)) # start, drift, diffusion

    m.evaluations.append(sdk.EvaluationPoint(2))

    return m

def test_simple_model():
    er = sdk.run( BuildModel_Simple(), server )
    print(er)
    assert len(er.names)==2

def test_functions_endpoint():
    response = requests.get(f'{server}/functions').json()
    for j in response:
        f = sdk.UpdaterDoc()
        sdk.UpdaterDoc_to_json(j,f)

def add_rate_and_discount_processes (
    model          : sdk.Model,
    rate_start     : float     = 0,
    rate_drift     : float     = 0,
    rate_diffusion : float     = 0,
    prefix         : str         = ''
):
    print(f'The rate process follows a BrownianMotion process starting at {rate_start} with drift={rate_drift} and diffusion={rate_diffusion} parameters.')
    rate_uf = model.Add(sdk.BrownianMotion(start=rate_start,drift=rate_drift,diffusion=rate_diffusion,title=f'{prefix}rate'))
    df_uf = model.Add(sdk.ZeroCouponBond(underlying=rate_uf.GetStateNumber(),start=1,title=f'{prefix}discount factor'))
    return {
        'rate':rate_uf,
        'df':df_uf
    }

def add_fixed_leg (
    model       : sdk.Model,
    t0          : float,
    dt          : float,
    n           : int,
    fixed_rate  : float,
    discount    : sdk.Updater,
    notional    : float       = 1,
    prefix      : str         = ''
):
    '''Add fixed leg with constant notional and rate
    
    Args:
        t0       (float): start of the leg with respect to the model start time
        dt       (float): time interval between fixed leg time points, dt>0
        n          (int): number of periods, n>0
        rate     (float): fixed rate
        notional (float): notional
    '''
    
    fixed_rate_uf = model.Add(sdk.Polynom(ref=-1,args=[fixed_rate],title=f'{prefix}fixed rate'))
    notional_uf = model.Add(sdk.Polynom(ref=-1,args=[notional],title=f'{prefix}notional'))
    tau_uf = model.Add(sdk.Polynom(ref=-1,args=[dt],title=f'{prefix}tau'))
    mul_uf = model.Add(sdk.Multiplication(refs=[uf.GetStateNumber() for uf in (fixed_rate_uf,notional_uf,tau_uf,discount)],title=f'{prefix}product'))

    t = [model.TimeStart+t0+i*dt for i in range(n+1)]
    print(f'{prefix} payment points:',t[1:])
    undiscounted_leg_uf = model.Add(sdk.SumOfFutureValues(
        state=mul_uf.GetStateNumber(),
        t=t[1:],
        title=f'{prefix}Value (not discounted)'
    ))
    
    leg_uf = model.Add(sdk.Division(
        numerator=undiscounted_leg_uf.GetStateNumber(),
        denominator=discount.GetStateNumber(),
        title=f'{prefix}Value'
    ))
    
    return {
        'time_points': t,
        'fixed_leg_undiscounted':undiscounted_leg_uf,
        'fixed_leg_discounted':leg_uf
    }

def test_multi_simulations ():

    t0 = 0

    model = sdk.Model()
    model.TimeStart = t0
    model.TimeSteps = 10
    model.NumPaths = 100
    model.Add(sdk.IndependentGaussian())

    add1 = add_rate_and_discount_processes(model=model,rate_start=0,rate_drift=0.02,rate_diffusion=0.5)
    add2 = add_fixed_leg(model=model,t0=0,dt=0.5,n=3,fixed_rate=0.01,discount=add1['df'],notional=1,prefix='[fixed leg] ')
    model.evaluations.append(
        sdk.EvaluationPoint(model.TimeStart)
            .Add(sdk.Histogram(
                ax = sdk.HistogramAxis(
                    add2['fixed_leg_discounted'].GetStateNumber(),
                    200
                ),
            ))                
    )
    model.evaluations.append(sdk.EvaluationPoint(add2['time_points'][-1]))

    results = sdk.run (model, server)
    print(results.df())

    point = 0

    print("TO TEST:",results.GetStateEvaluationResult(add2['fixed_leg_undiscounted'].GetStateNumber(),point).GetStdDev(),results.GetStateEvaluationResult(add2['fixed_leg_discounted'].GetStateNumber(),point).GetStdDev())

    assert results.GetStateEvaluationResult(add2['fixed_leg_undiscounted'].GetStateNumber(),point).GetStdDev()>1e-4
    assert results.GetStateEvaluationResult(add2['fixed_leg_discounted'].GetStateNumber(),point).GetStdDev()>1e-4
