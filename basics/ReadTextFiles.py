# open is the method that will help us to access the text file
# we can open the file using with keyword also
# with open('test.txt') as file:    if we are writing this we don't want to write file.close()
# we have to pass the path of the text file to the method
# her the file comes under the same package so give the name of the text file directly in single quotes
# then create the file object
# Whenever we create a file make sure to close the file to prevent file curreption and memory leakage

#file = open('test.txt')
with open('test.txt') as file:

# to read all the contents ofa file , use read method
# print(file.read())

# If you want to read only two characters from a file give the number up to which you want to ad
# print(file.read(8))

# if you want to read a particular line by line in the file the file
# print(file.readline())
# print(file.readline())

# if you want to read all the contents in the file in a list
#print(file.readlines())

# interview question
     # print line by line using readaline method
#line = file.readline()
#while line != "":
    ##line = file.readline()

 line = ['I am Soumya', 'I am married', 'My husband is Balu', 'My childrens are Siddhu and Jaggu']
print(line[1])

for i in line:
    print(line)
    print(line[1: 3])
    print(line[0])
    break









#file.close()