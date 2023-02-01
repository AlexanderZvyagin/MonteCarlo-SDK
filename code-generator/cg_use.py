from cg import *
from math import nan

if __name__ == '__main__':

    fname = 'output/dto'
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
        body_language = {
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

    for language in ('python','cpp','typescript'):
        write_objs(fname,language,objs)
