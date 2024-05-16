import matplotlib.pyplot as plt
from matplotlib import colors, cm
import numpy as np
from solve_3_layers import res, a1, a2, a3, b1, b2, b3


def compute_coeffs(e, L, S1, S2, D1, D2, pressure):
    coeffs = []
    for coeff in [a1, a2, a3, b1, b2, b3]:
        coeff_sub = res[coeff]
        coeff_sub = coeff_sub.subs("e", e)
        coeff_sub = coeff_sub.subs("L", L)
        coeff_sub = coeff_sub.subs("S1", S1)
        coeff_sub = coeff_sub.subs("S2", S2)
        coeff_sub = coeff_sub.subs("D1", D1)
        coeff_sub = coeff_sub.subs("D2", D2)
        coeff_sub = coeff_sub.subs("c_0", pressure**0.5 * S1)
        coeff_sub = coeff_sub.subs("c_L", 0)

        coeffs.append(coeff_sub)
    return coeffs


def concentration(x, coeffs):
    a1, a2, a3, b1, b2, b3 = coeffs
    if 0 < x <= e:
        return a1 * x + b1
    elif e < x <= L + e:
        return a2 * x + b2
    elif L + e < x <= L + 2 * e:
        return a3 * x + b3


param_vals = np.linspace(0.1, 1, num=10)
sm = plt.cm.ScalarMappable(
    cmap=cm.Blues, norm=colors.Normalize(vmin=0, vmax=max(param_vals))
)

# varying D_coating only
fig, axs = plt.subplots()
for param in param_vals:
    e = 0.2
    L = 1
    S2 = 1
    D2 = 1
    S1 = 1
    D1 = param
    pressure = 1

    coeffs = compute_coeffs(e, L, S1, S2, D1, D2, pressure)

    x = np.linspace(0, L + 2 * e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param / (param_vals.max()))
    plt.plot(x, c, color=colour)

plt.vlines(x=0.2, ymin=0, ymax=1, color="grey", linestyle="dashed", alpha=0.5)
plt.vlines(x=1.2, ymin=0, ymax=1, color="grey", linestyle="dashed", alpha=0.5)
fig.colorbar(sm, ax=axs, label=r"D$_{\mathrm{coating}}$")
plt.xlim(0, 1.4)
plt.ylim(0, 1)
plt.xlabel(r"x")
plt.ylabel(r"c$_{\mathrm{m}}$")
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.savefig("cartesian_profile_varying_diffusivity.png")

# varying S_coating only
fig, axs = plt.subplots()
for param in param_vals:
    e = 0.2
    L = 1
    S2 = 1
    D2 = 1
    S1 = param
    D1 = 1
    pressure = 1

    coeffs = compute_coeffs(e, L, S1, S2, D1, D2, pressure)

    x = np.linspace(0, L + 2 * e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param / (param_vals.max()))
    plt.plot(x, c, color=colour)

plt.vlines(x=0.2, ymin=0, ymax=1, color="grey", linestyle="dashed", alpha=0.5)
plt.vlines(x=1.2, ymin=0, ymax=1, color="grey", linestyle="dashed", alpha=0.5)
fig.colorbar(sm, ax=axs, label=r"S$_{\mathrm{coating}}$")
plt.xlim(0, 1.4)
plt.ylim(0, 1)
plt.xlabel(r"x")
plt.ylabel(r"c$_{\mathrm{m}}$")
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.savefig("cartesian_profile_varying_solutbility.png")


plt.show()
