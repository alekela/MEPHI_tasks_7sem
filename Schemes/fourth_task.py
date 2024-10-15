import matplotlib.pyplot as plt
import numpy as np


def a0a2(x, r):
     return (x * r * (r - 1) - r ** 2 + r + 1) / (r**2 + r) / 3


def a0a1(x, r):
     return (-2*x*r**2 + 2 * r**2 + r) / (2 * r**2 + r - 1)


def a0a11(x, r):
     return (-2 * x * r ** 2 + 2 * r ** 2 + 2 * x * r - 5 * r + 1) / (6 * r ** 2 - 3 * r)



r = 0.25
for r in range(0, 100):
     r /= 100
     
x = np.linspace(0, 5, 1000)
plt.plot(x, a0a2(x, r))

plt.grid()
plt.xlabel("a0")
plt.ylabel("a-2")
plt.scatter(4.33, 0.4, color='r')
plt.legend(["a-2(a0)", "3 порядок точности"])
plt.show()
