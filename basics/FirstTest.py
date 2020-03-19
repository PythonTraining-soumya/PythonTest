# print the text
print("hello world")

a = 3
b = 4
print(type(a))
Sum = a + b
print(Sum)

greet = "Hello World"
print(greet)

x = 'Soumya'
y = 'sreekumar'
print(x, "concatenated with", y)
print(x+" concated with "+y)

c, d, e, f = 1.234, 4.56, 2, "Wonderful"
Sum = c + d + e
print(Sum)
print(f)
# if you want to print string and numbers together use the below format
print("{} {} {}".format(Sum, "is", f))

# to know what kind of variable it is printing
print(type(Sum))
print(type(f))

# to print the data types
a = 100
print("The variable having value ", a, "is", type(a))

b = 2.34
print("The value ", b, "is", type(b))

c = -3.245678234
print("The number ", c, "is", type(c))

d = 100 + 2.34j
print("The value present in ", d, "is", type(d))



