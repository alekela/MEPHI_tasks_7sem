import matplotlib.pyplot as plt
import numpy as np

N_t = 1000
N_x = 1000
dx = 1 / N_x
dt = 1 / N_t
v = 0.5
r = v * dt / dx




# метод Лакса-Вендера
def Laks_Vendroff(c, limiter):
    for n in range(1, N_t):
        for j in range(N_x):
            c[n][j] = c[n - 1][j] - r * (c[n - 1][j] - c[n - 1][j - 1]) - r * (1 - r) * 0.5 * (
                    limiter(c[n - 1][j - 1], c[n - 1][j], c[n - 1][(j + 1) % N_x]) * (
                    c[n - 1][(j + 1) % N_x] - c[n - 1][j]) - limiter(c[n - 1][j - 2], c[n - 1][j - 1],
                                                                     c[n - 1][j]) * (
                            c[n - 1][j] - c[n - 1][j - 1]))


theoretical = [0 for _ in range(int(N_x * v))]+[1 for _ in range(int(N_x * 0.4))]+[0 for _ in range(int(N_x * (0.6 - v)))] + [0]
theoretical = np.array(theoretical)

def Osher(c0, c1, c2):
    beta = 1.5
    if c2 == c1:
        return beta
    r = (c1 - c0) / (c2 - c1)
    return max(0, min(r, beta))


def ospre(c0, c1, c2):
    if c2 == c1:
        return 1.5
    r = (c1 - c0) / (c2 - c1)
    return 1.5 * (r ** 2 + r) / (r ** 2 + r + 1)


def smart(c0, c1, c2):
    if c2 == c1:
        return 4
    r = (c1 - c0) / (c2 - c1)
    return max(0, min(2 * r, 0.25 + 0.75 * r, 4))


funcs = [Osher, ospre, smart, lambda x, y, z: 1]
fig = plt.figure()
fig2 = plt.figure()
ax2 = []
ax = []
for i in range(len(funcs)):
    ax.append(fig.add_subplot(int(f'41{i + 1}')))

for i in range(len(funcs) + 1):
    ax2.append(fig2.add_subplot(int(f'51{i + 1}')))

xs = [i * dx for i in range(N_x)]
ts = [n * dt for n in range(N_t)]
xs, ts = np.meshgrid(xs, ts)
for i in range(len(funcs)):
    c = [[0 for _ in range(N_x)] for _ in range(N_t)]
    # задаем начальные условия
    c[0] = [1 for _ in range(int(N_x * 0.4))] + [0 for _ in range(int(N_x * 0.6))]
    Laks_Vendroff(c, funcs[i])
    ax2[i].plot(xs[0], c[-1])
    ax2[i].set_title(f"Solution for {funcs[i].__name__ if funcs[i].__name__ != '<lambda>' else 'no'} limiter")
    tmp = np.array(c[-1])
    ax[i].plot(xs[0], abs(tmp - theoretical))
    ax[i].set_title(f"delta for {funcs[i].__name__ if funcs[i].__name__ != '<lambda>' else 'no'} limiter")

ax2[4].plot(xs[0], theoretical)
ax2[4].set_title("Theoretical solution")

plt.show()
