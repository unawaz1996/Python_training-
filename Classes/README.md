# Python Object Oriented Programming

## Classes 
CLasses allow us to logically group data and functions in a way that's easy to use and easy to build upon if needed.

### Methods 

Class methods and regular methods 


* A regular method is accessible through both, the class and the instance

* A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance 

    * Static method knows nothing about the class and just deals with the parameters 
    
    * Class method works with the class since its parameter is always the class itself 



### Python class inheritance 
A method that allows us to create a new class that shares the same attributes and method with the original function. 

When we input a function to a subclass, python follows the 'method resolution order', which is the chain of classes that it goes through to find what the method is. All classes have the built-in group of methods and attributes as their primary order.


isinstance() will tell us if an instance belongs to a class