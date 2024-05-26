
# Choice

The function accepts no arguments and a list of references of length n+1, n>=0.

A state value ferom the first reference (which is a mandatory) is converted into an int value *m*.

If the resulted integer *m* is between 1 and *n*, 
then the function value will be set to a state of the referenced function.
Otherwise (the converted argument is not a valid index in the refs),
the Choice function state is set to not-a-number (NAN).

## Initial state

The function has no initial state.

## Arguments

The function does not have any arguments.

## References



|     | name   | description      |
|-----|--------|------------------|
| 0   | Sindex | index            |
| 1   | S0     | state of index=0 |
| 2   | S1     | state of index=1 |
| ... | ...    | ...              |
| n   | ...    | ...              |


## Example

Consider a state I which is an indicator function, taking values only 0 and 1.
In this case, Choice(I,S0,S1) will return a state value of
S0 if round(I)==0 and S1 if round(I)==1.
If round(I) is not 0 or 1, the Choice state will be set to NAN.

