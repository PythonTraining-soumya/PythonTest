# function is a group of related statements which perform specific tasks
# To declare a function in python use the identifier def
# It is like creating methods in java and passing arguments to the method
# and calling the method name in main and passing the values


def greeting(name):
    print("Hello World " + name)


# Basically we are sending a string so we have to catch it in the function definition
# This is how we create parameters and that created parameters are send to the function


# If you want to call a function
# create a parameter in it

greeting('Soumya')

print("*********************")

# create a function to get the sum of two integers


def addition(a, b):
    print(a+b)


addition(2, 4)

print("************")


def cook(name):
    print("i will make biriyani " + name)


cook("Balu")


print("*****************")
# subtracting two integers


def subtract(a, b):
    return a - b

# instead of print we can return the value also
# When using return keyword we don't have to use the open bracket
# and we will print the output when we call the function


print(subtract(10, 4))

