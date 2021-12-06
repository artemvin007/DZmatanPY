import sympy as sym
import numpy as np

def max_expand(y):
  y = y.diff(x)
  y = sym.expand(y)
  return(y)

x = sym.Symbol('x')
y = sym.cot(x) / x **(1/2)


print(max_expand(y))
#-0.5*cot(x)/x**1.5 - cot(x)**2/x**0.5 - 1/x**0.5
