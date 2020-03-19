# to print list of arrays
a = [1, 2, 3, 4, 5, 'soumya sreekumar']
print(a)

# To print the 5th index which is the 6th value
print(a[5])

print('The name of the student is ', a[5], 'and she is working hard to get to number ', a[0])

# if you want to print the last index
print(a[-1])

# if you want to print the sub values
print(a[1:4])

# if you want to insert a value into the array
a.insert(3, 'Balu')
print(a)
print(a[3])

# if you want to add a value at the end use the word append
a.append(13)
print(a)

# if you want to remove a value from the list
a.remove(3)
print(a)

# if you want to reverse the list of arrays
a.reverse()
print(a)

# if you want to copy the list of array
a.copy()
print(a)

a.reverse()
print(a)
a[1] = 2
print(a)

# If you want to make any value uppercase that is we are updating the excisting value
a[5] = 'SOUMYA SREEKUMAR'
a[2] = 'BALU'
print(a)

# if you want to delete a particular value
del a[5]
print(a)

