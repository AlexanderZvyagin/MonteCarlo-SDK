import math

def linspace(min:float,max:float,n:int):
    assert n>=2 and min!=max
    step = (max-min)/n
    return [min] + [min+step*i for i in range(1,n-2)] + [max]

def newton_solver(f,x0,xstep=1,xmin=None,xmax=None,tol=1e-5,calls_max=100,xstep_min=1e-5):
    '''Solve an equation f(x)=0
    
    >>> newton_solver(lambda x:x+10,1,calls_max=20,tol=1e-12)

    eps=1e-12
    >>> newton_solver(lambda x:612-x**2,10,calls_max=20,tol=eps,xstep_min=eps)

    >>> newton_solver(lambda x:math.cos(x)-x**3,1,calls_max=20,tol=eps,xstep_min=eps)

    >>> newton_solver(lambda x:math.cos(x)-x**3,1,calls_max=5,tol=eps,xstep_min=1e-12)

    >>> newton_solver(lambda x:math.cos(x)-x**3,1,calls_max=20,tol=eps,xstep_min=1e-6)
    '''

    dx     = xstep
    x_prev = x0
    x_next = x_prev
    f_prev = f(x_prev)
    f_next = f_prev
    calls  = 1
    status = None
    
    def converged():
        return abs(f_next)<tol
    
    def stop_condition():
        if calls>=calls_max:
            return f'calls_max={calls_max} is reached'
        if abs(x_next-x_prev)<xstep_min:
            return f'no progress: the step size is smaller then xstep_min={xstep_min}'
        return None
    
    while True:
        x_prev = x_next
        f_prev = f_next
        x_next = x_prev + dx
        if xmin is not None and x_next<xmin:
            x_next = xmin
        if xmax is not None and x_next>xmax:
            x_next = xmax

        if converged():
            break
            
        status = stop_condition()
        if status is not None:
            break
        
        calls += 1
        f_next = f(x_next)
        f_deriv = (f_next-f_prev)/dx
        if f_deriv==0:
            status = 'Cannot make any progress, the function derivative is zero'
            break
        dx = - f_next/f_deriv
    
    return {
        'success' : converged(),
        'calls'   : calls,
        'f'       : f_next,
        'x'       : x_next,
        'xe'      : dx,
        'status'  : 'success' if status is None else status
    }

def test_newton_solver():
    '''
    '''
    
    r = newton_solver(lambda x:x+10,1,calls_max=20,tol=1e-12)
    assert r['success'] and r['calls']<=10

    eps=1e-12
    r = newton_solver(lambda x:612-x**2,10,calls_max=20,tol=eps,xstep_min=eps)
    assert r['success'] and r['calls']<=10

    r = newton_solver(lambda x:math.cos(x)-x**3,1,calls_max=20,tol=eps,xstep_min=eps)
    assert r['success'] and r['calls']<=10

    r = newton_solver(lambda x:math.cos(x)-x**3,1,calls_max=5,tol=eps,xstep_min=1e-12)
    assert (not r['success']) and r['calls']<=10

    r = newton_solver(lambda x:math.cos(x)-x**3,1,calls_max=20,tol=eps,xstep_min=1e-6)
    assert (not r['success']) and r['calls']<=10
