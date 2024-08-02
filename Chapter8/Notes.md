# Log Functions

- **Defining a Function**
  - Syntax:
    ```python
    def function_name(parameters):
        statement(s)
    ```
  - **Arguments and Parameters**
    - The definition is the parameter.
    - When calling a function, the values you pass are called arguments.
  - **Passing Arguments**
    - **Positional Arguments**
    - **Keyword Arguments**(You can pass arguments in any order)
      - Syntax:
        ```python
        def describe_pet(animal_type, pet_name):
            print(f"\nI have a {animal_type}.")
            print(f"My {animal_type}'s name is {pet_name.title()}.")
        describe_pet(animal_type='hamster', pet_name='harry')
        ```
        I prefer this way to readability.

    - **Default values**
      - You dont have to put the default value in the function call.
      - Put default values at the end of the parameter list.
      - Syntax:
        ```python
        def describe_pet(pet_name, animal_type='dog'):
        ```
- **Return Values**
  - Simple return values, give a value of the function to a variable when was called.
  - **Making an Argument Optional**
    - With default values.
    - Listed at the end of the parameter list.
    - Syntax:
      ```python
      def get_formatted_name(first_name, last_name, middle_name=''):
      ```
  - **Returning a Dictionary**
    - Define a variable with desired dictionary values and then return it.
- **Passing a list**
  - When you pass a list to a function, the function can modify the list, and are permanent.
  - **Preventing a Function from Modifying a List**
    - Send a copy of the list to the function.
    - But it is not efficient. It is better to use the original list. Specially when the list is large.
    - Syntax:
      ```python
      function_name(list_name[:])
      ```

- **Passing an Arbitrary Number of Arguments**
  - Syntax:
    ```python
    def function_name(*parameter_name):
    ```
  - Makes a tuple of the arguments.

  - **Mixing Positional and Arbitraty Arguments**
    - Add the arbitrary parameter at the end of the list of parameters.
  - **Using Arbitrary Keyword Args**
    - Syntax:
      ```python
      def function_name(**parameter_name):
      ```
    - Makes a dictionary of the arguments.

- **Storing Your Functions in Modules**
  - Use other files to store functions.
  - A module is a file ending in .py.
  - **Importing an Entire Module**
    - Syntax:
      ```python
      import module_name
      ```
    - Calling a function from the module: `module_name.function_name()`
      - Makes any function from the module available in your program.

  - **Importing Specific Functions**
    - Syntax:
      ```python
      from module_name import function_name, ...
      ```
    - Calling a function from the module: `function_name()`

  - **Using as to Give a Function an Alias**
    - Syntax:
      ```python
      from module_name import function_name as fn
      ```
    - Calling a function from the module: `fn()`

  - **Using as to Give a Module an Alias**
    - Syntax:
      ```python
      import module_name as mn
      ```
    - Calling a function from the module: `mn.function_name()`

  - **Importing All Functions in a Module**
    - Syntax:
      ```python
      from module_name import *
      ```
    - Calling a function from the module: `function_name()`

- **Styling Functions**
  - Functions should have descriptive names and use lowercase letters and underscores.
  - Docstring format after the function definition. To explain what the function does.
  - No spaces in default values def. Neither in keyword arguments.
  - ENTER in definition line to separate the function from parameters.
  - import statements at the beginning of the file. But after the module docstring.



