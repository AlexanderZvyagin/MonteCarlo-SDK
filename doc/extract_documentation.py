import os, requests, sys
sys.path.append(os.getcwd()+f'/../output/dto/python')
import dto

def main(server,outdir,index_file='f'):
    os.makedirs(outdir,exist_ok=True)
    functions = requests.get(f'{server}/functions').json()
    for f in functions:
        with open(f"{outdir}/{f['name']}.md",'w') as file:
            file.writelines(f['doc_md'])

    with open(f'{index_file}.rst','w') as index:
        for f in functions:
            name = f['name']

            autodoc = ''
            if hasattr(dto,name):
                autodoc = f'.. autoclass:: dto.{name}'
            
            index.write(f'''
{name}
=====================================================

{autodoc}

.. toctree::

.. include:: functions/{name}.md
   :parser: myst_parser.sphinx_

''')

if __name__ == '__main__':
    server = f'http://{os.getenv("SERVER_ADDRESS","az.hopto.org")}:{os.getenv("SERVER_PORT","8000")}'
    main(server,'functions')
