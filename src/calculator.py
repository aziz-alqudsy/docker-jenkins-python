def add(a, b):
  checkInputs(a, b)
  return a + b

def substract(a, b):
  checkInputs(a, b)
  return a - b

def multiply(a, b):
  checkInputs(a, b)
  return a * b

def divide(a, b):
  checkInputs(a, b)
  return a / b

def checkInputs(a, b):
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError("input must be either integer or float")
