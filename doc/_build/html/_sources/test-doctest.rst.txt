++++++++++++++++++++
Test of doctest
++++++++++++++++++++

.. testsetup:: *

   import dto as sdk
   server = 'az.hopto.org:8000'

SDK of MC.

.. testcode::

   import requests, pprint, json
   build_json = requests.get(f'http://{server}/build').json()
   build = json.loads(build_json)
   print(json.dumps(build))
   # pprint.pprint(requests.get(f'http://{server}/build').json())
   # pprint.pprint(requests.get(f'http://{server}/build').json())
    
.. testoutput::
   :skipif: False

   {"build": "master-build895-3b97207", "date": "Jan 13 2024", "time": "10:16:04"}
 

.. doctest::

    >>> model = sdk.Model()
    >>> 1
    1

Doctest example:

.. doctest::

   >>> 2+3
   5

Test-Output example:

.. testcode::

   print(2+4)

This would output:

.. testoutput::

   6
