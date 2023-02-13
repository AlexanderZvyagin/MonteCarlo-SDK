from .all import *
import math

def cpp_type_to_string (name:str):

    if name[-2:]=='[]':
        t = cpp_type_to_string(name[:-2])
        return f'std::vector<{t}>'

    return {
        'void'    : 'void',
        'string'  : 'std::string',
        'int'     : 'int',
        'float'   : 'float',
    }.get(name,name)

def cpp_value_to_string (arg):
    if type(arg)==Variable:
        return arg.name
    elif isinstance(arg,list):
        x = [ f'{item.name}'   for item in arg]
        y = ','.join(x)
        return f'{{{y}}}'
    elif isinstance(arg,str):
        return f'"{arg}"'
    elif type(arg)==float:
        if math.isnan(arg):
            return 'NAN'
        else:
            return str(arg)
    else:
        return str(arg)

def Constructor_cpp(ctor:Function,base:Struct):
    assert ctor.name == base.name
    code = []
    code.append('')
    
    code.append(f'{ctor.name} (')
    for i,arg in enumerate(ctor.args):
        defval = '' if arg.defval is None else f' = {cpp_value_to_string(arg.defval)}'
        code.append(f'{indent}{cpp_type_to_string(arg.type)} {arg.name}{defval}{"," if i+1<len(ctor.args) else ""}')
    code.append(f')')

    for i,(name,mapping) in enumerate(ctor.mapping):
        code.append(f'{":" if i==0 else ","} {name} (')
        for i,v in enumerate(mapping):
            line = cpp_value_to_string(v)
            code.append(indent + line + (',' if i+1<len(mapping) else ''))
        code.append(')')

    return code

def Function_cpp(self:Function, obj:Struct=None):

    code = []

    if obj and self.name==obj.name:
        code = Constructor_cpp(self,obj)
    else:
        ftype = cpp_type_to_string(self.type)+' '

        code = []
        code.append(f'{ftype}{self.name} (')

        args_code = []
        for a in self.args:
            default = '' if a.defval is None else f' = {cpp_value_to_string(a.defval)}'
            args_code.append(f'{indent}{cpp_type_to_string(a.type)} {a.name}{default}')
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
        code.append(f'{indent}{cpp_type_to_string(a.type)} {a.name};')

    code.append('')

    for func in self.methods:
        for line in Function_cpp(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'}};')

    if self.generate_json:
        code.extend(Struct_to_JSON_cpp(self))
        code.extend(Struct_to_JSON_string_cpp(self))
        code.extend(Struct_from_JSON_cpp(self))
        code.extend(Struct_from_JSON_string_cpp(self))

    return code

def Struct_to_JSON_cpp (self:Struct):
    code = []
    code.append(f'void to_json(json &j, const {self.name} &obj) {{')
    for attr in self.attributes:
        code.append(f'{indent}j["{attr.name}"] = obj.{attr.name};')
    code.append(f'}}')
    code.append('')
    return code

def Struct_from_JSON_cpp (self:Struct):
    code = []
    code.append(f'void from_json(const json &j, {self.name} &obj) {{')
    for attr in self.attributes:
        code.append(f'{indent}j.at("{attr.name}").get_to(obj.{attr.name});')
    code.append(f'}}')
    return code

def Struct_to_JSON_string_cpp (self:Struct):
    code = []
    code.append(f'std::string to_json(const {self.name} &obj) {{')
    code.append(f'{indent}json j;')
    code.append(f'{indent}to_json(j,obj);')
    code.append(f'{indent}return j.dump();')
    code.append(f'}}')
    return code

def Struct_from_JSON_string_cpp (self:Struct):
    code = []
    code.append(f'{self.name} {self.name}_from_json(const json &j) {{')
    code.append(f'{indent}{self.name} obj;')
    code.append(f'{indent}from_json(j,obj);')
    code.append(f'{indent}return obj;')
    code.append(f'}}')
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
