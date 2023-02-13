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
                name = f'Struct_{language}'
                func = globals().get(name)
                if func:
                    for line in func(obj):
                        file.write(line+'\n')
                    file.write('\n')
                else:
                    print(f'There is no function {name}')
            elif isinstance(obj,CodeBlock):
                for line in obj.code.get(language,[]):
                    file.write(line+'\n')
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

def run_test(fname,language):
    name = f'{language}_run_test'
    code = globals().get(name)
    if not code:
        print(f'Not found: {name}')
    else:
        code(fname)
