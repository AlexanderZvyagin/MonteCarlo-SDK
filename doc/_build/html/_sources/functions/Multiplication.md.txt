
# Multiplication

The function computes A*S1*S2*..., where A is a constant and S1,S2,... are process states.

## Initial state parameter

The initial state is ignored, the function state is computed on each time step.

## Arguments

The function has one arguments.

|   | name |
|---|------|
| 0 | multiplication factor |

## References

Non-zero number of references: nrefs>0. All states will be multipplied.

## Example:

- start = ignored
- args = [0.5]
- refs = [0,7,9]

Computes 0.5*state[0]*state[7]*state[9]

