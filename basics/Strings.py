Str = "My name is Soumya"
# if to get the value from the index
# space is considered as an index in python
print(Str[8])

# to print the string in the lower case
print(Str.lower())

# if you want to print the string in swapped form
print(Str.swapcase())

# to print the String index of a letter
print(Str.index('e'))

# To check whether the string is in upper case
print(Str.isupper())

# if you want to replace a string with an new one
print(Str.replace("name", "NAME"))

# if you want to print the substring (print only some value in the String)
print(Str[0: 7])
print(Str[11: 17])

# to concatenate two Strings
Str = "My name is Soumya"
Str1 = " Hello"
print(Str + Str1)
print("Say to soumya " + Str1 + " is good")
print(("Say to soumya " + Str1 + " is good").swapcase())

# concatenating integer and string
Str1 = " Hello"
a, b, c = 1, 2, 3
Sum = a + b + c
print("{} {} {}".format(Str1, Sum, "is done"))
print("{} {} {}".format(Str1, Sum, "is done").swapcase())
print("{} {}".format(Str1, Sum))

# to check if actions are possible
print(Str1.isnumeric())
print((Str + Str1).isprintable())

# to check if a string is present in the main string
# in is the keyword which helps to find out if a string is present in the other string(SubString check)
print("name" in Str)
print('h' in Str1)

# we can loop also to find  if a value is present or not
if "name" in Str:
    print("Condition is reached")
else:
    print("Condition is not reached")

# in order to trim (in python there is no trim function so we use strip )only a portion of a string
str2 = "  soumyabalu_hotmail"
print(str2.strip("_"))

# in order to left strip(left trim)
print(str2.lstrip())

# in order to right strip(right trim)
print(str2.rstrip())

# in order to strip the string
var = str2.split("_")

# in order to right split a string
var1 = str2.rsplit()
print(var)
print(var1)
print(var[0])







