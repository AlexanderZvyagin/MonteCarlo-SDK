import pytest
from testbook import testbook

import os

notebooks_directory = '../notebooks'

# @testbook (f'{notebooks_directory}/t00_endpoints.ipynb', execute=True)
# def test (tb):
#     pass

# @testbook (f'{notebooks_directory}/t01_BrownianMotion.ipynb', execute=True)
# def test (tb):
#     results = tb.ref('results')

# @testbook (f'{notebooks_directory}/t02_graph.ipynb', execute=True)
# def test (tb):
#     pass

# @testbook (f'{notebooks_directory}/t03_FinanceOption.ipynb', execute=True)
# def test (tb):
#     pass

# @testbook (f'{notebooks_directory}/t05_Histograms.ipynb', execute=True)
# def test (tb):
#     pass

# @testbook (f'{notebooks_directory}/t08_Swap.ipynb', execute=True)
# def test (tb):
#     pass


def test_all_notebooks (directory = notebooks_directory):
    for fname in os.listdir(directory):
        if fname.endswith('.ipynb'):
            full_path = os.path.join(directory,fname)
            print(f'Testing: {full_path}')
            try:
                with testbook(full_path, execute=True) as tb:
                    pass
            except:
                raise
