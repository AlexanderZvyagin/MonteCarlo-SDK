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

    code.extend(Struct_compare_cpp(self))

    code.append(f'}};')

    if self.generate_json:
        code.extend(Struct_to_JSON_cpp(self))
        code.extend(Struct_to_JSON_string_cpp(self))
        code.extend(Struct_from_JSON_cpp(self))
        code.extend(Struct_from_JSON_string_cpp(self))

    return code

def Struct_compare_cpp(self:Struct):
    code = []
    code.append(f'{indent}bool operator == (const {self.name} &other) const {{')
    if self.base:
        code.append(f'{indent*2}if ({self.base.name}::operator != (other)) return false;')
    for a in self.attributes:
        code.append(f'{indent*2}if ({a.name} != other.{a.name}) return false;')
    code.append(f'{indent*2}return true;')
    code.append(f'{indent}}}')
    code.append(f'{indent}bool operator != (const {self.name} &other) const {{return not(*this==other);}}')
    return code

def Struct_to_JSON_cpp (self:Struct):
    code = []
    code.append(f'void to_json(json &j, const {self.name} &obj) {{')
    if self.base:
        code.append(f'{indent}to_json(j,static_cast<const {self.base.name} &>(obj));')
    for attr in self.attributes:
        code.append(f'{indent}j["{attr.name}"] = obj.{attr.name};')
    code.append(f'}}')
    code.append('')
    return code

def Struct_from_JSON_cpp (self:Struct):
    code = []
    code.append(f'void from_json(const json &j, {self.name} &obj) {{')
    if self.base:
        code.append(f'{indent}from_json(j,static_cast<{self.base.name} &>(obj));')
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

# def cpp_run_test(fname):
#     incdir = '-I /home/zvyagin/Projects/MonteCarlo/MonteCarlo-to-gitlab/external/json/include'
#     cmd = f'g++ {incdir} {fname} -o {fname}.exe && {fname}.exe'
#     asyncio.run(run(cmd))

def Tests_cpp (objs):

    struct_names = []
    code_construct_random = []
    code_create = []
    code_convert = []
    code_compare = []

    for obj in objs:
        if type(obj)!=Struct:
            continue

        # print(obj.name,obj.generate_json)
        # if not obj.generate_json:
        #     continue

        struct_names.append(obj.name)

        random_args = ''

        ctors = [method for method in obj.methods if method.name == obj.name]
        assert len(ctors)==1

        for i,arg in enumerate(ctors[0].args):
            is_list, type_name = decode_type(arg.type)
            if is_list:
                if type_name=='string':
                    random_arg = 'random_list_of_strings()'
                elif type_name=='float':
                    random_arg = 'random_list_of_floats()'
                elif type_name=='int':
                    random_arg = 'random_list_of_ints()'
                elif type_name in struct_names:
                    random_arg = f'random_list_of_{type_name}()'
                else:
                    raise Exception(f'Unknown type {type_name}')
            elif type_name=='string':
                random_arg = 'random_string()'
            elif type_name=='float':
                random_arg = 'random_float()'
            elif type_name=='int':
                random_arg = 'random_int()'
            elif type_name in struct_names:
                random_arg = f'random_{type_name}()'
            else:
                raise Exception(f'Unknown type {type_name}')
            ending = '' if (i+1)==len(ctors[0].args) else ','
            random_args += f'{indent*4}{random_arg}{ending}\n'

        code_construct_random.extend(f'''
{obj.name} random_{obj.name} (void) {{
    return {obj.name} (
{random_args}
    );
}}
'''.split('\n'))

        code_construct_random.extend(f'''
std::vector<{obj.name}> random_list_of_{obj.name} (int min = 0, int max = 3) {{
    std::uniform_int_distribution<int> uniform_dist(min,max);
    auto size = uniform_dist (generator);
    std::vector<{obj.name}> list;
    for(int i=0; i<size; i++)
        list.push_back(random_{obj.name}());
    return list;
}}
'''.split('\n'))

        code_create.append(f'''
        }} else if (struct_name == "{obj.name}") {{
            f << to_json(random_{obj.name}());
''')

        code_convert.extend(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            std::ofstream out (file2_path);
            out << to_json(obj);
            if(!out)
                throw std::runtime_error("Operation 'convert': IO error on " + struct_name);
'''.split('\n'))
        code_compare.extend(f'''
        }} else if (struct_name == "{obj.name}") {{
            auto obj1 =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file1_path
            )));
            auto obj2 =
                {obj.name}_from_json (
                    json::parse (
                        std::ifstream (
                            file2_path
            )));
            if(obj1!=obj2)
                throw std::runtime_error("Operation 'compare' failed for struct " + struct_name);
