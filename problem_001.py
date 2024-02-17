from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def f(x, y):
    return x**2 + y**2

def g(y, z):
    return y**2 + y*z + z**2

def h(x, z):
    return x**2 + (3**0.5)*x*z + z**2
xr = []
yr = []
zr1 = []
zr2 = []

x1 = None
y1 = None
z1 = None
s1 = 10

for x in np.arange(-7, 7, 0.005):
    for y in np.arange(-7, 7, 0.005):
        d = y**2 - (4*(y**2-36))
        if d < 0:
            continue
        z = (-y + d**0.5)/2

        f1 = (49 - f(x, y)) ** 2
        g1 = (36 - g(y, z)) ** 2
        h1 = (25 - h(x, z)) ** 2

        s = f1 + g1 + h1
        xr.append(x)
        yr.append(y)
        if s > 0.01:
            zr1.append(s)
            zr2.append(99999)
        else:
            zr2.append(s)
            zr1.append(99999)
        if s1 > s:
            s1 = s
            x1 = x
            y1 = y
            z1 = z
# ax.set_zlim3d(0, 1000)
# ax.scatter(xr, yr, zr1, cmap='inferno', s=0.5, alpha=0.5)
# ax.scatter(xr, yr, zr2, c='r', cmap='inferno', s=0.5, alpha=0.5)
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# plt.show()

print(x1, y1, z1)
x, y, z = x1, y1, z1

print(2*x*y + (3**0.5)*y*z + x*z)