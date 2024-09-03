#1. Create a program to create two class
#1.1. Create a constructor and a method for each class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

 #1.2. Create a __init__.py for adding all packages.

# __init__.py

# Import all modules from the current package
from .module1 import *
from .module2 import *
from .module3 import *

# Optionally, you can define an __all__ list to control what is imported with a wildcard import
__all__ = [
    'module1',
    'module2',
    'module3',
    # Add other modules or packages that should be accessible
]

#1.3. Import the respective packages.

# my_package/__init__.py

# Importing modules from the current package
from .module1 import *
from .module2 import *

# Importing sub-packages
from .sub_package1 import *
from .sub_package2 import *

# Optionally, define the public API of the package
__all__ = [
    'module1',
    'module2',
    'sub_package1',
    'sub_package2',
    # Add other modules or classes that you want to expose
]

#1.4. Call each class by creating an object to it 

# Example usage script

# Import the classes from the package
from my_package import MyClass1, MyClass2, SubModuleClass1, SubModuleClass2

# Create instances of the classes
obj1 = MyClass1()
obj2 = MyClass2()
obj3 = SubModuleClass1()
obj4 = SubModuleClass2()

# Call methods on the instances
obj1.do_something()
obj2.do_something()
obj3.do_something()
obj4.do_something()

#1.5. Create a program by all the above.

# example_script.py

# Import the classes from the package
from my_package import MyClass1, MyClass2, SubModuleClass1, SubModuleClass2

def main():
    # Create instances of the classes
    obj1 = MyClass1()
    obj2 = MyClass2()
    obj3 = SubModuleClass1()
    obj4 = SubModuleClass2()

    # Call methods on the instances
    obj1.do_something()
    obj2.do_something()
    obj3.do_something()
    obj4.do_something()

if __name__ == "__main__":
    main()


