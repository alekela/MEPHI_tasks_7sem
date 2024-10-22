import matplotlib.pyplot as plt
import numpy as np

N_t = 200
N_x = 400
dx = 1 / N_x
dt = 1 / N_t
v = 0.4
r = v * dt / dx


def wave(x):
    if x < 0:
        x += 1
    return np.sin(2 * np.pi * x)


def step(x):
    if x < 0:
        x += 1
    if x < 0.4:
        return 1
    return 0


def exponent(x):
    if x < 0:
        x += 1
    dg = 0.1
    x1 = 2 * dg
    x2 = x1 + 2 * dg
    return np.exp(-(x - x1) ** 2 / dg ** 2) + np.exp(-(x - x2) ** 2 / dg ** 2)


fig = plt.figure()
funcs = [step, wave, exponent]
for f in range(len(funcs)):
    ax = fig.add_subplot(int(f"31{f+1}"))
    c = [[0 for _ in range(N_x)] for _ in range(N_t)]
    xs = np.linspace(0, 1, N_x)

    # задаем начальные условия
    c[0] = np.vectorize(funcs[f])(xs)

    # считаем второй шаг уголком назад
    for j in range(1, N_x):
        c[1][j] = -r * (c[0][j] - c[0][j - 1]) + c[0][j]

    # сам метод
    # matrix*koeffs = R
    for n in range(2, N_t):
        matrix = []
        R = []
        for j in range(N_x):
            line = [0 for _ in range(N_x)]
            line[j - 1] = -(r - 1) * (2 * r - 1)
            line[(j + 1) % N_x] = (r + 1) * (2 * r + 1)
            matrix.append(line)
            tmp = 8 * r * c[n-1][j] - 2 * r * c[n-2][j] - 2 / r * (c[n-1][j] - c[n-2][j])
            R.append(tmp)
        c[n] = [*np.linalg.solve(matrix, R)]

    analit = np.vectorize(funcs[f])(xs - v)

    ax.plot(xs, c[-1])
    ax.plot(xs, analit)
    ax.set_xlabel("x")
    ax.set_ylabel("u")
    ax.legend(["Численное решение", "Аналитическое решение"])
    ax.grid()


plt.show()


fig = plt.figure()
funcs = [step, wave, exponent]
for f in range(len(funcs)):
    xs = np.linspace(0, 1, N_x)
    ax = fig.add_subplot(int(f"31{f+1}"))
    c = np.vectorize(funcs[f])(xs - v)
    ax.plot(xs, c)
    ax.set_xlabel("x")
    ax.set_ylabel("u")
    ax.grid()


plt.show()