# Log Files and Exceptions

- **Python** have method chaining, which means that you can call multiple methods on the same object in a single line of code.
- **Python** always interpret text files into **strings**.
- **Python** dont have a limit to how much data you can read and write files.

- **Refactoring**
  - Restructuring code without changing its behavior.


1. **Reading from a File**
  - **Reading the contents of a file**
    - Use `pathlib` module to read the path of the file or dir in any OS.
      - `Path()`: Create a Path object.
        - Use `read_text()` method to read the contents of the file.
          - encoding='utf-8': Specify the encoding of the file.
        - use only forward slash in any OS.
        - You can use `exist()` method to check if the file exists.
    - `rstrip()` method removes the newline character from the end of the string.

  - **Relative and absolute file paths**
    - **Relative path**: Look for the path where the current program is running.
    - **Absolute path**: Look for the path from the root directory.

  - **Accessing a file lines**
    - then of `read_text()` method, use `splitlines()` method to get the lines of the file.

  - **Working with file contents**
    - `split()` method splits a string into a list of strings, by default it splits on whitespace. But you can specify the separator.

  - **Large Files: One Million Digits**

  - **Is Your Birthday Contained in Pi?**

2. **Writing to a file**
  - `write_text(text)`: Write text to a file using `Path()` object.
    - This creates a new file or overwrites the existing file.
    - Makes sure the file is closed.
  - To write multiple lines use newline character `\n` and then `write_text()` method.

3. **Exceptions**
  - **Python** pull off an exception object when an error occurs.
  - **try-except block**: Handle exceptions.
    - `try` block: Contains the code that might cause an exception.
    - `except <exception obj name>` block: Contains the code that will run if an exception occurs.
    - `else` block: Contains the code that will run if no exception occurs.
    - `finally` block: Contains the code that will run regardless of whether an exception occurs.
  - **Failing Silently**
    - Use `pass` statement to fail silently in the `except` block.

4. **Storing Data**
  - `json` module: Store data in a file.json.
  - **JSON**: JavaScript Object Notation
    - **json.dump()**: Write data to a file.
    - **json.load()**: Read data from a file.
    - **json.loads()**: Read data from a string.
    - **json.dumps()**: Write data to a string.
  - **Storing Data with json.dump()**
    - `json.dump(data, file_object)`: Write data to a file.
  - **Reading Data with json.load()**
    - `json.load(file_object)`: Read data from a file.



