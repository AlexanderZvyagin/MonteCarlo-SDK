from .all import *
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

# derived ctor
def Constructor_cpp(ctor:Function,base:Struct):
    debug = False
    assert ctor.name == base.name
    code = []
    code.append('')
    
    if debug:
        for arg in ctor.args:
            code.append(f'//       {arg}')
        predecessors = []
        this = base
        while this:
            predecessors.append(this.name)
            code.append(f'//   {".".join(predecessors)} attributes:')
            for attr in this.attributes:
                code.append(f'//       {attr}')
            this = this.base
    
        code.append(f'//   this class attributes which are not present in the ctor args')
        x = [attr for attr in base.attributes if attr.name not in ctor.args]
        code.append(f'//     {x}')

    code.append(f'{ctor.name} (')
    for i,arg in enumerate(ctor.args):
        code.append(f'{indent}{cpp_type(arg.type)} {arg.name}{"," if i+1<len(ctor.args) else ""}')
    code.append(f')')

    for i,(name,mapping) in enumerate(ctor.mapping):
        code.append(f'{":" if i==0 else ","} {name} (')
        for i,(k,v) in enumerate(mapping):
            if isinstance(v,Variable):
                line = f'{v.name}'
            elif isinstance(v,list):
                # x = [ f'({get_type(item.name)}) {item.name}'   for item in v]
                x = [ f'{item.name}'   for item in v]
                y = ','.join(x)
                line = f'{{{y}}}'
            elif isinstance(v,str):
                line = f'"{v}"'
            else:
                line = str(v)
            code.append(indent + line + (',' if i+1<len(mapping) else ''))
        code.append(')')

    return code

def Function_cpp(self:Function, obj:Struct=None):

    code = []

    if obj and self.name==obj.name:
        code = Constructor_cpp(self,obj)
    else:
        ftype = cpp_type(self.type)+' '

        code = []
        code.append(f'{ftype}{self.name} (')

        args_code = []
        for a in self.args:
            default = '' if a.defval is None else f' = {cpp_value(a.defval)}'
            args_code.append(f'{indent}{cpp_type(a.type)} {a.name}{default}')
        for i in range(len(args_code)-1):
            args_code[i] += ','
        code.extend(args_code)
        code.append(')')

    code.append('{')
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
        '',
        '#include <nlohmann/json.hpp>',
        'using json = nlohmann::json;',
        '',
    ]

def cpp_run_test(fname):
    incdir = '-I /home/zvyagin/Projects/MonteCarlo/MonteCarlo-to-gitlab/external/json/include'
    cmd = f'g++ {incdir} {fname} -o {fname}.exe && {fname}.exe'
    asyncio.run(run(cmd))
