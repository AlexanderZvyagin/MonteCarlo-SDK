
# SwapFixedLeg

The function computes the sum (T[i]-T[i-1])*N[i],
for i=1..n

## Input parameters

|   | name | range | description |
|---|------|---|---|
| args[0] | T[0] | | |
| args[1] | T[1] | | |
| args[2] | ...  | | |
| refs[0] | notional*df | | |

- time points Ti=[T0,...Tn]   n>=1, the minimal length of Ti vector is two: [T0,T1]
- notional process

