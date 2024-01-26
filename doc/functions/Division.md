
# Division

Compute division of two processes.

If abs(denominator)<=eps, than the division result will be not-a-number.

## Initial state

Not used, the function will override previously computed values.

## Arguments

The function has exactly one arguments. It is a non-negative number eps. 
If denominator state absolute value is less than eps, the division result will be set to NaN.
This can be used to avoid producing +/- infinity values for the division result.
A value 0 can be used (which essentially will allow division by zero).

|   | name | description | range |
|---|------|-------------|-------|
| 0 | eps  | abs(denominator) min value | non-negative |

## References

|   | name |
|---|------|
| 0 | Numerator |
| 1 | Denominator |

## Example:

- start = Ignore
- args = [0.01]
- refs = [2,5]

Take a state[5] value, if abs(state[5])>=0.01 set the division result to state[2]/state[5].
Otherwise, the resukts is NAN.

