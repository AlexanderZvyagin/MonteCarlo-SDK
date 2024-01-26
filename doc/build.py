#!/bin/env python3

import sys, os, requests
sys.path.append('../output/dto/python')
import dto

def write_to_file_v1(f,name):
    f.write(f'''
{name}
=====================================================

.. autoclass:: dto.{name}

.. toctree::

   functions/{name}.md
''')

def write_to_file_v2(f,name):

    autoclass = f'.. autoclass:: dto.{name}' if getattr(dto,name,None) else ''

    f.write(f'''
{name}
=====================================================

{autoclass}

.. include:: functions/{name}.md
   :parser: myst_parser.sphinx_
''')

def extract_documentation (server, outdir, index_file='functions'):
    os.makedirs(outdir,exist_ok=True)
    functions = requests.get(f'{server}/functions').json()
    for f in functions:
        with open(f"{outdir}/{f['name']}.md",'w') as file:
            file.writelines(f['doc_md'])

    with open(f'{index_file}.rst','w') as index:
        for f in functions:
            name = f['name']
            # write_to_file(index,name)
            write_to_file_v2(index,name)

if __name__ == '__main__':

    os.system('rm -rf _build functions')

    server = f'http://{os.getenv("SERVER_ADDRESS","az.hopto.org")}:{os.getenv("SERVER_PORT","8000")}'
    extract_documentation(server,'functions')

    os.system('make html')
