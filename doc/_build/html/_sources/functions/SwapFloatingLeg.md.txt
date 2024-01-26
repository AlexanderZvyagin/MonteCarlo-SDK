
# SwapFloatingLeg

The reset (or fixing) time points are i=0,1,..n-1.
At this moment the reference process value N[i] is checked, but the cash flow
is only generated at time point i+1.

## Input parameters

To compute the leg value we need to know:
- notional values at points i=1...n, n values in total
- P_df(T_start,T[i]) discount factors at points i=1...n, n values in total
- P_L(T_start,T[i]) factors at points i=0...n, n+1 values in total

L(T_start,T[i],T[i+1]) = (P'(T_start,T[i])/P'(T_start,T[i+1])-1) / (T[i+1]-T[i])

|   | name | range | description |
|---|------|---|---|
| args[0] | T[0] | | |
| args[1] | T[1] | | |
| args[2] | ...  | | |
| refs[0] | P_df(T_start,T[i])*N[i] | notional*df | |
| refs[1] | P_L(T_start,T[i]) | For L() computation |

