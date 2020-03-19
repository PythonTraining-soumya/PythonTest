a = [2, 4, 6, 8, 10]
for i in a:
    print(i*2)


# sum of first 5 natural numbers 1 + 2 + 3 + 4 + 5
# here range means it will take the numbers from 1 to n-1 ie (6-1=5)
Sum = 0
for i in range(1, 6):
    Sum = Sum + i
print(Sum)

# Sum of first 5 even numbers
# here 2 at the end means jump 2 times after every number
Sum = 0
for i in range(2, 11, 2):
    Sum = Sum + i
print(Sum)

# sum of all odd numbers till 100
Sum = 0
for i in range(1, 100, 2):
    Sum = Sum + i
print(Sum)

# Sum of all even numbers till 100
Sum = 0
for i in range(2, 101, 2):
    Sum = Sum + i
print(Sum)

print("***************")
# Skipping the first index
for i in range(100):
    print(i)
