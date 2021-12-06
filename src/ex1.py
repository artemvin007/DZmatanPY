import sympy as sym
import numpy as np

def max_expand(y):
  y = y.diff(x)
  y = sym.expand(y)
  return(y)

x = sym.Symbol('x')
y = (x**(1 / 2) + 1) * (x**(-1/2) - 1)


yprime = sym.expand(y.diff(x))
print(yprime)
