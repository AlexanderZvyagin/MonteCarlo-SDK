from .all import *

def File_prefix_python (objs):
    return [
        f'# {autogen_text}',
        'from math import nan',
        'import json',
        '# 1',
        ''
    ]

def python_type_to_string (name:str):
    return {
        'string' : 'str',
        'int'    : 'int',
        'int[]'  : 'list[int]',
        'float'  : 'float',
        'float[]': 'list[float]',
    }.get(name,name)

def python_value_to_string (arg):
    if type(arg)==Variable:
        return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'{{{y}}}'
    elif type(arg)==str:
        return f'"{arg}"'
    else:
        return str(arg)

def Constructor_python(ctor:Function,base:Struct):
    assert ctor.name == base.name
    code = []
    code.append('')
    
    code.append(f'def __init__ (')
    code.append(f'{indent}self,')
    for i,arg in enumerate(ctor.args):
        defval = '' if arg.defval is None else f' = {python_value_to_string(arg.defval)}'
        code.append(f'{indent}{arg.name}{defval}{"," if i+1<len(ctor.args) else ""}')
    code.append(f'):')

    for i,(name,mapping) in enumerate(ctor.mapping):
        if base.base and name==base.base.name:
            code.append(f'{indent}super.__init__(')
            for arg in mapping:
                code.append(f'{indent*2}{python_value_to_string(arg)},')
            code.append(f'{indent})')
        else:
            assert len(mapping)==1
            arg = mapping[0]
            code.append(f'{indent}self.{name} = {python_value_to_string(arg)}')

    return code

def Function_python(self:Function, obj:Struct=None):
    code = []

    if obj and self.name==obj.name:
        code = Constructor_python(self,obj)
    else:
        code = []
        code.append(f'def {self.name} (')
        if obj:
            code.append(f'{indent}self,')

        for a in self.args:
            default = '' if a.defval is None else f' = {python_value_to_string(a.defval)}'
            code.append(f'{indent}{a.name}{default}')
        code.append('):')

    for line in get_lines(self.lines.get('python')):
        code.append(f'{indent}{line}')

    code.append(f'{indent}pass')
    return code

def Struct_python (self:Struct):
    code = []
    if self.base:
        code.append(f'class {self.name} ({self.base.name}):')
    else:
        code.append(f'class {self.name}:')
    code.append('')
    
    for func in self.methods:
        for line in Function_python(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    if self.generate_json:
        code.extend(Struct_to_JSON_string_python(self))

    return code

def Struct_to_JSON_string_python (self):
    return [
        f'def {self.name}_to_JSON (self):',
        f"{indent}return json.dumps(self,default=lambda o: {{k:v for k,v in o.__dict__.items() if k[0]!='_'}})"
    ]

def python_run_test(fname):
    asyncio.run(run(f'pytest {fname}'))
