#1. Write two methods with the same name but different number of parameters of same type and call the methods 

# module2.py

class MyClass2:
    def __init__(self):
        print("MyClass2 instance created")

    def do_something(self, *args):
        if len(args) == 2:
            print(f"Doing something with two parameters: {args[0]} and {args[1]}")
        elif len(args) == 1:
            print(f"Doing something with one parameter: {args[0]}")
        else:
            print("Doing something with no parameters")

#2. Write two methods with the same name but different number of parameters of different data type and call the methods 

# example_script.py

from my_package import MyClass1, MyClass2

def main():
    # Create instances of the classes
    obj1 = MyClass1()
    obj2 = MyClass2()

    # Call methods with different numbers and types of parameters
    print("Calling MyClass1.do_something:")
    obj1.do_something()                          # No parameters
    obj1.do_something(42)                       # Integer parameter
    obj1.do_something("Hello", 10)              # String and integer parameters

    print("\nCalling MyClass2.do_something:")
    obj2.do_something()                          # No parameters
    obj2.do_something(3.14)                      # Float parameter
    obj2.do_something("Hello", 2.718)           # String and float parameters

if __name__ == "__main__":
    main()

#3. Write two methods with the same name and same number of parameters of same type

# example_script.py

from my_package.module1 import MyClass1

def main():
    # Create an instance of MyClass1
    obj = MyClass1()

    # Call the method with different types of parameters
    print("Calling MyClass1.do_something with integer:")
    obj.do_something(42)  # Pass an integer

    print("\nCalling MyClass1.do_something with string:")
    obj.do_something("Hello")  # Pass a string

if __name__ == "__main__":
    main()
