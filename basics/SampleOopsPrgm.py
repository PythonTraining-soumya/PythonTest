class Calculator:

    def __init__(self, a, b, c):
        self.firstNum = a
        self.secondNum = b
        self.thirdNum = c

    def sum(self):
        return self.firstNum + self.secondNum + self.thirdNum

    def sub(self):
        return self.firstNum - self.secondNum - self.thirdNum

    def prod(self):
        return self.firstNum * self.secondNum * self.thirdNum

    def div(self):
        return self.firstNum / self.secondNum / self.thirdNum


obj = Calculator(8, 2, 5)
print(obj.sum())
print(obj.sub())
print(obj.prod())
print(obj.div())



