++++++++++++++++++++++++++
Evaluation Grid
++++++++++++++++++++++++++

We solve a system of SDE in the time window :math:`[t_{start},t_{end}]`.
At the initial time point :math:`t=t_{start}`, the state vector
:math:`\vec{S(t_{start})}` is known (it is the input).
When computations will reach :math:`t=t_{end}`,
the :ref:`solution <Evaluation Results>` :math:`\vec{S(t_{end})}` is available.

For some problems it is suffice to have :math:`\vec{S(t_{end})}` as the
result of a computation.
For some other problems, you may want to observe the intermediate states
:math:`\vec{S(\tau)}`, :math:`t_{start} < \tau < t_{end}`.
It is very unpractical to return the list of :math:`\vec{S(t_i)}`, where
:math:`i={1\cdots k}` is every point of the time grid.

User needs to provide the list of evaluation points explicitly.
