import math
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(nr1, nr2):
  return nr1 + nr2

def subtract(nr1: float, nr2: float) -> float:
  return nr1 - nr2

def multiply(nr1: float, nr2: float) -> float:
  return nr1 * nr2

def divide(nr1: float, nr2: float) -> float:
  if nr2 == 0: return None
  return nr1 / nr2

def calculate_cilinder_content(diametr, heigt):
  return multiply(heigt,(multiply(pow(divide(diametr,2),2), math.pi)))

