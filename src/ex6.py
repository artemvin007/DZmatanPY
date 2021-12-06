import sympy as sym
import numpy as np


x, y = sym.symbols('x y')

f = sym.cos(x + y)

f1 = f.diff(x)
f2 = f.diff(y)
print(f1, '       ', f2)
diff_y = sym.expand(f1 / f2)
print(diff_y)
#1
