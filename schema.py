#!/usr/bin/env python3

from cgdto import *
from math import nan

def schema ():

    objs = [] # objects in the file

    obj = Struct('UpdaterDoc')
    obj.attributes.append(Variable('name','string'))
    obj.attributes.append(Variable('title','string'))
    obj.attributes.append(Variable('doc_md','string'))
    obj.attributes.append(Variable('start','string'))
    obj.attributes.append(Variable('nargs_min','int'))
    obj.attributes.append(Variable('nrefs_min','int'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',''),
            Variable('title','string',''),
            Variable('doc_md','string',''),
            Variable('start','string',''),
            Variable('nargs_min','int',-88),
            Variable('nrefs_min','int',-88)
        ],
        mapping = [
            ('name',[Variable('name')]),
            ('title',[Variable('title')]),
            ('doc_md',[Variable('doc_md')]),
            ('start',[Variable('start')]),
            ('nargs_min',[Variable('nargs_min')]),
            ('nrefs_min',[Variable('nrefs_min')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('UpdaterDto')
    obj.attributes.append(Variable('name','string'))
    obj.attributes.append(Variable('refs','int', list=True, optional=True))
    obj.attributes.append(Variable('args','float', list=True, optional=True))
    obj.attributes.append(Variable('start','float',optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name', 'string', ''),
            Variable(name='refs', type='int', defval=None, list=True, optional=True),
            Variable('args', 'float', defval=None, list=True, optional=True),
            Variable('start', 'float', defval=None, optional=True)
        ],
        mapping = [
            ('name',[Variable('name')]),
            ('refs',[Variable('refs')]),
            ('args',[Variable('args')]),
            ('start',[Variable('start')]),
        ]
    ))
    objs.append(obj)
    UpdaterDto = obj

    obj = Struct('Updater',UpdaterDto)
    obj.attributes.append(Variable('_equation','int',skip_dto=True))
    obj.attributes.append(Variable('_state','int',skip_dto=True))
    obj.attributes.append(Variable('title','string',skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',''),
            Variable('refs','int',[],list=True),
            Variable('args','float',[],list=True),
            Variable('start','float',None,optional=True),
            Variable('title','string',''),
        ],
        mapping = [
            (obj.base.name,[
                Variable('name'),
                Variable('refs'),
                Variable('args'),
                Variable('start'),
            ]),
            ('_equation',[-88]),
            ('_state',[-88]),
            ('title',[Variable('title')]),
        ]
    ))
    obj.methods.append(Function (
        'GetStateNumber',
        'int',
        code = {
            'typescript':
'''
if(this._state<0)
    throw new Error(`Updater ${this.name} has no state.`);
return this._state;
''',
            'cpp':
'''
if(_state<0)
    throw std::runtime_error("An updater has no state.");
return _state;
''',
            'python':
'''
if self._state<0:
    raise Exception(f'Updater {self.name} has no state.')
return self._state
'''
        }
    ))

    obj.methods.append(Function (
        'GetEquationNumber',
        'int',
        code = {
            'typescript':
'''
if(this._equation<0)
    throw new Error(`Updater ${this.name} has no _equation.`);
return this._equation;
''',
            'cpp':
'''
if(_equation<0)
    throw std::runtime_error("An updater has no _equation.");
return _equation;
''',
            'python':
'''
if self._equation<0:
    raise Exception(f'Updater {self.name} has no _equation.')
return self._equation
'''
        }
    ))

    obj.methods.append(Function (
        'HasState',
        'boolean',
        const = True,
        code = {
            'python':
'''
return self.start is not None
''',
            'cpp':
'''
return start.has_value();
''',
            'typescript':
'''
return this.start !== undefined;
'''
        }
    ))

    obj.methods.append(Function (
        'GetStart',
        'float',
        const = True,
        code = {
            'python':
'''
if self.start is None:
    raise ValueError()
return self.start
''',
            'cpp':
'''
if( not start.has_value() )
    throw std::invalid_argument("start");
return start.value();
''',
            'typescript':
'''
if( this.start === undefined )
    throw new Error("start");
return this.start;
'''
        }
    ))

    objs.append(obj)
    Updater = obj

    objs.append(CodeBlock(code={
        'cpp': {'''
void from_json(const json &j, std::vector<Updater> &u) {
    for(auto v: j)
        u.push_back(v);
}
'''
        }
    }))

    obj = Struct('IndependentGaussian',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('refs','int'  ,defval=[], list=True),
            Variable('title','string',''),
        ],
        mapping = [(obj.base.name,[
            'IndependentGaussian',
            Variable('refs'),
            [],
            None,
            Variable('title'),
        ])]
    ))
    objs.append(obj)
    
    obj = Struct('CorrelatedGaussian',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('correlation','float'  ,nan),
            Variable('state1','int'  ,-88),
            Variable('state2','int'  ,-88),
            Variable('title','string',''),
        ],
        mapping = [(obj.base.name,[
            'CorrelatedGaussian',
            [Variable('state1'),Variable('state2')],
            [Variable('correlation')],
            None,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('BrownianMotion',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,'float', nan),
            Variable('drift'     ,'float', nan),
            Variable('diffusion' ,'float', nan),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'BrownianMotion',
            [], # refs
            [Variable('drift'),Variable('diffusion')], # args
            Variable('start'),
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('BrownianMotionRef',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,'float', nan),
            Variable('drift'     ,'int'  , -88),
            Variable('diffusion' ,'int'  , -88),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'BrownianMotion',
            [Variable('drift'),Variable('diffusion')], # refs
            [], # args
            Variable('start'),
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('GeometricalBrownianMotion',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,'float', nan),
            Variable('drift'     ,'float', nan),
            Variable('diffusion' ,'float', nan),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'GeometricalBrownianMotion',
            [], # refs
            [Variable('drift'),Variable('diffusion')], # args
            Variable('start'),
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('GeometricalBrownianMotionRef',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,'float', nan),
            Variable('drift'     ,'int'  , -88),
            Variable('diffusion' ,'int'  , -88),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'GeometricalBrownianMotion',
            [Variable('drift'),Variable('diffusion')], # refs
            [], # args
            Variable('start'),
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('ZeroCouponBond',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying','int'  , -88),
            Variable('start'     ,'float', nan),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'ZeroCouponBond',
            [Variable('underlying')], # refs
            [], # args
            Variable('start'),
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('Option',Updater)
    obj.attributes.append(Variable('Call','int',defval=0, static=True, skip_dto=True))
    obj.attributes.append(Variable('Put' ,'int',defval=1, static=True, skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying','int'  , -88),
            Variable('strike'    ,'float', nan),
            Variable('call_put'  ,'int',   -88),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'Option',
            [Variable('underlying')], # refs
            [Variable('strike'),Variable('call_put')], # args
            0, # start
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('Barrier',Updater)
    obj.attributes.append(Variable('DirectionUp','int',defval=1, static=True, skip_dto=True))
    obj.attributes.append(Variable('DirectionDown','int',defval=-1, static=True, skip_dto=True))
    obj.attributes.append(Variable('DirectionAny','int',defval=0, static=True, skip_dto=True))
    obj.attributes.append(Variable('ActionSet','int',defval=0, static=True, skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying','int'  ,-88),
            Variable('start'     ,'float',nan),
            Variable('level'     ,'float',nan),
            Variable('direction' ,'int'  ,-88),
            Variable('action'    ,'int'  ,-88),
            Variable('value'     ,'float',nan),
            Variable('title'     ,'string',''),
        ],
        mapping = [(obj.base.name,[
            'Barrier',
            [
                Variable('underlying')
            ],
            [
                Variable('level'),
                Variable('value'),
                Variable('direction'),
                Variable('action')
            ],
            Variable('start'),
            Variable('title'),
        ])]
    ))
    
    objs.append(obj)

    obj = Struct('Linear1DInterpolation',Updater,gen_test=False)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('ref'    ,'int'   ,defval=-88),
            Variable('xmin'   ,'float' ,defval=-1),
            Variable('xmax'   ,'float' ,defval=1),
            Variable('y'      ,'float' ,defval=[],list=True),
            Variable('title'  ,'string',defval=''),
        ],
        mapping = [(obj.base.name,[
            'Linear1DInterpolation',
            [Variable('ref')],
            [],
            0, # start
            Variable('title'),
        ])],
        code = {
            'cpp' : '''
if(y.size()<2)
    throw std::invalid_argument("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)");
args.value() = std::vector<float>();
args.value().reserve(2+y.size());
args.value().push_back(xmin);
args.value().push_back(xmax);
for(auto item: y)
    args.value().push_back(item);
''',
            'python' : '''
if len(y)<2:
    raise ValueError("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)")
self.args = [xmin,xmax] + y
''',
            'typescript' : '''
if(y.length<2)
    throw new Error("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)");
this.args = [...[xmin,xmax],...y];
''',
        }
    ))
    objs.append(obj)


    obj = Struct('Multiplication',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('refs'     ,'int',defval=[],list=True),
            Variable('factor'   ,'float',defval=1),
            Variable('title'     ,'string',defval=''),
        ],
        mapping = [(obj.base.name,[
            'Multiplication',
            Variable('refs'),
            [Variable('factor')],
            0, # start
            Variable('title'),
        ])]
    ))
    objs.append(obj)


    obj = Struct('HistogramAxis')
    HistogramAxis = obj
    obj.attributes.append(Variable('state','int'))
    obj.attributes.append(Variable('nbins','int'))
    obj.attributes.append(Variable('min','float'))
    obj.attributes.append(Variable('max','float'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('_state','int',-88),
            Variable('_nbins','int',-88),
            Variable('_min'  ,'float',-88), # FIXME: cannot use math.nan for the moment
            Variable('_max'  ,'float',-88), # FIXME: cannot use math.nan for the moment
        ],
        mapping = [
            ('state',[Variable('_state')]),
            ('nbins',[Variable('_nbins')]),
            ('min',[Variable('_min')]),
            ('max',[Variable('_max')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('Histogram')
    Histogram = obj
    obj.attributes.append(Variable('x',HistogramAxis))
    obj.attributes.append(Variable('y',HistogramAxis,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('x',HistogramAxis,Variable('HistogramAxis()',HistogramAxis)),
            Variable('y',HistogramAxis,None,optional=True),
        ],
        mapping = [
            ('x',[Variable('x')]),
            ('y',[Variable('y')])
        ]
    ))
    objs.append(obj)

    objs.append(CodeBlock(code={
        'cpp': {'''
void from_json(const json &j, std::vector<Histogram> &u) {
    for(auto v: j)
        u.push_back(v);
}
'''
        }
    }))

    obj = Struct ('EvaluationPoint')
    EvaluationPoint = obj
    obj.attributes.append(Variable('state','int'))
    obj.attributes.append(Variable('time','float'))
    obj.attributes.append(Variable('value','float',optional=True))
    obj.attributes.append(Variable('error','float',optional=True))
    obj.attributes.append(Variable('histograms',Histogram,list=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('state','int',-88),
            Variable('time','float',nan),
            Variable('value','float',None,optional=True),
            Variable('error','float',None,optional=True),
            Variable('histograms',Histogram,[],list=True),
        ],
        mapping = [
            ('state',[Variable('state')]),
            ('time',[Variable('time')]),
            ('value',[Variable('value')]),
            ('error',[Variable('error')]),
            ('histograms',[Variable('histograms')]),
        ]
    ))
    obj.methods.append(Function (
        'GetState',
        'int',
        const = True,
        code = {
            'python':
'''
return self.state
''',
            'cpp':
'''
return state;
''',
            'typescript':
'''
return this.state;
''',
        }
    ))
    obj.methods.append(Function (
        'GetTime',
        'int',
        const = True,
        code = {
            'python':
'''
return self.time
''',
            'cpp':
'''
return time;
''',
            'typescript':
'''
return this.time;
''',
        }
    ))
    obj.methods.append(Function (
        'GetValue',
        'float',
        const = True,
        code = {
            'python':
'''
if self.value is None:
    raise ValueError()
return self.value
''',
            'cpp':
'''
if( not value.has_value() )
    throw std::invalid_argument("value");
return value.value();
''',
            'typescript':
'''
if( this.value === undefined )
    throw new Error("value");
return this.value;
''',
        }
    ))
    obj.methods.append(Function (
        'GetError',
        'float',
        const = True,
        code = {
            'python':
'''
if self.error is None:
    raise ValueError()
return self.error
''',
            'cpp':
'''
if( not error.has_value() )
    throw std::invalid_argument("error");
return error.value();
''',
            'typescript':
'''
if( this.error === undefined )
    throw new Error("error");
return this.error;
''',
        }
    ))
    obj.methods.append(Function (
        'Add',
        EvaluationPoint,
        args = [Variable('histogram',Histogram)],
        code = {
            'python':
'''
self.histograms.append(histogram)
return self
''',
            'cpp':
'''
histograms.push_back(histogram);
return *this;
''',
            'typescript':
'''
this.histograms.push(histogram);
return this;
''',
        }
    ))
    objs.append(obj)

    obj = Struct ('Parameter')
    obj.attributes.append(Variable('value','float'))
    obj.attributes.append(Variable('step','float'))
    obj.attributes.append(Variable('min','float'))
    obj.attributes.append(Variable('max','float'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('value','float',nan),
            Variable('step','float',nan),
            Variable('min','float',nan),
            Variable('max','float',nan),
        ],
        mapping = [
            ('value',[Variable('value')]),
            ('step',[Variable('step')]),
            ('min',[Variable('min')]),
            ('max',[Variable('max')]),
        ]
    ))
    objs.append(obj)

    obj = Struct ('Model')
    Model = obj
    obj.attributes.append(Variable('TimeStart','float'))
    obj.attributes.append(Variable('TimeSteps','int'))
    obj.attributes.append(Variable('NumPaths','int'))
    obj.attributes.append(Variable('updaters',Updater,list=True))
    obj.attributes.append(Variable('evaluations',EvaluationPoint,list=True))
    obj.attributes.append(Variable('RandomSeed','int'))
    obj.attributes.append(Variable('RunTimeoutSeconds','float'))
    obj.attributes.append(Variable('MemoryLimitKB','int'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('TimeStart','float',nan),
            Variable('TimeSteps','int',0),
            Variable('NumPaths','int',0),
            Variable('updaters',Updater,[],list=True),
            Variable('evaluations',EvaluationPoint,[],list=True),
            Variable('RandomSeed','int',-1),
            Variable('RunTimeoutSeconds','float',1),
            Variable('MemoryLimitKB','int',1),
        ],
        mapping = [
            ('TimeStart',[Variable('TimeStart')]),
            ('TimeSteps',[Variable('TimeSteps')]),
            ('NumPaths',[Variable('NumPaths')]),
            ('updaters',[Variable('updaters')]),
            ('evaluations',[Variable('evaluations')]),
            ('RandomSeed',[Variable('RandomSeed')]),
            ('RunTimeoutSeconds',[Variable('RunTimeoutSeconds')]),
            ('MemoryLimitKB',[Variable('MemoryLimitKB')]),
        ]
    ))

    obj.methods.append(Function (
        'GetNumberOfUpdaters',
        'int',
        const = True,
        code = {
            'python':
'''
return len(self.updaters)
''',
            'cpp':
'''
return updaters.size();
''',
            'typescript':
'''
return this.updaters.length;
''',
            'csharp':
'''
return updaters.Count();
'''
        }
    ))

    obj.methods.append(Function (
        'GetNumberOfStates',
        'int',
        const = True,
        code = {
            'python':
'''
return len([u for u in self.updaters if u.HasState()])
''',
            'cpp':
'''
int n {0};
for(const auto &u: updaters)
    n += u.HasState();
return n;
''',
            'typescript':
'''
return this.updaters.filter(
    u => u.HasState()
).length;
'''
        }
    ))

    obj.methods.append(Function (
        'Add',
        Updater,
        args = [Variable('updater',Updater)],
        code = {
            'python':
'''
self.updaters.append(updater)
updater._equation = self.GetNumberOfUpdaters()-1
updater._state = self.GetNumberOfStates()-1 if updater.HasState() else None
return updater
''',
            'cpp':
'''
updaters.push_back(updater);
auto &u = updaters.back();
u._equation = GetNumberOfUpdaters()-1;
if(u.HasState())
    u._state = GetNumberOfStates()-1;
return u;
''',
            'typescript':
'''
this.updaters.push(updater);
updater._equation = this.GetNumberOfUpdaters()-1;
if(updater.HasState())
    updater._state = this.GetNumberOfStates()-1;
return updater;
''',
        }
    ))

    objs.append(obj)

    obj = Struct('Result')
    Result = obj
    obj.attributes.append(Variable('n','int'))
    obj.attributes.append(Variable('mean','float'))
    obj.attributes.append(Variable('stddev','float'))
    obj.attributes.append(Variable('skewness','float'))

    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('n','int',0),
            Variable('mean','float',nan),
            Variable('stddev','float',nan),
            Variable('skewness','float',nan),
        ],
        mapping = [
            ('n',[Variable('n')]),
            ('mean',[Variable('mean')]),
            ('stddev',[Variable('stddev')]),
            ('skewness',[Variable('skewness')]),
        ]
    ))

    obj.methods.append(Function (
        'GetMean',
        'float',
        const = True,
        code = {
            'python':
'''
return self.mean
''',
            'cpp':
'''
return mean;
''',
            'typescript':
'''
return this.mean;
''',
        }
    ))

    obj.methods.append(Function (
        'GetMeanError',
        'float',
        const = True,
        code = {
            'python':
'''
return nan if self.n<=0 else self.stddev/math.sqrt(self.n)
''',
            'cpp':
'''
return n<=0 ? NAN : stddev/std::sqrt(n);
''',
            'typescript':
'''
return this.n<=0 ? Number.NaN : this.stddev/Math.sqrt(this.n);
''',
        }
    ))

    obj.methods.append(Function (
        'GetStdDev',
        'float',
        const = True,
        code = {
            'python':
'''
return self.stddev
''',
            'cpp':
'''
return stddev;
''',
            'typescript':
'''
return this.stddev;
''',
        }
    ))

    obj.methods.append(Function (
        'GetSkewness',
        'float',
        const = True,
        code = {
            'python':
'''
return self.skewness
''',
            'cpp':
'''
return skewness;
''',
            'typescript':
'''
return this.skewness;
''',
        }
    ))

    objs.append(obj)


    obj = Struct('EvaluationResults')
    EvaluationResults = obj
    obj.attributes.append(Variable('names','string',list=True))
    obj.attributes.append(Variable('npaths','int',list=True))
    obj.attributes.append(Variable('mean','float',list=True))
    obj.attributes.append(Variable('stddev','float',list=True))
    obj.attributes.append(Variable('skewness','float',list=True))
    obj.attributes.append(Variable('time_points','float',list=True))
    obj.attributes.append(Variable('time_steps','int',list=True))
    obj.attributes.append(Variable('histograms',Histogram,list=True))
    obj.attributes.append(Variable('model',Model,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('names','string',[],list=True),
            Variable('npaths','int',[],list=True),
            Variable('mean','float',[],list=True),
            Variable('stddev','float',[],list=True),
            Variable('skewness','float',[],list=True),
            Variable('time_points','float',[],list=True),
            Variable('time_steps','int',[],list=True),
            Variable('histograms',Histogram,[],list=True),
            Variable('model',Model,None,optional=True),
        ],
        mapping = [
            ('names',[Variable('names')]),
            ('npaths',[Variable('npaths')]),
            ('mean',[Variable('mean')]),
            ('stddev',[Variable('stddev')]),
            ('skewness',[Variable('skewness')]),
            ('time_points',[Variable('time_points')]),
            ('time_steps',[Variable('time_steps')]),
            ('histograms',[Variable('histograms')]),
            ('model',[Variable('model')]),
        ]
    ))

    obj.methods.append(Function (
        'GetNumberOfStates',
        'int',
        const = True,
        code = {
            'python':
'''
return len(self.names)
''',
            'cpp':
'''
return names.size();
''',
            'typescript':
'''
return this.names.length;
''',
        }
    ))

    obj.methods.append(Function (
        'GetNumberOfEvaluations',
        'int',
        const = True,
        code = {
            'python':
'''
return len(self.time_points)
''',
            'cpp':
'''
return time_points.size();
''',
            'typescript':
'''
return this.time_points.length;
''',
        }
    ))

    obj.methods.append(Function (
        'Index',
        'int',
        args = [
            Variable('state','int'),
            Variable('point','int')
        ],
        const = True,
        code = {
            'python':
'''
if not (state>=0 and state<self.GetNumberOfStates() and point>=0 and point<self.GetNumberOfEvaluations()):
    raise ValueError()
return point*self.GetNumberOfStates() + state
''',
            'cpp':
'''
if( not (state>=0 and state<GetNumberOfStates() and point>=0 and point<GetNumberOfEvaluations()) )
    throw std::invalid_argument("Index");
return point*GetNumberOfStates() + state;
''',
            'typescript':
'''
if( !(state>=0 && state<this.GetNumberOfStates() && point>=0 && point<this.GetNumberOfEvaluations()))
    throw new Error(`Index`);
return point*this.GetNumberOfStates() + state;
''',
        }
    ))

    obj.methods.append(Function (
        'GetStateEvaluationResult',
        Result,
        args = [
            Variable('state','int'),
            Variable('point','int')
        ],
        const = True,
        code = {
            'python':
'''
n = self.Index(state,point)
return Result(self.npaths[n],self.mean[n],self.stddev[n],self.skewness[n])
''',
            'cpp':
'''
auto n = Index(state,point);
return Result(npaths[n],mean[n],stddev[n],skewness[n]);
''',
            'typescript':
'''
const n = this.Index(state,point);
return new Result(this.npaths[n],this.mean[n],this.stddev[n],this.skewness[n]);
''',
        }
    ))

    obj.methods.append(Function (
        'df',
        'any',
        const = True,
        code = {
            'python':
'''
data = []
for j in range(self.GetNumberOfEvaluations()):
    for i in range(self.GetNumberOfStates()):
        n = self.Index(i,j)
        item = {
            'name': self.names[i],
            'title': '',
            'state': i,
            'time': self.time_points[j],
            'step': self.time_steps[j],
            'npaths': self.npaths[n],
            'mean':self.mean[n],
            'mean_error': None if self.stddev[n] is None else self.stddev[n]/math.sqrt(self.npaths[n]),
            'stddev': self.stddev[n],
            'skewness': self.skewness[n]
        }
        # if self.model:
        #     item['title'] = self.model._titles.get(i,'')
        data.append(item)
return pd.DataFrame(data)
''',
        }
    ))

    objs.append(obj)

    objs.append(CodeBlock(code={
        'python': {'''
def EvaluationResults_from_response(r,model=None):
    er = EvaluationResults_from_json_string(r.text)
    er.model = model
    return er
'''
        }
    }))

#     obj.methods.append(Function (
#         'random_Linear1DInterpolation',
#         Variable('',Linear1DInterpolation,list=True),
#         args = [],
#         code = {
#             'cpp' : '''
# return Linear1DInterpolation (
#     random_int(),
#     random_float(),
#     random_float(),
#     random_list_float(2,5),
#     random_string()
# );
# '''
#         }
#     ))

    return objs

if __name__ == '__main__':

    languages = ['python','cpp','typescript']
    objs = schema()

    for language in languages:
        write_objs('output/dto','output/dto_test',language,objs)

    for lang1 in languages:
        for lang2 in languages:
            print(f'Testing: {lang1} {lang2}')
            run_round_trip_tests(lang1,lang2,objs,'output')
