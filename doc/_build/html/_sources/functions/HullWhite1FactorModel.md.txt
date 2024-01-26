
# HullWhite1FactorModel

One Factor Hull-White Model.

$dr(t) = [theta(t)-alpha(t)*r(t)]*dt + sigma(t)*dW(t)$

The updater accepts either:
- 3 arguments and 0 references (for constant alpha,theta,sigma parameters)
OR
- 0 arguments and 3 references (any t-adapted processes of alpha,theta,sigma)

## Input parameters


### Constant parameters, the random variable is internally generated.

|   | name | range | description |
|---|------|---|---|
| nrefs |  | 0 | |
| nargs |  | 3 | |
| args[0] | alpha | any | |
| args[1] | theta | any | |
| args[2] | sigma | any | |

### Constant parameters, with externally given random variable.

|   | name | range | description |
|---|------|---|---|
| nrefs |  | 1 | |
| refs[0] | W     | any | |
| nargs |  | 3 | |
| args[0] | alpha | any | |
| args[1] | theta | any | |
| args[2] | sigma | any | |

### Parameters are given as processes, the random variable is internally generated.

|   | name | range | description |
|---|------|---|---|
| nrefs |  | 3 | |
| refs[0] | alpha(t) | any | |
| refs[1] | theta(t) | any | |
| refs[2] | sigma(t) | any | |
| nargs |  | 0 | |

### Parameters are given as processes, the random variable is externally generated.

|   | name | range | description |
|---|------|---|---|
| nrefs |  | 4 | |
| refs[0] | alpha(t) | any | |
| refs[1] | theta(t) | any | |
| refs[2] | sigma(t) | any | |
| refs[3] | W        | any | |
| nargs |  | 0 | |

        