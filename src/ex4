import sympy as sym
import numpy as np


def max_expand(y):
    y = y.diff(x)
    y = sym.expand(y)
    return (y)


x = sym.Symbol('x')
y = 10**(x**(1 / 2))

print(max_expand(y))
#0.5*10**(x**0.5)*log(10)/x**0.5
