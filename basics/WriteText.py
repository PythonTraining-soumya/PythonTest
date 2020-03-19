# you have to tell python which way we need to open the file  ie is read mode or write mode
# if in read mode then give a flag 'r' and in write mode put a 'w' flag

   # our goal is to reverse the contents in the file and write it back to the file
   # for that first we have to get the content of the file
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    print(reversed(content))
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
