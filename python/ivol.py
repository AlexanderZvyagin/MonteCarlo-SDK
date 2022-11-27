from math import sqrt, log, nan
from scipy.special import ndtr as N
from scipy import optimize

def bs76_call_put (spot,strike,volatility,expiry,df=1):
    '''returns (call,put)'''
    sqt = volatility*sqrt(expiry)
    forward = spot/df
    d1 = log(forward/strike)/sqt + sqt/2
    d2 = d1 - sqt
    call = N( d1)*spot      - N( d2)*strike*df
    put =  N(-d2)*strike*df - N(-d1)*spot
    return (call,put)

def bs76_ivol (spot,strike,expiry,price,call_put,df=1,vol_guess=0.1,method='broyden1'):
    
    def f(volatility):
        call,put = bs76_call_put (spot,strike,volatility,expiry,df)
        if call_put=='call':
            return price-call
        if call_put=='put':
            return price-put
        raise Exception(f'Bad call_put={call_put}')

    if method=='hybr':
        sol = optimize.root(f,vol_guess,method='hybr')
        return sol.x[0] if sol.success else nan
    elif method=='broyden1':
        sol = optimize.root(f,vol_guess,method='broyden1')
        return float(sol.x) if sol.success else nan
    # elif method=='broyden1':
    #     sol = newton_solver(f,vol_guess,xmin=1e-5,xmax=2,xstep=1e-2,xstep_min=1e-10,tol=1e-3,calls_max=200)
    #     return float(sol.x) if sol.success else nan
    else:
        raise Exception(f'Bad method name: {method}')
    
# def bs76_ivol_newton (spot,strike,expiry,price,call_put,df=1,vol_guess=0.1):
#     def f(volatility):
#         call,put = bs76(spot,strike,volatility,expiry,df)
#         if call_put=='call':
#             return price-call
#         if call_put=='put':
#             return price-put
#         raise Exception(f'Bad call_put={call_put}')
#     sol = newton_solver(f,vol_guess,xmin=1e-5,xmax=2,xstep=1e-2,xstep_min=1e-10,tol=1e-3,calls_max=200)
#     if not sol['success']:
#         print(sol['status'])
#     else:
#         print(sol)
#     # print(f'sol: S={spot} K={strike} T={expiry} P={price} cp={call_put} df={df} => {sol.success} {sol.x[0]}')
#     return sol['x'] if sol['success'] else nan
    
# def bs76_ivol_scipy_broyden1 (spot,strike,expiry,price,call_put,df=1,vol_guess=0.1):
#     def f(volatility):
#         call,put = bs76_call_put (spot,strike,volatility,expiry,df)
#         if call_put=='call':
#             return price-call
#         if call_put=='put':
#             return price-put
#         raise Exception(f'Bad call_put={call_put}')
#     sol = optimize.root(f,vol_guess,method='broyden1')
#     # print(f'sol: S={spot} K={strike} T={expiry} P={price} cp={call_put} df={df} => {sol.success} {sol.x[0]}')
#     return float(sol.x) if sol.success else nan

# def bs76_ivol_scipy_hybr (spot,strike,expiry,price,call_put,df=1,vol_guess=0.1):
#     def f(volatility):
#         call,put = bs76(spot,strike,volatility,expiry,df)
#         if call_put=='call':
#             return price-call
#         if call_put=='put':
#             return price-put
#         raise Exception(f'Bad call_put={call_put}')
#     sol = optimize.root(f,vol_guess,method='hybr')
#     # print(f'sol: S={spot} K={strike} T={expiry} P={price} cp={call_put} df={df} => {sol.success} {sol.x[0]}')
#     return sol.x[0] if sol.success else nan

