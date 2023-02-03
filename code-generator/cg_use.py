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
    obj.methods.append(Function (obj.name,'ctor-all-attributes'))
    objs.append(obj)

    obj = Struct('UpdaterDto')
    obj.attributes.append(Variable('name','string',None))
    obj.attributes.append(Variable('refs','int[]',None))
    obj.attributes.append(Variable('args','float[]',None))
    obj.attributes.append(Variable('start','float',None))
    obj.methods.append(Function (obj.name,'ctor-all-attributes'))
    objs.append(obj)
    UpdaterDto = obj

    obj = Struct('Updater',UpdaterDto)
    obj.attributes.append(Variable('_equation','int',-1))
    obj.attributes.append(Variable('_state','int',-1))
    obj.methods.append(Function (obj.name,'ctor-all-attributes'))
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

    obj = Struct('HistogramAxis')
    obj.attributes.append(Variable('state','int',-1))
    obj.attributes.append(Variable('nbins','int',0))
    obj.attributes.append(Variable('min','float',nan))
    obj.attributes.append(Variable('max','float',nan))
    obj.methods.append(Function (obj.name,'ctor-all-attributes'))
    objs.append(obj)

    obj = Struct('Histogram1D')
    obj.attributes.append(Variable('x','HistogramAxis',None))
    obj.methods.append(Function (obj.name,'ctor-all-attributes'))
    objs.append(obj)

    obj = Struct('Histogram2D')
    obj.attributes.append(Variable('x','HistogramAxis',None))
    obj.attributes.append(Variable('y','HistogramAxis',None))
    obj.methods.append(Function (obj.name,'ctor-all-attributes'))
    objs.append(obj)

    for language in languages:
        write_objs(fname,language,objs)

# def create_dto_test(fname, languages):
#     objs = [] # objects in the file

#     objs.append(File())


#     for language in languages:
#         write_objs(fname,language,objs)

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
                
        # if isinstance(obj,list):
        #     print('ok, list')
        # else:
        #     raise Exception(f'Unsupported type: {type(obj)}')



# asyncio.run(run('ls /zzz'))



# def python_run_test(fname):
#     print(f'python_run_test: {fname}')
#     asyncio.run(run(f'python3 {fname}'))


# def typescript_run_test(fname):
#     asyncio.run(run(f'npx tsx {fname}'))


def run_test(fname,language):
    # asyncio.run(f'python {fname}')
    name = f'{language}_run_test'
    code = globals().get(name)
    if not code:
        print(f'Not found: {name}')
    else:
        code(fname)

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
    
    

    # asyncio.run(run('g++ output/dto.test.cpp -o dto.test.cpp.exe && ls'))

#     objs.append(Function (
#         'test_1',
#         'void',
#         body_language = {
#             'typescript':
# '''
# ''',
#             'cpp':
# '''
# ''',
#             'python':
# '''
# pass
# '''
#         }
#     ))

