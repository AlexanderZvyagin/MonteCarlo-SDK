# This file can be (and should be) imported
# by all language-specific implementations.

import asyncio
from collections import namedtuple

indent = ' '*4
autogen_text = 'This is an automatically generated file.'

Variable = namedtuple('Variable',['name','type','defval'])

class Struct:
    '''Holds info on a structure.
    
    Should contain info enough to generate code for all languages.
    '''
    def __init__ (self, name:str, base=None):
        self.name = name
        self.attributes = []
        self.methods = []
        self.base = base # Struct
    def __repr__ (self):
        return f"Struct('{self.name}',base={self.base}) #attributes={len(self.attributes)} #methods={len(self.methods)}"
    def GetAllAttributes (self):
        attrs = []
        this = self
        while this:
            attrs = [a for a in this.attributes] + attrs
            this = this.base
        return attrs

class Function:
    def __init__ (self, name:str, type:str, args=[], lines={}):
        '''lines: dictionary of language:str=>list[str]'''
        self.name = name
        self.type = type
        self.args = args
        self.lines = lines
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
