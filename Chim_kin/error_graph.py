import matplotlib.pyplot as plt
import numpy as np

Ts = [1000]
figs = [plt.figure() for i in range(len(Ts))]
axes = [figs[i].add_subplot() for i in range(len(Ts))]
with open("Theoretical_isoterm.csv") as file:
    file.readline()
    data = file.readlines()
theory_data = list(map(lambda x: x.split(';'), data))
step = 0.01
start = 1
stop = 300
for q in range(len(Ts)):
    T = Ts[q]
    #нанесение теоретических точек на график
    theory_x = list(map(lambda x: float(x[2*2+1]), theory_data))
    theory_y = np.array(list(map(lambda x: float(x[2*2]), theory_data)))
    #axes[q].scatter(theory_x, theory_y)

    ros = np.array(theory_x)
    Ps_ideal = 8.31 * T * ros / 0.018
    Ps_ideal /= 1e6
    axes[q].plot(theory_y, abs(Ps_ideal - theory_y) / theory_y * 100)

    num_of_comps = 1
    Ps_vdv = [0] * num_of_comps
    A = np.array([0.556])
    B = np.array([0.0000306])
    xs = np.array([1])
    for i in range(num_of_comps):
        Ps_vdv[i] = (8.31 * T * ros / 0.018 / (1 - ros / 0.018 * B[i]) - A[i] * ros * ros / 0.018 / 0.018)
    Ps_res = ros * 0
    for i in range(num_of_comps):
        Ps_res += Ps_vdv[i] * xs[i]
    Ps_res /= 1e6
    axes[q].plot(theory_y, abs(Ps_res - theory_y) / theory_y * 100)

    axes[q].grid()
    axes[q].set_ylabel("deltaP/P, %")
    axes[q].set_xlabel("P, МПа/моль")
    axes[q].legend(["Идеальный газ", "В-Д-В газ", "Реальные значения"])
    axes[q].set_title(f"Относительная ошибка двух газов при T = {T} K")


plt.show()
