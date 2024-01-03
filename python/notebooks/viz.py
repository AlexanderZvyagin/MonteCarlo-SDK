from graphviz import Digraph

def tr (lorig:list, nmax:int=4):
    '''Trunctate list to lmax items and convert it into a string'''
    
    lstr = ','.join(map(str,lorig[:nmax]))
    
    if len(lorig)>nmax:
        lstr += ',...'
    
    return f'[{lstr}]'
        
def viz (model,graph_attr={'rankdir':'LR'}):
    '''
        graph_attr parameter documentation: https://graphviz.org/doc/info/attrs.html
    '''
    g = Digraph(format='svg',graph_attr=graph_attr)
    states = {} # state number => updater number
    
    for iupdater,updater in enumerate(model.updaters):
#         print()
#         print(updater)
        if updater._nstates==0:
#             print(f'WARNING: not showing {updater.name}, which has no state.')
            continue

        for n in range(updater._nstates):
            states[updater._state+n] = iupdater

        label = fr'<u> {updater.name}\n{updater.title}\nargs={tr(updater.args)}  start={tr(updater.start)}'
        if updater._nstates:
            label += '|'
            label += '|'.join([f'<s{updater._state+n}> state {updater._state+n}' for n in range(updater._nstates)])

        name  = f'<u{iupdater}>'
#         print(f'name={name}  label={label}')
        g.node(
            name  = name,
            label = label,
            shape = 'record'
        )
        
        for ref in updater.refs:
            if ref<0: continue
            g.edge(f'{name}:u',f'<u{states[ref]}>:<s{ref}>')
    return g
