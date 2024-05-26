
# Polynom

The function will compute a polynom of an order N.

The number N is equal to the number of arguments passed to the Polynom updater.
The minimal number is 1, and in this case a constant function is defined.
Otherwise it will compute a0+a1*x+a2*x*x+..., where 'x'-is the
polynom argument (see below) and a0,a1... are arguments of the
function.

The polynom argument 'x' is passed as a 'reference', thus the Polynom function expects
strictly one reference and 1...N arguments. If Xref=-1, then the argument is a current MC time.
Otherwise, it is a state number which is used as an 'x'-argument.

Examples: 
| Polynom | refs | args | Comment |
| ----- | ---- | ---- | ---- |
| P(t) = 44 | [-1] | [44] | A constant function |
| P(t) = 1+2*t^4 | [-1] | [1,0,0,0,2] | use ref=-1 for the time argument |
| P(x) = -x^2 | [123] | [0,0,-1] | assuming that state 123 holds the 'x' argument |


