++++++++++++++++++++++++++
Introduction & Readme
++++++++++++++++++++++++++

In a nutshell, we try to provide a framework to numerically solve a system
of stochastical differential equations
(https://en.wikipedia.org/wiki/Stochastic_differential_equation):

.. math::

    \begin{cases}
    dS_1 &=& \mu_1(t,\vec{S}) \cdot \text{d}t + \sigma_1(t,\vec{S}) \cdot \text{d}W_1 \\
    dS_2 &=& \mu_2(t,\vec{S}) \cdot \text{d}t + \sigma_2(t,\vec{S}) \cdot \text{d}W_2 \\
    \cdots \\
    dS_n &=& \mu_n(t,\vec{S}) \cdot \text{d}t + \sigma_n(t,\vec{S}) \cdot \text{d}W_n
    \end{cases}

where :math:`\vec{S}=(S_1,S_2,\cdots,S_n)`.

The aim of the present documentation is to introduce the concepts of building
the system of SDE and the API to solve it.

The software access is provided by a RESTful API
(https://en.wikipedia.org/wiki/Representational_state_transfer).
The software development kit SDK (with examnples) can be found in
the repository https://github.com/WarShoe/mcsdk.
