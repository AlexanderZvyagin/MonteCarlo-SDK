++++++++++++++++++++++++++
Functions
++++++++++++++++++++++++++

Stateless functions
+++++++++++++++++++++

Generation of (pseudo)random numbers does not require
a knowledge of a previous random generator state explicitly.
It is enough to have some function which will
just produce a new random number on each
call, like :code:'r()'. And the function will handle
its state internally.
Usually, you need to provide at least one function of this kind,
to generate the random numbers. Such functions
do not have any initial states
(initial seed number is handled in a special way).
They still can have parameters,
for example you need to pass somehow a correlation
parameter :math:`\rho` to generate two correlated
Brownian motion processes. Still, the a random number
does not have a *state*, its next value should be independent
from the current.

Stateful functions
+++++++++++++++++++++

Other functions (e.g. simple Brownian motion process)
do have states. They (usually) require some initial
state value, given at initial time :math:`t_{start}`.

.. note::

    To generate a simple Brownian motion process
    :math:`dS_t = \mu \cdot \text{d}t + \sigma \cdot \text{d}W_t`
    we need to use two functions:

    - one *stateless* function to generate a normally distributed random variable :math:`W_t`
    - one *stateful* function for the process :math:`S_t`, which depends on :math:`S(t=t_{start},\mu,\sigma)`

.. toctree::
    :glob:

    functions/*