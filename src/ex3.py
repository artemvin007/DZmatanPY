import sympy as sym
import numpy as np

def max_expand(y):
  y = y.diff(x)
  y = sym.expand(y)
  return(y)

x = sym.Symbol('x')
y = sym.log(x - sym.cos(x), 10)


print(max_expand(y))
#sin(x)/(x*log(10) - log(10)*cos(x)) + 1/(x*log(10) - log(10)*cos(x))
