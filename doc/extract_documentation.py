import os, requests

def main(server,outdir):
    os.makedirs(outdir,exist_ok=True)
    functions = requests.get(f'{server}/functions').json()
    for f in functions:
        with open(f"{outdir}/{f['name']}.md",'w') as file:
            file.writelines(f['doc_md'])

if __name__ == '__main__':
    server = f'http://{os.getenv("SERVER_ADDRESS","az.hopto.org")}:{os.getenv("SERVER_PORT","8000")}'
    main(server,'functions')
