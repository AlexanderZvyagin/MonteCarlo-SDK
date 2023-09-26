++++++++++++++++++++++++++
Computational Grid
++++++++++++++++++++++++++

Lets suppose we have a system of :math:`n` equations
which define our system. We want to generate :math:`m`
(independent) paths for each state. Because we have *processes*
our paths are time-dependent, defined in some time window range
:math:`[t_{start},t_{end}]`. Because we simulate
*Discrete stochastic processes*, the interval :math:`[t_{start},t_{end}]`
is divided into :math:`k` subintervals.

The parameters :math:`n,m,k` are inputs (among others)
for the Monte Carlo engine.

- :math:`n` number of equations
- :math:`m` number of paths
- :math:`k` number of time points

Thus, during a single Monte Carlo simulation the engine
will need to compute :math:`n \cdot m \cdot k` values.

.. note::

    The GPU card *NVIDIA GeForce RTX 2060 Super* is capable
    of computing :math:`n \cdot m \cdot k = 10^{10}` values
    in seconds.
