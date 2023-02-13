from cg import *
from math import nan

def create_dto(fname, languages):

    objs = [] # objects in the file

    obj = Struct('UpdaterDoc')
    obj.attributes.append(Variable('name','string',None))
    obj.attributes.append(Variable('title','string',None))
    obj.attributes.append(Variable('doc_md','string',None))
    obj.attributes.append(Variable('start','string',None))
    obj.attributes.append(Variable('nargs_min','int',None))
    obj.attributes.append(Variable('nrefs_min','int',None))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     mapping = [
    #         ('name',['']),
    #         ('title',['']),
    #         ('doc_md',['']),
    #         ('start',['']),
    #         ('nargs_min',[-1]),
    #         ('nrefs_min',[-1]),
    #     ]
    # ))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',''),
            Variable('title','string',''),
            Variable('doc_md','string',''),
            Variable('start','string',''),
            Variable('nargs_min','int',-1),
            Variable('nrefs_min','int',-1)
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
    obj.attributes.append(Variable('name','string',None))
    obj.attributes.append(Variable('refs','int[]',None))
    obj.attributes.append(Variable('args','float[]',None))
    obj.attributes.append(Variable('start','float',None))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',''),
            Variable('refs','int[]',[]),
            Variable('args','float[]',[]),
            Variable('start','float',nan)
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
    obj.attributes.append(Variable('_equation','int',-1))
    obj.attributes.append(Variable('_state','int',-1))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',''),
            Variable('refs','int[]',[]),
            Variable('args','float[]',[]),
            Variable('start','float',nan)
        ],
        mapping = [(obj.base.name,[
            Variable('name'),
            Variable('refs'),
            Variable('args'),
            Variable('start'),
        ])]
    ))
    obj.methods.append(Function (
        'GetStateNumber',
        'int',
        lines = {
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
        'TTTT',
        'int',
        args = [Variable('arg','int',-11)],
        lines = {
            'typescript':
'''
return arg;
''',
            'cpp':
'''
return arg;
''',
            'python':
'''
return arg
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

    obj = Struct('IndependentGaussian',Updater,generate_json=False)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('refs_','int[]'  ,None),
        ],
        mapping = [(obj.base.name,[
            'IndependentGaussian',
            Variable('refs_'),
            [],
            nan
        ])]
    ))
    objs.append(obj)
    
    obj = Struct('CorrelatedGaussian',Updater,generate_json=False)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('correlation','float'  ,None),
            Variable('state1','int'  ,None),
            Variable('state2','int'  ,None),
        ],
        mapping = [(obj.base.name,[
            'CorrelatedGaussian',
            [Variable('state1'),Variable('state2')],
            [Variable('correlation')],
            nan,
        ])]
    ))
    objs.append(obj)

    # 'Barrier' is an updater with special arguments
    obj = Struct('Barrier',Updater,generate_json=False)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying','int'  ,None),
            Variable('start'     ,'float',None),
            Variable('level'     ,'float',None),
            Variable('direction' ,'int'  ,None),
            Variable('action'    ,'int'  ,None),
            Variable('value'     ,'float',None),
        ],
#         lines = {
#             'python':
# '''
# super().__init__('Barrier',[underlying],[level, value, direction, action],start)
# ''',
#             'typescript':
# '''
# super('Barrier',[underlying],[level, value, direction, action],start)
# '''
#         },
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
            Variable('start')
        ])]
    ))
    
    objs.append(obj)

    obj = Struct('HistogramAxis')
    obj.attributes.append(Variable('state','int',-1))
    obj.attributes.append(Variable('nbins','int',0))
    obj.attributes.append(Variable('min','float',nan))
    obj.attributes.append(Variable('max','float',nan))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('_state','int',-1),
            Variable('_nbins','int',-1),
            Variable('_min'  ,'float',nan),
            Variable('_max'  ,'float',nan),
        ],
        mapping = [
            ('state',[Variable('_state')]),
            ('nbins',[Variable('_nbins')]),
            ('min',[Variable('_min')]),
            ('max',[Variable('_max')]),
        ]
    ))
    objs.append(obj)

    # obj = Struct('Histogram1D')
    # obj.attributes.append(Variable('x','HistogramAxis',None))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     args = [
    #         Variable('x','HistogramAxis',None),
    #     ],
    #     mapping = [('x',[
    #         Variable('x'),
    #     ])]
    # ))
    # objs.append(obj)

    # obj = Struct('Histogram2D')
    # obj.attributes.append(Variable('x','HistogramAxis',None))
    # obj.attributes.append(Variable('y','HistogramAxis',None))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     args = [
    #         Variable('x','HistogramAxis',None),
    #         Variable('y','HistogramAxis',None),
    #     ],
    #     mapping = [
    #         ('x',[Variable('x')]),
    #         ('y',[Variable('y')])
    #     ]
    # ))
    # objs.append(obj)

    obj = Struct('Histogram')
    obj.attributes.append(Variable('x','HistogramAxis',None))
    obj.attributes.append(Variable('y','HistogramAxis',None))
    obj.methods.append(Function (
        obj.name,
        'constructor'
    ))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     args = [
    #         Variable('x','HistogramAxis',None),
    #     ],
    #     mapping = [
    #         ('x',[Variable('x')]),
    #     ]
    # ))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     args = [
    #         Variable('x','HistogramAxis',None),
    #         Variable('y','HistogramAxis',None),
    #     ],
    #     mapping = [
    #         ('x',[Variable('x')]),
    #         ('y',[Variable('y')])
    #     ]
    # ))
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
    obj.attributes.append(Variable('state','int',None))
    obj.attributes.append(Variable('time','float',None))
    obj.attributes.append(Variable('value','float',None))
    obj.attributes.append(Variable('error','float',None))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('state_','int',-1),
            Variable('time_','float',nan),
            Variable('value_','float',nan),
            Variable('error_','float',nan),
        ],
        mapping = [
            ('state',[Variable('state_')]),
            ('time',[Variable('time_')]),
            ('value',[Variable('value_')]),
            ('error',[Variable('error_')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('EvaluationResults')
    obj.attributes.append(Variable('names','string[]',None))
    obj.attributes.append(Variable('npaths','int[]',None))
    obj.attributes.append(Variable('mean','float[]',None))
    obj.attributes.append(Variable('stddev','float[]',None))
    obj.attributes.append(Variable('skewness','float[]',None))
    obj.attributes.append(Variable('time_points','float[]',None))
    obj.attributes.append(Variable('time_steps','int[]',None))
    obj.attributes.append(Variable('histograms','Histogram[]',None))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('names_','string[]',[]),
            Variable('npaths_','int[]',[]),
            Variable('mean_','float[]',[]),
            Variable('stddev_','float[]',[]),
            Variable('skewness_','float[]',[]),
            Variable('time_points_','float[]',[]),
            Variable('time_steps_','int[]',[]),
            Variable('histograms_','Histogram[]',[]),
        ],
        mapping = [
            ('names',[Variable('names_')]),
            ('npaths',[Variable('npaths_')]),
            ('mean',[Variable('mean_')]),
            ('stddev',[Variable('stddev_')]),
            ('skewness',[Variable('skewness_')]),
            ('time_points',[Variable('time_points_')]),
            ('time_steps',[Variable('time_steps_')]),
            ('histograms',[Variable('histograms_')]),
        ]
    ))
    objs.append(obj)

    obj = Struct ('Parameter')
    obj.attributes.append(Variable('value','float',None))
    obj.attributes.append(Variable('step','float',None))
    obj.attributes.append(Variable('min','float',None))
    obj.attributes.append(Variable('max','float',None))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('value_','float',nan),
            Variable('step_','float',nan),
            Variable('min_','float',nan),
            Variable('max_','float',nan),
        ],
        mapping = [
            ('value',[Variable('value_')]),
            ('step',[Variable('step_')]),
            ('min',[Variable('min_')]),
            ('max',[Variable('max_')]),
        ]
    ))
    objs.append(obj)

    obj = Struct ('Model')
    obj.attributes.append(Variable('TimeStart','float',None))
    obj.attributes.append(Variable('TimeSteps','int',None))
    obj.attributes.append(Variable('NumPaths','int',None))
    obj.attributes.append(Variable('updaters','Updater[]',None))
    obj.attributes.append(Variable('evaluations','EvaluationPoint[]',None))
    obj.attributes.append(Variable('RunTimeoutSeconds','float',None))
    obj.attributes.append(Variable('MemoryLimitKB','int',None))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('TimeStart_','float',nan),
            Variable('TimeSteps_','int',0),
            Variable('NumPaths_','int',0),
            Variable('updaters_','Updater[]',[]),
            Variable('evaluations_','EvaluationPoint[]',[]),
            Variable('RunTimeoutSeconds_','float',1),
            Variable('MemoryLimitKB_','int',1),
        ],
        mapping = [
            ('TimeStart',[Variable('TimeStart_')]),
            ('TimeSteps',[Variable('TimeSteps_')]),
            ('NumPaths',[Variable('NumPaths_')]),
            ('updaters',[Variable('updaters_')]),
            ('evaluations',[Variable('evaluations_')]),
            ('RunTimeoutSeconds',[Variable('RunTimeoutSeconds_')]),
            ('MemoryLimitKB',[Variable('MemoryLimitKB_')]),
        ]
    ))
    objs.append(obj)

    for language in languages:
        write_objs(fname,language,objs)

