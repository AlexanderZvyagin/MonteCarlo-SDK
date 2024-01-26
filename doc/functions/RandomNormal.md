
# RandomNormal

The function can do one of the following:
- generate a single normally distributed random variable
- generate two correlated normally distributed random variables

## Initial state

Not applicable, the function has no initial state.

## Arguments & References

| nrefs | nargs | #states | description |
|-------|-------|---------|-------------|
| 0     | 0     | 1       | Generate a single variable. |
| 0     | 1     | 2       | Generate two correlated (correlation coefficient is args[0]) random variables. |
| 1     | 1     | 1       | Takes a random variable from refs[0] and generate a correlated (correlation coefficient is args[0]) random variable. |

