# you want to add 2 items in your cart
# initially items in the cart will be 0
# we have to throw exception that if the item number is not equal to throw raise an exception
# raise Exception and assert are the two keywords that we use to raise the exception
# pass is a keyword used to move next line
# you are writing a code and at some point you think that the code will fail and you don't want the test case to fail
# then you can place that particular code in try except mechaism(instead of catch in python there is exception


ItemsInTheCart = 0
if ItemsInTheCart != 2:
    # raise Exception("item count doesnt match")
    pass
    assert (ItemsInTheCart == 0)


# try catch mechanism  real time use example is to check for popup

try:
    with open('testcvdbdz.txt') as reader:
        reader.readline()
except:
    print("raeched the block but something is wrong in the try block")

# here we will be able to know what error python will give by using Exception e
try:
    with open('testcsfsd.txt') as reader:
        reader.readline()
except Exception as e:
    print(e)

# finally is a keyword that is associated with try except
# finally keyword will rum no matter what if there is any failure or pass in the try except mechaism

finally:
    print("test is done ")


