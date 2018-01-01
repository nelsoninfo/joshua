from scipy.interpolate import interp1d

x = np.arange(0,5,1)
y = np.array([0.1,0.2,0.3,0.5,1.0,0.9])

%matplotlib inline
import matplotlib.pyplot as plt

plt.plot(x,y,'bo')
print(x)