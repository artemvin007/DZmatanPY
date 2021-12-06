import sympy as sym
import numpy as np


def max_expand(y):
    y = y.diff(x)
    y = sym.expand(y)
    return (y)


x = sym.Symbol('x')
y = x ** sym.sin(x)

print(max_expand(y))
#x**sin(x)*log(x)*cos(x) + x**sin(x)*sin(x)/x
