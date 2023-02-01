from cg_all import *
import math

def File_prefix_typescript (objs):
    return [
        f'// {autogen_text}',
        ''
    ]

def File_suffix_typescript (objs):
    code = []
    code.append('export {')
    for i,obj in enumerate(objs):
        c = ',' if (i+1)<len(objs) else ''
        code.append(f'{indent}{obj.name}' + c)
    code.append('}')
    return code

def typescript_type (name:str):
    return {
        'void'   : 'void',
        'string' : 'string',
        'int'    : 'number',
        'int[]'  : 'number[]',
        'float'  : 'number',
        'float[]': 'number[]',
    }.get(name,name)

def typescript_value (arg):
    if type(arg)==float:
        if math.isnan(arg):
            return 'Number.NaN'
    return arg

def Function_typescript (self:Function, obj:Struct=None):
    fname = self.name
    ctor = False
    derived = False
    ftype = self.type
    if obj:
        derived = obj.base is not None
        if self.name==obj.name:
            fname = 'constructor'
            ctor = True
            assert len(self.args)==0
            ftype = ''
        else:
            ftype = f': {typescript_type(self.type)} '

    code = []
    if obj:
        code.append(f'{fname} (')
    else:
        code.append(f'function {fname} (')

    attributes = []
    if ctor:
        if self.type == 'ctor-all-attributes':
            attributes = obj.GetAllAttributes()
        else:
            raise Exception(f'not supported: ctor type "{self.type}"')
    else:
        attributes = self.args

    args_code = []
    for a in attributes:
        default = '' if a.defval is None else f' = {typescript_value(a.defval)}'
        args_code.append(f'{indent}{a.name} : {typescript_type(a.type)}{default}')
    for i in range(len(args_code)-1):
        args_code[i] += ','
    code.extend(args_code)

    code.append(f') {ftype}{{')

    if derived and ctor:
        code.append(f'{indent}super (')
        args_code = []
        for a in obj.base.GetAllAttributes():
            args_code.append(f'{indent*2}{a.name}')
        for i in range(len(args_code)-1):
            args_code[i] += ','
        code.extend(args_code)
        code.append(f'{indent})')
    if not ctor:
        for line in get_body(self.body_language.get('typescript')):
            code.append(f'{indent}{line}')

    code.append('}')

    return code

def Struct_typescript (self:Struct):
    code = []
    if self.base:
        code.append(f'class {self.name} extends {self.base.name} {{')
    else:
        code.append(f'class {self.name} {{')
    code.append('')
    
    for a in self.attributes:
        code.append(f'{indent}{a.name} : {typescript_type(a.type)};')

    code.append('')

    for func in self.methods:
        for line in Function_typescript(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'}}')
    code.append('')
    return code
