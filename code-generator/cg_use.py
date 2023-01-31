from cg import *

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
    obj.methods.append(Function (obj.name,''))
    objs.append(obj)

    obj = Struct('UpdaterDto')
    obj.attributes.append(Variable('name','string',None))
    obj.attributes.append(Variable('refs','int[]',None))
    obj.attributes.append(Variable('args','float[]',None))
    obj.attributes.append(Variable('start','float',None))
    obj.methods.append(Function (obj.name,''))
    objs.append(obj)
    UpdaterDto = obj

    obj = Struct('Updater',UpdaterDto)
    obj.attributes.append(Variable('_equation','int',-1))
    obj.attributes.append(Variable('_state','int',-1))
    obj.methods.append(Function (obj.name,''))
    objs.append(obj)
    Updater = obj

    obj = Struct('UpdaterDerived',Updater)
    obj.attributes.append(Variable('__ok','string','aaaaa!'))
    obj.methods.append(Function (obj.name,''))
    objs.append(obj)

    for language in ('python','cpp','typescript'):
        write_objs(fname,language,objs)