class File:
    def __init__ (self, file_name:str):
        self.file_name = file_name
        self.objs = []

def write_file (f, language):
    for obj in f.objs:
        lines = obj[language]
        with open(f.file_name + '.' + ext[language],'w') as file:
            for line in get_lines(lines):
                file.write(line+'\n')
                
def create_dto_test(fname,languages):
    f = File(fname)
    f.objs.append({
        'typescript':
'''
import {describe, expect, test, it} from '@jest/globals';

test('sum', function() {
    expect(1+4).toBe(5);
});
''',
        'cpp':
'''
#include "ut.hpp"
#include "dto.cpp"


int main (void) {
    using namespace boost::ut;
    "sum"_test = [&] {
        expect(that% (1+4)==5);
    };    
    "UpdaterDoc ctor"_test = [&] {
        auto doc1 = UpdaterDoc ("name","title","doc_md","start",1,2);
        //auto js1 = UpdaterDoc_to_JSON(doc1);
        //auto doc2 = UpdaterDoc_from_json(js1);
        //expect(that% doc1==doc2);
    };    
    return 0;
}
''',
        'python':
'''
def test_sum():
    assert 1+4 == 5
'''
    })

    for language in languages:
        write_file(f,language)
        run_test(f.file_name + '.' + ext[language],language)


if __name__ == '__main__':

    # languages = ('python','cpp','typescript')
    languages = ('python','cpp')
    create_dto('output/dto',languages)
    create_dto_test('output/dto-test',languages)
