from test_lib import *

def addition(num1:float, num2:float):
    return num1 + num2
def substracrion(num1:float,num2:float):
    return num1 - num2
def multiplication(num1:float,num2:float):
    return num1*num2
def division(num1:float,num2:float):
    return num1/num2

a = 11 + 11
test('text 1: addition' ,addition(11,11), 22)


report()