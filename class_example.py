class Dog:   ## Create own blueprint for what dog does
    ## Operations that can be performed by Dog 
# inside the class, can define a method 
    def __init__(self, name, age ): # This method will be called whenever we create Dog
        self.name = name   # attribute of the class Dog
        self.age = age # this attribute is stored permanently per instance  
        # invisibily, reference to this dog object is passed
        # this can be references inside different functions 
    
    def get_name(self):
        return self.name 
    
    def get_age(self): 
        return self.age 
    # self is being used so we can remember which instance is the one we're looking for 

    def set_age(self, age): 
        self.age = age 


d = Dog() # assign d an instance of class Dog 
print(type(Dog))

d.bark()