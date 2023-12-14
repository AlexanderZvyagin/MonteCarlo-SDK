
# Polynom

The polynom order is taken from the number of passed arguments.
Minimum number is 1, which will be treated as constant function.
Otherwise it will compute a0+a1*x+a2*x*x+..., where 'x'-is the
polynom argumnt (see below) and a0,a1... are arguments of the
function.

The polynopm argument 'x' is passed as 'Xref'. If Xref=-1, then the argument is time.
Otherwise, it is a state number to which will be used as an 'x'-argument.
