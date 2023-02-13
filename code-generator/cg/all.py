# This file can be (and should be) imported
# by all language-specific implementations.

import asyncio
from collections import namedtuple

indent = ' '*4
autogen_text = 'This is an automatically generated file.'

Variable = namedtuple('Variable',['name','type','defval'],defaults=['',None,None])

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

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    assert proc.returncode==0
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
