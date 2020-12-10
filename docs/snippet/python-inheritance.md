title: "Python class inheritance"
tags: development, snippet, inheritance, python
author: Colm Britton
--------------------

An example of class inheritance in python.

    class Animal:
        def __init__(self, name, type="Animal"):
            self.type = type
            self.name = name
        
        def print_info(self):
            print(f"My name is {self.name}, I'm an {self.type}")

    class Dog(Animal):
        # child class can be instaniated with more args
        def __init__(self, name, type="Dog"):
            super().__init__(name, type)

        def say_hello(self):
            print("Hello")
            # call method from parent class
            self.print_info()
