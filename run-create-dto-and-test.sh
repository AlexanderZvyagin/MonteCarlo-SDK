rm -rf output
#cgdto --schema=schema.py --output=output --languages=cpp,python,typescript
cgdto --schema=schema.py --output=output --languages=cpp,python,typescript --run-tests
(cd doc; make html)
