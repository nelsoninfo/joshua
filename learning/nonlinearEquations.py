from scipy.optimize import fsolve

def f(z):
	x = z[0]
	y = z[1]
	return [x+2*y, x**2+y**2-1]

z0 = [0,1]
z = fsolve(f,z0)
print(z)
print(f(z))