'''.split('\n'))

    code = []
    for line in cpp_test_template.split('\n'):
        if line=='//create-struct-random//':
            code.extend(code_construct_random)
        elif line=='//create-struct-tests//':
            code.extend(code_create)
        elif line=='//convert-struct-tests//':
            code.extend(code_convert)
        elif line=='//compare-struct-tests//':
            code.extend(code_compare)
        else:
            code.append(line)
    return code

cpp_test_template = '''
#include <random>
#include <limits>
#include <filesystem>
#include <iostream>
#include <fstream>
#include <stdexcept>

#include "dto.cpp"

namespace fs = std::filesystem;

std::random_device rd;
std::mt19937 generator(rd());

int random_int (int min = -1000, int max = 1000) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    return uniform_dist (generator);
}

std::vector<int> random_list_of_ints (int min = 0, int max = 3) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    auto size = uniform_dist (generator);
    std::vector<int> list;
    for(int i=0; i<size; i++)
        list.push_back(random_int());
    return list;
}

float random_float (
    float min            = -1e6,
    float max            =  1e6,
    bool can_be_nan      = false,
    bool can_be_infinity = false
) {
    std::uniform_int_distribution<int> yes_no(0,1);

    if(can_be_nan and yes_no(generator))
        return NAN;

    if(can_be_infinity and yes_no(generator))
        return (yes_no(generator) ? -1 : 1) * std::numeric_limits<float>::infinity();

    std::uniform_real_distribution uniform_dist(min,max);
    return uniform_dist (generator);
}

std::vector<float> random_list_of_floats (int min = 0, int max = 3) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    auto size = uniform_dist (generator);
    std::vector<float> list;
    for(int i=0; i<size; i++)
        list.push_back(random_float());
    return list;
}

// https://stackoverflow.com/questions/47977829/generate-a-random-string-in-c11
std::string random_string (int len=16) {
    static std::string str("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
    std::shuffle(str.begin(), str.end(), generator);
    return str.substr(0, len);
}

std::vector<std::string> random_list_of_strings (int min = 0, int max = 3) {
    std::uniform_int_distribution<int> uniform_dist(min,max);
    auto size = uniform_dist (generator);
    std::vector<std::string> list;
    for(int i=0; i<size; i++)
        list.push_back(random_string());
    return list;
}

//create-struct-random//

int main (int argc, const char **argv) try {

    const std::string
        command         = argc>1 ? argv[1] : "",
        struct_name     = argc>2 ? argv[2] : "",
        file1_path      = argc>3 ? argv[3] : "",
        file2_path      = argc>4 ? argv[4] : "";

    if (command == "create") {

        if(!file2_path.empty())
            throw std::runtime_error("Command 'create' expects empty file2 name, got:'" + file2_path + '"');

        std::ofstream f (file1_path);

        if (false) {
//create-struct-tests//
        } else {
            throw std::runtime_error("Not supported operation 'create' on struct " + struct_name);
        }
        if(!f)
            throw std::runtime_error("Operation 'create': IO error");

    } else if (command == "convert") {

        if (false) {
//convert-struct-tests//
        } else {
            throw std::runtime_error("Not supported operation 'convert' on struct " + struct_name);
        }

    } else if (command == "compare") {

        if (false) {
//compare-struct-tests//
        } else {
            throw std::runtime_error("Not supported operation 'compare' on struct " + struct_name);
        }

    } else {
        throw std::runtime_error("Not supported command " + command);
    }

    return 0;

} catch (const std::exception &e) {
    std::cerr << "Exception:" << std::endl << e.what() << std::endl;
    return 1;
}

catch (...) {
    std::cerr << "Unknown exception:" << std::endl;
    return 1;
}
'''