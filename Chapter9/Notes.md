# Log Classes

- **Creating and Using a Class**
  - **The init method**
    - It's the constructor method.
    - The underscore is a convention to prevent Python from using the method name in certain situations.
    - **self** is required in the method definition.
      - Is a reference to the instance of the class.
      - It's called automatically.
      - Goes before other parameters.
      - **Attributes are created with self.**
  - **Making an Instance from a Class**
    - Syntax:
      ```python
      instance_name = ClassName(parameters)
      ```
  - **Accessing Attributes**
    - Syntax:
      ```python
      instance_name.attribute_name
      ```
  - **Calling Methods**
    - Syntax:
      ```python
      instance_name.method_name()
      ```
  - **Creating Multiple Instances**
    - Just call the class as many times as needed.

- **Working with Classes and Instances**
  - You can modify the attributes of an instance directly.
    - Direct mod -> Syntax: `instance_name.attribute_name = new_value`
    - Method mod -> Syntax: `instance_name.method_name(new_value)`
  - Attributes can have default values.

- **Inheredit**
  - The class that inherits, and inheredit attributes and methods, also the constructor.
  - **The __init__() Method for a Child Class**
    - Syntax:
      ```python
      class ChildClassName(ParentClassName):
        def __init__(self, parameters):
          super().__init__(parameters)
      ```

    - `super()`: A function that helps Python make connections between the parent and child class.
      - It's a reference to the parent class.
      - It's called automatically.
      - Goes before other parameters.
      - **Attributes are created with super().**

    - **Defining Attr and med fot the child class**
      - Just add the new attributes and methods to the child class.
      - This is called specialization.

    - **Overriding Methods from the Parent Class**
      - Just define the method in the child class with the same name as the parent class.
      - This is called overriding.
    - **Instances as Attr**
      - Composition.
      - We can use an instance of a class as an attribute in another class.
      - Just pass the instance as a parameter in the constructor or instatiate it in the constructor.

- **Importing Classes**
  - **Importing a single class**
    - Same as importing a library with the `import`, `from` and `as` keywords.
    - You can call multiple classes from the same file.py.
    - Or import the entire module.
    - Dont use `*` to import all classes.
      - Instead use `import module_name` and call the classes with `module_name.class_name`.
    - Use aliases to avoid conflicts.

- **Python Standard Library**
  - With python installed, you have access to a lot of modules.
  - Call with `import module_name`.
  - Examples of stantar libraries:
    - `random`: Do random stuff.
    - `datetime`: Work with dates and times.
    - `json`: Work with JSON data.
    - `os`: Work with the operating system.
    - `math`: Work with math.

  - External ones are useful.
    - `matplotlib`: Create plots.
    - `requests`: Make API calls.
    - `Django`: Create web apps.
    - `Flask`: Create web apps.
    - `Pygame`: Create games.
    - `Pandas`: Work with data.
    - `Numpy`: Work with arrays.
    - `Scipy`: Work with scientific computing.
    - `Scikit-learn`: Work with machine learning.
    - `Tensorflow`: Work with machine learning.
    - `Keras`: Work with machine learning.
    - `PyTorch`: Work with machine learning.
    - `OpenCV`: Work with computer vision.
    - `BeautifulSoup`: Work with web scraping.
    - `Selenium`: Work with web scraping.
    - `PyQt`: Create GUIs.
    - `Tkinter`: Create GUIs.
    - `wxPython`: Create GUIs.
    - `PyGTK`: Create GUIs

- **Styling Classes**
  - CamelCase for class names.
  - Instance and module names should be lowercase.
    - With underscores for spaces.
  - Docstrings for classes and methods.
  - Module should have a docstring.
  - Standard libraries and external libraries go first.
    - Blank line between standard and external libraries. Also between external and own libraries.

