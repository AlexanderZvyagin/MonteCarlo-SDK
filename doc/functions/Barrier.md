
# Barrier

A barrier state starts from some initial value S0.
On each computation step we verify the barrier crossing condition, and if it is satisfied, the barrier state will
be set to STATE=valueOnCrossing.

For direction 'up':

    if(Sold<level and Snew>=level)
        barrierState = valueOnCrossing;

For direction 'down':

    if(Sold>level and Snew<=level)
        barrierState = valueOnCrossing;

## References

The barrier function expectes exactly one reference: an **underlying**.

### [ref 0]

The underlying process.

## Arguments

### [arg 0] level
Barrier level

### [arg 1] valueOnCrossing
The value we set when the barrier is crossed.

### [arg 2] direction

This is the barrier crossing condition.

| value | direction  |
| ------------- |-------------:|
| -1 | down          |
|  0 | any (up or down) |
| +1 | up |
    .has_start  = false,
    .nargs_min  = 4,
    .nrefs_min  = 1,
r of time windows

The number of time windows (say **m**) when the barrier will be checked.
The next **m * 2** parameters will be treated as [from,to) pairs, time windows
where the barrier condition will be checked. If **m==0**, the barrier condition
will be checked on all time step.

## Examples

### S0=0, args=[1000,1,-1,0,0]

The barrier inital state is 0. We check on any time step (because arg[4]==0)
the the barrier level==1000 will be crossed in the down direction (for example,
from 1000.5 to 1000). If the condition is NOT fulfilled, we don't change the
barrier state. Otherwise, we set the barrier value (arg[3]==0 means 'set')
to value 1 (because arg[1]==1). Obvioulsy, only the first crossing over
the barrier will have an effect, when we change the barrier state from 0
(because S0==0) to 1 (because arg[1]==1 and arg[3]==0)

### S0=0, args=[1000,1,-1,0,2,111.1,222.2,333.3,444.4]

The same as above, but wee only check the barrier condition if the time
is in one of the two (because arg[5]==2) windows:

- [111.1,222.2)
- [333.3,444.4)

### S0=0, args=[1000,1,-1,1,2,111.1,222.2,333.3,444.4]

The same as above, we 'count' (arg[3]==1 is the increment)
how many times the barrier is crossed in the 'down' direction.
