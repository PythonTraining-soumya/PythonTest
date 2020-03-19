# inheritance is accuring the properties of parent class
# which means the child class will accure all properties of the parent class(all the methods, variables etc)
# if yo want to inherit a parent class use class ChildImpl(parentclassname)
# give the constructor knowledge from parent class to child class
from basics.SampleOopsPrgm import Calculator


class ChildImpl(Calculator):

    def __init__(self):
        Calculator.__init__(self, 4, 4, 4)

    def getting(self):
        return self.sum()


obj = ChildImpl()
print(obj.getting())




