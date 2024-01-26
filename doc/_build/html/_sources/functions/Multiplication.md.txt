
# Multiplication

The function computes

$$
A \cdot \prod_{i=1}^n S_i
$$
where A is a constant args[0] and $S_1,S_2,\dots,S_n$ are process states refs[0], ..., refs[n-1].

## Initial state

Not applicable, the function state is computed on each time step.

## Arguments

The function has one arguments.

|   | name |
|---|------|
| args[0] | A, multiplication factor |

## References

Non-zero number of references: nrefs>0.

## Example:

- args = [0.5]
- refs = [0,7,9]

The function will compute: 0.5*state[0]*state[7]*state[9]

