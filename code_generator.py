indent = '    ' # FIXME make it configurable? Is it language-dependent?

type_cpp = {
    None:'void',
    str:'std::string',
    int:'int',
    float:'float'
}

class Generator:
    def Build (self,language:str):
        raise Exception('Not implemented')

class Statement (Generator):
    pass

class JsonCreate (Generator):
    def __init__ (self,name:str):
        self.name = name
    def Build (self,language:str):
        if language=='c++':
            return [f'json {self.name};']
        elif language=='python':
            return [f'{self.name} = {{}}']
        elif language=='javascript':
            return [f'{self.name} = {{}};']
        else:
            raise NotImplementedError(language)

class JsonSetKeyValue (Generator):
    def __init__ (self,name_json:str,name_key:str,name_var:str):
        self.name_json = name_json
        self.name_key = name_key
        self.name_var = name_var
    def Build (self,language:str):
        if language=='c++':
            return [f'{self.name_json} ["{self.name_key}"] = {self.name_var};']
        elif language=='python':
            return [f'{self.name_json} ["{self.name_key}"] = {self.name_var}']
        elif language=='javascript':
            return [f'{self.name_json}.{self.name_key} = {self.name_var};']
        else:
            raise NotImplementedError(language)

class FunctionDeclaration (Generator):
    def __init__ (self,name:str,return_type:type):
        self.name = name
        self.return_type = return_type
        self.statements = []

    def Add (self,statement):
        self.statements.append(statement)

    def Build (self,language:str):
        '''Return list of strings'''
        code = []
        if language=='c++':
            code.append('{} {} (void) {{'.format(type_cpp[self.return_type],self.name))
            for statement in self.statements:
                for line in statement.Build(language):
                        code.append(f'{indent}{line}')
            code.append('}')
        elif language=='python':
            code.append('def {} ():'.format(self.name))
            if self.statements:
                for statement in self.statements:
                    for line in statement.Build(language):
                        code.append(f'{indent}{line}')
            else:
                code.append(f'{indent}pass')
        elif language=='javascript':
            code.append('function {} () {{'.format(self.name))
            for statement in self.statements:
                for line in statement.Build(language):
                        code.append(f'{indent}{line}')
            code.append('}')
        else:
            raise NotImplementedError(language)
        return code

class FunctionCall (Generator):
    def __init__ (self,name:str,return_variable:str,args:[str]):
        self.name = name
        self.return_variable = return_variable
        self.args = args

    def Build (self,language:str):
        '''Return list of strings'''
        if language=='c++' or language=='javascript':
            line = ''
            if self.return_variable:
                line = f'{self.return_variable} = '
            line += f'{self.name} ();'
        elif language=='python':
            line = ''
            if self.return_variable:
                line = f'{self.return_variable} = '
            line += f'{self.name} ()'
        else:
            raise NotImplementedError(language)
        return [line]

class File (Generator):
    '''  File is basically a list of functions.

        File has a name (we always think that a file has name, length, type concepts).
        
        File has no 'directory' concept (KISS).
        Because File is language independent, it has no 'extension' concept as well.
    '''

    def __init__ (self,name:str):
        self.name = name
        self.blocks = [] # list of functions, and maybe something else

    def Add (self,block):
        self.blocks.append(block)
        return block

    def Build (self,language:str):
        lines = []
        if language=='c++':
            lines.append('#include <nlohmann/json.hpp>')
            lines.append('using json = nlohmann::json;')
            lines.append('')
        for block in self.blocks:
            lines.extend(block.Build(language))
        return lines

def main():
    cg = File('test')
    print(cg.Build('c++'))
    # For the moment:
    # - all in one file
#    f1 = cg.AddFunction()

if __name__=='__main__':
    main()

def lprint(lst:[str]):
    for line in lst:
        print(line)

def show (obj,languages=['c++','python','javascript']):
    for language in languages:
        s = f'*** {language} ***'
        print('*'*len(s))
        print(s)
        print('*'*len(s))
        print()
        lprint(obj.Build(language))
        print()


def test_empty_file():
    file_name = 'test'
    f = File(file_name)
    assert f.name == file_name
    # for language in ['c++','python']:
    #     assert f.Build(language) == []

def test_function():

    f = File('file')
    ftest = f.Add(FunctionDeclaration('ftest1',None))
    ftest.Add(JsonCreate('js1'))
    ftest.Add(JsonSetKeyValue('js1','key','value'))

    ftest = f.Add(FunctionDeclaration('ftest2',None))
    ftest.Add(FunctionCall('ftest1','rv',()))

    show(f)


# class Argument:
#     def __init__ (self,name:str,type:type,defval:None):
#         self.name = name
#         self.type = type
#         self.defval = defval

class Variable (Generator):
    def __init__ (self,name:str,type:type,defvalue:str=None):
        self.name = name
        self.type = type
    def Build (self,language:str):
        if language=='c++':
            return [f'{type_cpp[self.type]} {self.name};']
        elif language=='python':
            return [f'{self.name} = {{}}']
        elif language=='javascript':
            return [f'{self.name} = {{}};']
        else:
            raise NotImplementedError(language)


class Structure (Generator):
    def __init__ (self,name:str):
        self.name = name
        self.members = []
    # def AddVariable (self,name:str,type:None):
    #     self.members.append()
    # def AddMethod (self,name:str,args:[Argument]=[]):
    #     pass
    def Build (self,language:str):
        code = []
        if language=='c++':
            code.append(f'struct {self.name} {{')
            for member in self.members:
                for line in member.Build(language):
                    code.append(f'{indent}{line}')
            code.append('};')
        elif language=='python':
            pass
        elif language=='javascript':
            pass
        else:
            raise NotImplementedError(language)
        return code


'''
class Model:
    def __init__ (self):
        self.TimeStart = 0
        self.TimeSteps = 1
        self.NumPaths = 1
        self.updaters = []
        self.evaluations = []
        self.RandomSeed = -1 # generate random seed
        self.RunTimeoutSeconds = 1
        self.MemoryLimitKB = 64
        self._titles = {}
    def AddEvaluationRequest(self,time:float):
        self.evaluations.append(EvaluationPoint(0,time))
    def Add (self, updater: Updater):
        self.updaters.append(updater)
        title = getattr(updater,'_title',None)
        updater._eq = self.NumStatefulProcesses()-1
        self._titles[updater._eq] = title
    def NumStatefulProcesses (self):
        return len([x for x in self.updaters if hasattr(x,'start')])
    def json (self):
        return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})
'''

def test_create_model ():
    Model = Structure ('Model')
    Model.members.append(Variable('TimeStart',int,0))
    # Model.AddVariable ('TimeSteps',int,1)
    # Model.AddVariable ('NumPaths',int,1)
    show(Model)
