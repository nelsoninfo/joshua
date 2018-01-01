from scipy.misc import derivative

def f(x):
	return x**3

print(derivative(f,2,dx=1e-10))

import sympy as sym
x = sym.Symbol('x')
f = sym.diff(x**3,x)
f.subs(x,2)
