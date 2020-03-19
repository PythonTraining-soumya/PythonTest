num = 4
while num > 1:
    print(num)
    num = num - 1


print("************")

# Skip number 3
num = 4
while num > 1:
    if num != 3:
        print(num)
    num = num - 1

print("************************")
# introducing break key word
num = 4
while num > 1:
    if num == 3:
        break
    print(num)
    num = num - 1


print("************************")
# introducing break key word
num = 11
while num > 1:
    if num == 2:
        num = num - 1
        continue

    if num == 3:
        break
    print(num)
    num = num - 1
