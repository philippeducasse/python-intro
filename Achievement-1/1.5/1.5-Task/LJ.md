Reflection Questions

1.	In your own words, what is object-oriented programming? What are the benefits of OOP?

OOP is a specific programming paradigm in which all elements are treated as objects. Objects need to be created through an initiator; and objects are structred in hierarchies. This allows for inheritance, or passing down predifined variables, so it avoids code repetition; and polymorphism.

2.	What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.

An object in python is a variable with a specific set of key-value pairs. A class is an object constructor, or the methods to create an object. 

For example, this is a class constructor:

class Cat(object):
def __init__(self, name):
        self.name = name

and this is the object:

cat = Cat('Smokey')

3.	In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine. 

Method	Description

Method description is when you define your own getter and setter methods within a class constructor. These methods can be called outside of the object constructor to modify or retrieve information about the object; but can only be used on an object which contains that method.

Inheritance	

Inheritance is the process by which objects can be placed in a hierarchical order. Parent classes thus pass down methods or variables, and the child class thus inherits them. Child classes can not pass down methods or variables, the process is bottom down only.

Polymorphism

Polymorphism is where a specific method or data attribute has different outcomes or values depending on where it is called or defined. So for example, the method .speak() might be inherited through various objects, but the output will be different as the arguments passed in will change from object to object.

Operator Overloading

Operator overloading allows the use of special operators such as + or - with class objects. However, to use operator overloading, these operations must be predifined in the class; for example __add__().