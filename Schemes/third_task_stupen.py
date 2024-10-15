import matplotlib.pyplot as plt
import numpy as np

N_t = 1000
N_x = 1000
dx = 1 / N_x
dt = 1 / N_t
v = 0.8
r = v * dt / dx

c = [[0 for _ in range(N_x)] for _ in range(N_t)]

# задаем начальные условия
c[0] = [1 for _ in range(int(N_x * 0.4))] + [0 for _ in range(int(N_x * 0.6))]

#считаем второй шаг для креста
for j in range(1, N_x):
    c[1][j] = -r * (c[0][j] - c[0][j-1]) + c[0][j]

# сам метод крест
for n in range(2, N_t):
    for j in range(N_x):
        c[n][j] = -r * (c[n - 1][(j + 1) % N_x] - c[n - 1][j - 1]) + c[n - 2][j]

#убираем два фиктивных граничных слоя

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
fig2 = plt.figure()
ax2d1 = fig2.add_subplot(211)
ax2d2 = fig2.add_subplot(212)

xs = [i*dx for i in range(N_x)]
ts = [n*dt for n in range(N_t)]
xs, ts = np.meshgrid(xs, ts)
#ax.scatter(xs, ts, c, c=ts, cmap="plasma")
ax.set_xlabel("X")
ax.set_ylabel("t")
ax.set_zlabel("u")

ax2d1.plot(xs[0], c[0])
ax2d2.plot(xs[0], c[-1])
plt.show()
