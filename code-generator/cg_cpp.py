from cg_all import *
import math

def cpp_type (name:str):
    return {
        'void'   : 'void',
        'string' : 'std::string',
        'int'    : 'int',
        'int[]'  : 'std::vector<int>',
        'float'  : 'float',
        'float[]': 'std::vector<float>',
    }.get(name,name)

def cpp_value (arg):
    if type(arg)==float:
        if math.isnan(arg):
            return 'NAN'
    return arg

def Function_cpp(self:Function, obj:Struct=None):
    ftype = cpp_type(self.type)+' '
    ctor = False
    derived = False
    if obj:
        derived = obj.base is not None
        if self.name==obj.name:
            ftype = '' # constructor
            ctor = True
            assert len(self.args)==0

    code = []
    code.append(f'{ftype}{self.name} (')

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
        default = '' if a.defval is None else f' = {cpp_value(a.defval)}'
        args_code.append(f'{indent}{cpp_type(a.type)} {a.name}{default}')
    for i in range(len(args_code)-1):
        args_code[i] += ','
    code.extend(args_code)

    if derived and ctor:
        code.append(f') : {obj.base.name} (')
        args_code = []
        for a in obj.base.GetAllAttributes():
            args_code.append(f'{indent}{a.name}')
        for i in range(len(args_code)-1):
            args_code[i] += ','
        code.extend(args_code)
        code.append('){')
    else:
        code.append('){')
    if ctor:
        for a in obj.attributes:
            code.append(f'{indent}this->{a.name} = {a.name};')
    else:
        for line in get_lines(self.lines.get('cpp')):
            code.append(f'{indent}{line}')

    code.append('}')

    return code

def Struct_cpp (self:Struct):
    code = []
    if self.base:
        code.append(f'class {self.name}: public {self.base.name} {{')
    else:
        code.append(f'class {self.name} {{')
    code.append(f'public:')
    code.append(f'')
    
    for a in self.attributes:
        code.append(f'{indent}{cpp_type(a.type)} {a.name};')

    code.append('')

    for func in self.methods:
        for line in Function_cpp(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'}};')
    return code


def File_prefix_cpp (objs):
    return [
        f'// {autogen_text}',
        '',
        '#include <string>',
        '#include <vector>',
        '#include <stdexcept>',
        '#include <cmath> // NAN',
        ''
    ]

def cpp_run_test(fname):
    asyncio.run(run(f'g++ {fname} -o {fname}.exe && {fname}.exe'))
