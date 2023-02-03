import math
from .all import *
from .python import *
from .typescript import *
from .cpp import *

ext = {
    'cpp' : 'cpp',
    'python' : 'py',
    'typescript' : 'ts'
}

def write_objs(fname:str,language,objs=[]):
    '''fname: full path name without extension, the file will be overwritten. the directory path must exist.'''
    with open(fname+'.'+ext[language],'w') as file:
        file_prefix_code = globals().get(f'File_prefix_{language}')
        if file_prefix_code:
            for line in file_prefix_code(objs):
                file.write(line+'\n')
        for obj in objs:
            if isinstance(obj,Struct):
                for prefix in ('Struct','Struct_from_JSON','Struct_to_JSON'):
                    name = f'{prefix}_{language}'
                    func = globals().get(name)
                    if func:
                        for line in func(obj):
                            file.write(line+'\n')
                        file.write('\n')
                    else:
                        print(f'There is no function {name}')
            elif isinstance(obj,Function):
                name = f'Function_{language}'
                func = globals().get(name)
                if func:
                    for line in func(obj):
                        file.write(line+'\n')
            else:
                print(f'Cannot handle {type(obj)}')

        file_suffix_code = globals().get(f'File_suffix_{language}')
        if file_suffix_code:
            for line in file_suffix_code(objs):
                file.write(line+'\n')
