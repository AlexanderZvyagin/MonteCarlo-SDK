Feature: Code generation

  Scenario: Files creation
      When  file "file" is being generated
      When  function "f1" returning "void" is created with arguments
        | name | type  | default |
        | arg1 | int   |         |
        | arg2 | str   | defVal  |
        | arg3 | float | -1.23   |
     Given  output directory "output/1"
      When  "c++, python" code is generated and saved in the output directory
      Then  We expect to find files in the output directory "file.cpp, file.py"

  Scenario: Create a simple add(x,y) function
      When  file "file" is being generated
      When  function "add" returning "float" is created with arguments
        | name | type  | default |
        | x    | float |         |
        | y    | float |         |
      When  statement "return x+y" is added to the function
     Given  output directory "output/2"
      When  "c++, python" code is generated and saved in the output directory
      Then  We expect to find files in the output directory "file.cpp, file.py"

  Scenario: Check function calls
      When  file "file" is being generated

      When  function "add" returning "float" is created with arguments
        | name | type  | default |
        | x    | float |         |
        | y    | float |         |
      When  statement "return x+y" is added to the function

      When  function "inc" returning "float" is created with arguments
        | name | type  | default |
        | x    | float |         |
      When  statement "return x+1" is added to the function

      When  function "neg" returning "float" is created with arguments
        | name | type  | default |
        | x    | float |         |
      When  statement "return -x" is added to the function

      When  function "main" returning "int" is created with arguments
        | name | type  | default |
      When  statement "inc(1)" is added to the function
      When  statement "neg(1)" is added to the function
      When  statement "return add(inc(2),neg(2))" is added to the function

     Given  output directory "output/3"
      When  "c++, python" code is generated and saved in the output directory
      Then  We expect to find files in the output directory "file.cpp, file.py"

  Scenario: Create structure
      When  file "file" is being generated

      When  structure "Updater" is added
        | name | type  | default |
        | x    | float |         |
        | y    | float |         |

     Given  output directory "output/4"
      When  "c++, python" code is generated and saved in the output directory
      Then  We expect to find files in the output directory "file.cpp, file.py"
