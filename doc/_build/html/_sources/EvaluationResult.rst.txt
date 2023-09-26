.. _Evaluation Results:

++++++++++++++++++++++++++
Evaluation Results
++++++++++++++++++++++++++

Evaluation results are represented as a two-dimensional table (matrix).
The rows of the matrix are stateful functions
and the columns are evaluation points.

Every *cell* of the matrix is an object with four *float-type* values:

- :math:`l` number of paths used in the computation
- :math:`\mu` mean value
- :math:`\sigma` standard deviation
- :math:`k` skewness

https://en.wikipedia.org/wiki/Skewness

Normally :math:`l` should be equal to :math:`m` (number of paths). But it can
be smaller, as the MonteCarloEngine will automatically exclude in the statistics
computation values which were evaluated to
`NAN <https://en.wikipedia.org/wiki/NaN>`_ values.
