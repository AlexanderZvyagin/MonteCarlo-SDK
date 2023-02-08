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
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',None),
            Variable('title','string',None),
            Variable('doc_md','string',None),
            Variable('start','string',None),
            Variable('nargs_min','int',None),
            Variable('nrefs_min','int',None)
        ],
        mapping = [
            ('name',[('name',Variable('name'))]),
            ('title',[('title',Variable('title'))]),
            ('doc_md',[('doc_md',Variable('doc_md'))]),
            ('start',[('start',Variable('start'))]),
            ('nargs_min',[('nargs_min',Variable('nargs_min'))]),
            ('nrefs_min',[('nrefs_min',Variable('nrefs_min'))]),
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
            Variable('name','string',None),
            Variable('refs','int[]',None),
            Variable('args','float[]',None),
            Variable('start','float',None)
        ],
        mapping = [
            ('name',[('name',Variable('name'))]),
            ('refs',[('refs',Variable('refs'))]),
            ('args',[('args',Variable('args'))]),
            ('start',[('start',Variable('start'))]),
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
            Variable('name','string',None),
            Variable('refs','int[]',None),
            Variable('args','float[]',None),
            Variable('start','float',None)
        ],
        mapping = [
            (obj.base.name,[
                ('name',Variable('name')),
                ('refs',Variable('refs')),
                ('args',Variable('args')),
                ('start',Variable('start')),
            ])
        ]
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
    objs.append(obj)
    Updater = obj

    # 'Barrier' is an updater with special arguments
    obj = Struct('Barrier',Updater)
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
        lines = {
            'python':
'''
super().__init__('Barrier',[underlying],[level, value, direction, action],start)
''',
            'typescript':
'''
super('Barrier',[underlying],[level, value, direction, action],start)
'''
        },
        mapping = [(obj.base.name,[
            ('name','Barrier'),
            ('refs',[
                Variable('underlying')
            ]),
            ('args',[
                Variable('level'),
                Variable('value'),
                Variable('direction'),
                Variable('action')
            ]),
            ('start',Variable('start'))
        ])]
    ))
    
    objs.append(obj)


    obj = Struct('HistogramAxis')
    obj.attributes.append(Variable('state','int',-1))
    obj.attributes.append(Variable('nbins','int',0))
    obj.attributes.append(Variable('min','float',nan))
    obj.attributes.append(Variable('max','float',nan))
    obj.methods.append(Function (obj.name,'constructor'))
    objs.append(obj)

    obj = Struct('Histogram1D')
    obj.attributes.append(Variable('x','HistogramAxis',None))
    obj.methods.append(Function (obj.name,'constructor'))
    objs.append(obj)

    obj = Struct('Histogram2D')
    obj.attributes.append(Variable('x','HistogramAxis',None))
    obj.attributes.append(Variable('y','HistogramAxis',None))
    obj.methods.append(Function (obj.name,'constructor'))
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

    languages = ('python','cpp','typescript')
    create_dto('output/dto',languages)
    create_dto_test('output/dto-test',languages)
