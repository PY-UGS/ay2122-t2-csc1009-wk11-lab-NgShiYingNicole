class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
    def adder(self):
        return self.input1+self.input2
    def subtractor(self):
        return self.input1-self.input2
    def multiplier(self):
        return self.input1*self.input2
    def divider(self):
        return self.input1/self.input2
    def clear(self):
        self.input1=0
        self.input2=0
        
input1 = float(input("Please enter the first number: "))
input2 = float(input("Please enter the second number: "))

cal = Calculator(input1, input2)

print(f'Adding: {cal.input1} + {cal.input2} = {cal.adder()}')
print(f'Subtracting: {cal.input1} - {cal.input2} = {cal.subtractor()}')
print(f'Multiplying: {cal.input1} * {cal.input2} = {cal.multiplier()}')
print(f'Dividing: {cal.input1} / {cal.input2} = {cal.divider()}')
cal.clear()
print(f'After reset: value of input1 is {cal.input1} and value of input2 is {cal.input2}')
