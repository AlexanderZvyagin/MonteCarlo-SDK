
# Linear1DInterpolation

Perform one demensional interpolation between [Xmin,Xmax].
The number of interpolation points
is deduced from the number of arguments passed to the function.
The first two arguments are Xmin,Xmax. The rest arguments are Y-values on the
regular grid between [Xmin,Xmax]. Thus, the total nummber of arguments
must be at least 4. And the total number of interpolation points is narg-2.

## Example: args=[1,2,3,4,5]
there are three interpolation points (5-2=3):

- Xmin = 1.0
- Xmax = 2.0
- Y(X=1.0) = 3
- Y(X=1.5) = 4
- Y(X=2.0) = 5

The interpolation function argument is passed as 'Xref'. If Xref=-1, then the argument is time.
Otherwise, it is a state number to will be used as an 'x'-argument.

Linear1DInterpolation returns Y(Xmin) if X<Xmin and Y(Xmax) if X>Xmax.

Linear1DInterpolation does not use the old state value.
Thus, the starting process state value is ignored.

