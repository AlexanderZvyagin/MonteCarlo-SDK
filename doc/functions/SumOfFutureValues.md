
# SumOfFutureValues

args: an array of (monotnoically increasing) m time points T[i]:  T[0]<T[1]<...<T[m-1]
refs: a reference process N.

At every extraction point, the state value is computed as

SumOfFutureValues = sum(i = [j..N]) N[i]

where j is the first time point which is not less than t: T[j]>=t (and j==0 or T[j-1]<t)

Between every two extraction points Ta,Tb the SumOfFutureValues value is constant.

