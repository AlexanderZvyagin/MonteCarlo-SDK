# This file can be (and should be) imported
# by all language-specific implementations.

import os, subprocess
from collections import namedtuple

indent = ' '*4
autogen_text = 'This is an automatically generated file.'

Variable = namedtuple('Variable',['name','type','defval'],defaults=['',None,None])

ext = {
    'cpp' : 'cpp',
    'python' : 'py',
    'typescript' : 'ts'
}

def decode_type(type_name:str):
    '''return (bool,str) for is_list and type_string'''
    if type_name[-2:]=='[]':
        return (True,type_name[:-2])
    else:
        return (False,type_name)

class Struct:
    '''Holds info on a structure.
    
    Should contain info enough to generate code for all languages.
    '''
    def __init__ (self, name:str, base=None, generate_json=True):
        self.name = name
        self.attributes = []
        self.methods = []
        self.base = base
        self.generate_json = generate_json
    def __repr__ (self):
        return f"Struct('{self.name}',base={self.base}) #attributes={len(self.attributes)} #methods={len(self.methods)}"
    def GetAllAttributes (self):
        attrs = []
        this = self
        while this:
            attrs = [a for a in this.attributes] + attrs
            this = this.base
        return attrs

class CodeBlock:
    def __init__ (self, code={}):
        self.code = code

class Function:

    class Call:
        '''
        FunctionCall('myfunc',[1,'arg_string',Variable('aa')])
        '''
        def __init__ (self,name:str,args=[]):
            pass

    class Code:
        def __init__ (self,code):
            pass

    def __init__ (self, name:str, type:str, args=[], lines={}, mapping=[]):
        '''lines: dictionary of language:str=>list[str]
        
        mapping: it is an array of (key,value) pairs
        '''
        self.name = name
        self.type = type
        self.args = args

        self.lines = lines
        self.objs  = [] # Call,Code
        self.mapping = mapping

    def __repr__ (self):
        return f"Function('{self.name}','{self.type}',{self.args})"

def get_lines (body):
    if body is None:
        return []
    elif type(body)==str:
        return body.split('\n')
    else:
        return body

# async def run(cmd):
#     proc = await asyncio.create_subprocess_shell(
#         cmd,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)

#     stdout, stderr = await proc.communicate()

#     print(f'[{cmd!r} exited with {proc.returncode}]')
#     assert proc.returncode==0
#     if stdout:
#         print(f'[stdout]\n{stdout.decode()}')
#     if stderr:
#         print(f'[stderr]\n{stderr.decode()}')

def run_test(language,command,struct_name='',file1='',file2=''):
    cmd = [
        './run',
        command,
        struct_name,
        os.path.abspath(file1) if file1 else '',
        os.path.abspath(file2) if file2 else ''
    ]
    proc = subprocess.run (cmd, capture_output=True, text=True, cwd=f'languages/{language}')
    print('')
    print('>>>',cmd)
    print(f'ExitCode={proc.returncode} StdOutLen={len(proc.stdout)} StdErrLen={len(proc.stderr)}')
    for v in ['stdout','stderr']:
        if not getattr(proc,v):
            continue
        print(f'*** {v} ***')
        print(getattr(proc,v))
    proc.check_returncode()

def run_round_trip_tests(lang1,lang2,objs,outdir):

    for lang in [lang1,lang2]:
        run_test(lang,'build')

    for obj in objs:
        if type(obj)!=Struct:
            continue
        struct_name = obj.name
        json_file1 = f'{outdir}/{struct_name}-{lang1}-create.json'
        run_test(lang1,'create',struct_name,json_file1)
        json_file2 = f'{outdir}/{struct_name}-{lang2}-convert.json'
        run_test(lang2,'convert',struct_name,json_file1,json_file2) 
        run_test(lang1,'compare',struct_name,json_file1,json_file2)
