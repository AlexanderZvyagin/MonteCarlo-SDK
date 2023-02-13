import os, subprocess

import json

# This is python specific
from output.dto import *

# This is c++ specific


def run_python_create(struct_name, json_file_name1, json_file_name2):
    assert json_file_name2 is None
    struct = globals()[struct_name]
    obj = struct()
    to_JSON = globals()[f'{struct_name}_to_JSON']
    obj_json = to_JSON(obj)
    with open(json_file_name1,'w') as f:
        f.write(obj_json)

def run_python_convert(struct_name,json_file_name1, json_file_name2):
    assert json_file_name1 is not None
    assert json_file_name2 is not None
    with open(json_file_name1) as f:
        obj_input_json = json.loads(f.read())
    from_JSON = globals()[f'{struct_name}_from_JSON']
    obj = from_JSON(obj_input_json)
    to_JSON = globals()[f'{struct_name}_to_JSON']
    obj_output_json = to_JSON(obj)
    with open(json_file_name2,'w') as f:
        f.write(obj_output_json)

def run_python_compare(struct_name,json_file_name1, json_file_name2):
    assert json_file_name1 is not None
    assert json_file_name2 is not None

def old_run(language,command,struct_name,file1,file2=None):
    func = globals().get(f'run_{language}_{command}')
    func(struct_name,file1,file2)

def run(language,command,struct_name='',file1='',file2=''):
    cmd = [
        './run',
        command,
        struct_name,
        os.path.abspath(file1) if file1 else '',
        os.path.abspath(file2) if file2 else ''
    ]
    proc = subprocess.run (cmd, capture_output=True, text=True, cwd=f'languages/{language}')
    print('')
    print('>>>',cmd)
    print(f'ExitCode={proc.returncode} StdOutLen={len(proc.stdout)} StdErrLen={len(proc.stderr)}')
    for v in ['stdout','stderr']:
        if not getattr(proc,v):
            continue
        print(f'*** {v} ***')
        print(getattr(proc,v))
    proc.check_returncode()

if __name__ == '__main__':
    lang1 = 'cpp'
    lang2 = 'cpp'

    for lang in ['python','typescript','cpp']:
        run(lang,'build')

    struct_name = 'UpdaterDoc'
    json_file1 = f'output/{struct_name}-{lang1}-create.json'
    run(lang1,'create',struct_name,json_file1)
    json_file2 = f'output/{struct_name}-{lang2}-convert.json'
    run(lang2,'convert',struct_name,json_file1,json_file2) 
    run(lang1,'compare',struct_name,json_file1,json_file2)
