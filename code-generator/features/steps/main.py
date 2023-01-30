import os, shutil
import code_generator as cg

language_extension = {'c++':'cpp', 'python':'py', 'typescript':'ts'}

@given(u'output directory "{output}"')
def step_impl (context, output):
    context.output = output
    if os.path.exists(output):
        shutil.rmtree(output)
    os.makedirs(output)

@when(u'file "{file_name}" is being generated')
def step_impl (context, file_name):
    context.file_name = file_name
    context.code_file = cg.File(file_name)

@when(u'function "{function_name}" returning "{type_name}" is created with arguments')
def step_impl (context, function_name, type_name):
    args = [row for row in context.table]
    context.code_function = context.code_file.Add(cg.FunctionDeclaration(function_name,type_name,args))

@when(u'statement "{statement}" is added to the function')
def step_impl (context, statement):
    context.code_function.Add(statement)

@when(u'"{languages}" code is generated and saved in the output directory')
def step_impl (context, languages):
    context.languages = [s.strip() for s in languages.split(',')]

    for language in context.languages:
        with open(os.path.join(
            context.output,
            context.file_name+'.'+language_extension[language]
        ),'w') as f:
            lines = context.code_file.Build(language)
            f.write('\n'.join(lines))
            # f.write(f'hello {language}!')

@then(u'We expect to find files in the output directory "{files}"')
def step_impl (context, files):
    for fname in [s.strip() for s in files.split(',')]:
        assert (os.path.exists(os.path.join(context.output,fname)))

@when(u'structure "{structure_name}" is added')
def step_impl (context, structure_name):
    context.code_structure = cg.Structure(structure_name)
