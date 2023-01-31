from collections import namedtuple

indent = ' '*4

Variable = namedtuple('Variable',['name','type','defval'])

ext = {
    'cpp' : 'cpp',
    'python' : 'py',
    'typescript' : 'ts'
}

typescript_types = {
    ''       : '',
    'string' : 'string',
    'int'    : 'number',
    'int[]'  : 'number[]',
    'float'  : 'number',
    'float[]': 'number[]',
}

cpp_types = {
    ''       : '',
    'void'   : 'void',
    'string' : 'std::string',
    'int'    : 'int',
    'int[]'  : 'std::vector<int>',
    'float'  : 'float',
    'float[]': 'std::vector<float>',
}

python_types = {
    'string' : 'str',
    'int'    : 'int',
    'int[]'  : 'list[int]',
    'float'  : 'float',
    'float[]': 'list[float]',
}

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
    def __init__ (self, name:str, type:str, args=[]):
        self.name = name
        self.type = type
        self.args = args
    def __repr__ (self):
        return f"Function('{self.name}','{self.type}',{self.args})"

def Function_python(self:Function, obj:Struct=None):
    fname = self.name
    ctor = False
    derived = False
    if obj:
        derived = obj.base is not None
        if self.name==obj.name:
            fname = '__init__'
            ctor = True
            assert len(self.args)==0

    attributes = []
    if ctor:
        attributes = obj.GetAllAttributes()
    else:
        attributes = self.args

    code = []
    code.append(f'def {fname}(')

    args_code = [f'{indent}self']
    for a in attributes:
        args_code.append(f'{indent}{a.name} : {python_types[a.type]}')
    for i in range(len(args_code)-1):
        args_code[i] += ','
    code.extend(args_code)

    code.append('):')
    if ctor:
        if derived:
            super_args = []
            code_init = []
            for a in obj.GetAllAttributes():
                if a.name in [v.name for v in obj.base.GetAllAttributes()]:
                    super_args.append(a.name)
                else:
                    code_init.append(f'{indent}self.{a.name} = {a.name}')
            code.append(f'{indent}super().__init({",".join(super_args)})')
            code.extend(code_init)
        else:
            for a in obj.attributes:
                code.append(f'{indent}self.{a.name} = {a.name}')
    else:
        print('no code')

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


def Function_cpp(self:Function, obj:Struct=None):
    ftype = cpp_types[self.type]+' '
    ctor = False
    derived = False
    if obj:
        derived = obj.base is not None
        if self.name==obj.name:
            ftype = '' # constructor
            ctor = True
            assert len(self.args)==0

    code = []
    code.append(f'{ftype}{self.name}(')

    attributes = []
    if ctor:
        attributes = obj.GetAllAttributes()
    else:
        attributes = self.args

    args_code = []
    for a in attributes:
        args_code.append(f'{indent}{cpp_types[a.type]} {a.name}')
    for i in range(len(args_code)-1):
        args_code[i] += ','
    code.extend(args_code)

    if derived:
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
        print('no code')
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
        code.append(f'{indent}{cpp_types[a.type]} {a.name};')

    code.append('')

    for func in self.methods:
        for line in Function_cpp(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'}};')
    return code

def Function_typescript (self:Function, obj:Struct=None):
    fname = self.name
    ctor = False
    derived = False
    if obj:
        derived = obj.base is not None
        if self.name==obj.name:
            fname = 'constructor'
            ctor = True
            assert len(self.args)==0

    code = []
    code.append(f'{fname}(')


    attributes = []
    if ctor:
        attributes = obj.GetAllAttributes()
    else:
        attributes = self.args

    args_code = []
    for a in attributes:
        args_code.append(f'{indent}{a.name} : {typescript_types[a.type]}')
    for i in range(len(args_code)-1):
        args_code[i] += ','
    code.extend(args_code)

    code.append('){')

    if derived:
        code.append(f'{indent}super (')
        args_code = []
        for a in obj.base.GetAllAttributes():
            args_code.append(f'{indent*2}{a.name}')
        for i in range(len(args_code)-1):
            args_code[i] += ','
        code.extend(args_code)
        code.append(f'{indent})')

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
        code.append(f'{indent}{a.name} : {typescript_types[a.type]};')

    code.append('')

    for func in self.methods:
        for line in Function_typescript(func,self):
            code.append(f'{indent}{line}')
        code.append('')

    code.append(f'}}')
    code.append('')
    return code

autogen_text = 'This is an automatically generated file.'

def File_prefix_cpp (objs):
    return [
        f'// {autogen_text}',
        '',
        '#include <string>',
        '#include <vector>',
        ''
    ]

def File_prefix_python (objs):
    return [
        f'# {autogen_text}',
        ''
    ]

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

def write_objs(fname:str,language,objs=[]):
    '''fname: full path name without extension, the file will be overwritten. the directory path must exist.'''
    with open(fname+'.'+ext[language],'w') as file:
        file_prefix_code = globals().get(f'File_prefix_{language}')
        if file_prefix_code:
            for line in file_prefix_code(objs):
                file.write(line+'\n')
        for obj in objs:
            if isinstance(obj,Struct):
                name = f'Struct_{language}'
                func = globals().get(name)
                if not func:
                    print(f'Not found: "{name}"')
                    continue

                for line in func(obj):
                    file.write(line+'\n')
            else:
                print(f'Cannot handle {type(obj)}')

        file_suffix_code = globals().get(f'File_suffix_{language}')
        if file_suffix_code:
            for line in file_suffix_code(objs):
                file.write(line+'\n')
