rm -rf output
# cgdto --schema=schema.py --output=output --languages=cpp,python,typescript --run-tests
cgdto --schema=schema.py --output=output --languages=cpp,python,typescript 
(cd doc; make html)