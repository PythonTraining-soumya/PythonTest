# classes are user defined prototype or blue print
# a class can have methods, instance variables, class variables, constructors etc
# if you want to create a class use the keyword class
# when we write methods without classes it is called as functions
# functions inside a class is called as methods
# constructors are methods which are automatically called once the object of the class is created
# to declare constructor use def __init__(self):
# self keyword is necessary to call the variables in to method
# init is the keyword that is used to define constructor
# there are two types of variables in programming languages- class variables and instance variables
# class variables - defined immedietly after class
# class variables are constant no matter how many objects we create
# variables defined inside constructor is called instance variables
#  instant variable will be different for each object created
# when we create object for the class new keyword in not needed

# calculator program

# SUM OF TWO NUMBERS


class Calculator1:
    num = 100
# here num is the class variable

# creating constructor
# give the knowledge of the variables you hav egiven in the object to the constructor
# then store the value
# self is the object and the instance variables are a and b
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b

    def addition(self):
        return self.firstNum + self.secondNum + Calculator1.num

    def subtraction(self):
        return self.firstNum - self.secondNum

# creating object for the class


obj1 = Calculator1(10, 5)
print(obj1.addition())


obj2 = Calculator1(8, 2)
print(obj2.subtraction())








