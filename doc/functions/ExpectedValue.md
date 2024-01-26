
# ExpectedValue

The function will compute $\mathbb{E} S(T)$.

## Input arguments

- refs[0] is the reference process
- args[0] extraction point number (non-negative integer)

### Example

Let's suppose that a model starts simulation at t=0, and we want to evaluate the
model state values at time points t=[10,20,50].
Thus, the model has three extraction points. If we want to use ExpectedValue at
t=20 for a state S=9, we will need
to pass into ExpectedValue function:

- refs[0]=9
- args[0]=1

