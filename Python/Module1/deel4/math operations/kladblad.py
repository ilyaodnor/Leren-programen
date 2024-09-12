from test_lib import test, report
from math_operations import increment, decrement, add, subtract, multiply, divide

nr1 = 3
nr2 = 11
nr3 = 37
nr4 = 79
result1 = (nr1 - (nr4 - nr3)) / (nr2 + nr3)
print(result1)
result2 = subtract(nr1, subtract(nr4,nr3)) / add(nr2,nr3)
print(result2)