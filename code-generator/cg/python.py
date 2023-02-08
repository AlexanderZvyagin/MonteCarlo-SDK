from .all import *

def File_prefix_python (objs):
    return [
        f'# {autogen_text}',
        'from math import nan',
        'import json',
        '# 1',
        ''
    ]

def python_type (name:str):
    return {
        'string' : 'str',
        'int'    : 'int',
        'int[]'  : 'list[int]',
        'float'  : 'float',
        'float[]': 'list[float]',
    }.get(name,name)

def python_value (arg):
    return str(arg)

def Function_python(self:Function, obj:Struct=None):
    fname = self.name
    ctor = False
    derived = False
    if obj:
        derived = obj.base is not None
        if self.name==obj.name:
            fname = '__init__'
            ctor = True

    attributes = []
    if ctor:
        if self.type == 'ctor-all-attributes':
            assert len(self.args)==0
            attributes = obj.GetAllAttributes()
        elif self.type == 'ctor-special':
            attributes = self.args
        else:
            print(f'not supported: ctor type "{self.type}"')
    else:
        attributes = self.args

    code = []
    code.append(f'def {fname} (')

    args_code = []
    if obj:
        args_code.append(f'{indent}self')
    for a in attributes:
        default = '' if a.defval is None else f' = {python_value(a.defval)}'
        args_code.append(f'{indent}{a.name} : {python_type(a.type)}{default}')
    for i in range(len(args_code)-1):
        args_code[i] += ','
    code.extend(args_code)

    code.append('):')
    if self.type == 'ctor-all-attributes':
        if derived:
            super_args = []
            code_init = []
            for a in obj.GetAllAttributes():
                if a.name in [v.name for v in obj.base.GetAllAttributes()]:
                    super_args.append(a.name)
                else:
                    code_init.append(f'{indent}self.{a.name} = {a.name}')
            code.append(f'{indent}super().__init__({",".join(super_args)})')
            code.extend(code_init)
        else:
            for a in obj.attributes:
                code.append(f'{indent}self.{a.name} = {a.name}')
    for line in get_lines(self.lines.get('python')):
        code.append(f'{indent}{line}')

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
    
    return code

def Struct_to_JSON_python (self):
    return [
        f'def {self.name}_to_JSON (self):',
        f"{indent}return json.dumps(self,default=lambda o: {{k:v for k,v in o.__dict__.items() if k[0]!='_'}})"
    ]

def python_run_test(fname):
    asyncio.run(run(f'pytest {fname}'))
