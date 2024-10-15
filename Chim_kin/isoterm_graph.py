import matplotlib.pyplot as plt
import numpy as np

Ts = [300, 500, 1000]
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
    ros = np.linspace(start, stop, 100000)
    Ps_ideal = 8.31 * T * ros / 0.018
    Ps_ideal /= 1e6
    axes[q].plot(ros, Ps_ideal)

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
    axes[q].plot(ros, Ps_res)

    #нанесение теоретических точек на график
    theory_x = list(map(lambda x: float(x[2*q+1]), theory_data))
    theory_y = list(map(lambda x: float(x[2*q]), theory_data))
    axes[q].scatter(theory_x, theory_y)

    axes[q].grid()
    axes[q].set_ylabel("P, МПа/моль")
    axes[q].set_xlabel("ρ, кг/моль*м³")
    axes[q].legend(["Идеальный газ", "В-Д-В газ", "Реальные значения"])
    axes[q].set_title(f"Сравнение двух газов при T = {T} K")


plt.show()
