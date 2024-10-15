import matplotlib.pyplot as plt
import numpy as np

Ps = np.array([1, 100, 5000])
Ps *= 100000
figs = [plt.figure() for i in range(len(Ps))]
axes = [figs[i].add_subplot() for i in range(len(Ps))]
with open("Theoretical_isobar.csv") as file:
    file.readline()
    data = file.readlines()
theory_data = list(map(lambda x: x.split(';'), data))
step = 0.01
start = 15
stop = 50
for q in range(len(Ps)):
    P = Ps[q]
    Vs = np.linspace(start, stop, 100000)
    Vs /= 1000000
    Ts_ideal = P * Vs / 8.31
    axes[q].plot(Vs, Ts_ideal)

    num_of_comps = 1
    Ts_vdv = [0] * num_of_comps
    A = np.array([0.556])
    B = np.array([0.0000306])
    xs = np.array([1])
    for i in range(num_of_comps):
        Ts_vdv[i] = (P + A[i] / Vs / Vs) * (Vs - B[i]) / 8.31
    Ts_res = Vs * 0
    for i in range(num_of_comps):
        Ts_res += Ts_vdv[i] * xs[i]
    axes[q].plot(Vs, Ts_res)

    #нанесение теоретических точек на график
    theory_x = list(map(lambda x: float(x[2*q+1]), theory_data))
    theory_y = list(map(lambda x: float(x[2*q]), theory_data))
    axes[q].scatter(np.array(theory_x) * 0.018, theory_y)

    axes[q].grid()
    axes[q].set_ylabel("T, К")
    axes[q].set_xlabel("V, м³/моль")
    axes[q].legend(["Идеальный газ", "В-Д-В газ", "Реальные значения"])
    axes[q].set_title(f"Сравнение двух газов при P = {P} Па")


plt.show()
