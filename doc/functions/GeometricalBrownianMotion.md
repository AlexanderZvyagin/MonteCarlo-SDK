
# GeometricalBrownianMotion

$$dS = S(\mu dt + \sigma dW_t)$$

The function requires _mean_ and _sigma_ parameters and a gaussian random variable to advance its state.
The parameters _mean_ and _sigma_ can be passed either as constant values in _args_ or
they can be themself some processes and in this case the reference process must be provided in _refs_.
A random number can be genegerated internally, or provided externally with _refs_.

## Input parameters

### nrefs=0 and nargs=2

Constant _mean_ and _sigma_, internally generated random variable.

|   | name | range | description |
|---|------|---|---|
| args[0] | mean | any | |
| args[1] | sigma | any | |

### nrefs=1 and nargs=2

Constant _mean_ and _sigma_, externally taken random variable.

|   | name | range | description |
|---|------|---|---|
| refs[0] | W | any | normally distributed variable |
| args[0] | mean | any | |
| args[1] | sigma | any | |

### nrefs=2 and nargs=0

Parameters _mean_ and _sigma_ are given as a reference processes,
the random variable is generated internally.

|   | name | range | description |
|---|------|---|---|
| refs[0] | mean | any | |
| refs[1] | sigma | any | |

### nrefs=3 and nargs=0

Parameters _mean_, _sigma_ and the random variable are given as a reference processes,

|   | name | range | description |
|---|------|---|---|
| refs[0] | mean | any | |
| refs[1] | sigma | any | |
| refs[2] | W | any | |

