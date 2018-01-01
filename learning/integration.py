from scipy.integrate import quad

def f(x):
	return x**2

print(quad(f,0,2)[0])
print(2**3/3)

import sympy as sympy
sym.init_printing()
x = sym.Symbol('x')
f = sym.integrate(x**2,x)
sym.pprint(f)
