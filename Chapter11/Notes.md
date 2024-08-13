
# Log Testing your code

1. **Installing ``pytest`` with ``pip``**
  - In linux you need to intall ``pip``.
  - ``pip install pytest`` or ``pip3 install pytest``
  - **Updating pip**
    - ``pip install --upgrade pip`` or ``pip3 install --upgrade pip``

2. **Testing a Function**
  - `F` means that the test failed.
  - `.` means that the test passed. More dots means more tests passed.
  - **Unit tests and test cases**
    - Check the files with the name ``test_*.py``.
    - Same with the functions, the name of the test functions should start with ``test_``.
  - **Running a test**
    - ``pytest test_name.py``
    - ``pytest test_name.py::test_function_name``
    - ``pytest test_name.py -v`` for verbose output.
    - ``pytest test_name.py -x`` for stopping the test after the first failure.

3. **Testing a Class**
  - In the test file we have to import the class and then instantiate it.
  - We can use a loop to assert multiple values.
  - **Variety of assertions**
    - ``assert a == b``
    - ``assert a != b``
    - ``assert a is b``
    - ``assert a is not b``
    - ``assert a in b``
    - ``assert a not in b``
    - ``assert a > b``
    - ``assert a < b``
    - ``assert a >= b``
    - ``assert a <= b``
  - **Using Fixtures**
    - The fixtures is a super arrange of the test, that would be used in multiple tests.
    - We made it with the ``@pytest.fixture`` decorator.
      - Decorators run before the function they decorate.
      - We need to import the ``pytest`` module.
      - We first define the decorator function and then we use it in the test functions through the parameter.
