# Log

- **Conditional tests**
  - ``True`` or ``False``
  - Operators:
    - `==` - Equal to
    - `!=` - Not equal to
    - `>` - Greater than
    - `<` - Less than
    - `>=` - Greater than or equal to
    - `<=` - Less than or equal to
    - `and` - Both conditions must be true
    - `or` - Either condition must be true
    - `in` - Check if a value is in a **list**
    - `not in` - Check if a value is not in a **list**
    - `is` - Check if two values are the same
    - `is not` - Check if two values are not the same
    - `not` - Negate a condition
  - Sensitive to case
  - Sensitive to whitespace
  - `()` to emphasize order of operations or combine multiple conditions
- **`if` statement**
  - Executes code if a condition is true
  -
  - Syntax:
    ```python
    if condition:
        # Code to execute
    ```
  - **`else` statement**
    - Specifies code to execute if the condition is false
    - Can be omitted
    - Syntax:
      ```python
      if condition:
          # Code to execute if condition is true
      else:
          # Code to execute if condition is false
      ```
  - **`elif` statement**
    - Specifies additional conditions to test
    - Use instead of else to closed multiple conditions
    - Can use any number of `elif` statements
    - Syntax:
      ```python
      if condition:
          # Code to execute if condition is true
      elif condition:
          # Code to execute if the first condition is false and this condition is true
      else:
          # Code to execute if all conditions are false
      ```
  - **Testing multiple conditions**
- **Using if Statements with Lists**
  - **Checking for special Items**
  - **Checking That a List Is Not Empty**
    - Syntax: `if list_name:`
  - **Using Multiple Lists**
    - We can check if one item in a list is in another list
    - Syntax: `if list_name1 in list_name2:`
- **Style your If Statements**
  - writing with space within the if statement
