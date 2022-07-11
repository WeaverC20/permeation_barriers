import matplotlib.pyplot as plt
from matplotlib import ticker, colors, cm
import numpy as np
from solve_3_layers_cylindrical import res, a1, a2, a3, b1, b2, b3


def compute_coeffs(e, r_0, D1, D2, S1, S2, L, c_0):
    coeffs = []
    for coeff in [a1, a2, a3, b1, b2, b3]:
        coeff_sub = res[coeff]
        coeff_sub = coeff_sub.subs("e", e)
        coeff_sub = coeff_sub.subs("r_0", r_0)
        coeff_sub = coeff_sub.subs("S1", S1)
        coeff_sub = coeff_sub.subs("S2", S2)
        coeff_sub = coeff_sub.subs("L", L)
        coeff_sub = coeff_sub.subs("D1", D1)
        coeff_sub = coeff_sub.subs("D2", D2)
        coeff_sub = coeff_sub.subs("c_0", c_0)
        coeff_sub = coeff_sub.subs("c_L", 0)

        coeffs.append(coeff_sub)
    return coeffs


def concentration(r, coeffs):
    a1, a2, a3, b1, b2, b3 = coeffs
    if r_0 < r <= r_0 + e:
        return a1*np.log(r) + b1
    elif r_0 + e < r <= r_0 + L + e:
        return a2*np.log(r) + b2
    elif r_0 + L + e < r <= r_0 + L + 2*e:
        return a3*np.log(r) + b3


param_vals = np.linspace(0.1, 1, num=4)
sm = plt.cm.ScalarMappable(cmap=cm.Blues, norm=colors.Normalize(vmin=0, vmax=max(param_vals)))


# varying S_coating only
for param in param_vals:
    r_0 = 0.5
    e = 1
    L = 1
    S2 = 1
    D2 = 1
    S1 = param
    D1 = 1
    pressure = 1

    coeffs = compute_coeffs(e, r_0, D1, D2, S1, S2, L, pressure**0.5*S1)

    x = np.linspace(r_0, r_0 + L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x, c, color=colour)

plt.colorbar(sm, label="$S_{\mathrm{coating}}$")
plt.xlabel("r")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()

# varying D_coating only
for param in param_vals:
    r_0 = 0.5
    e = 1
    L = 1
    S2 = 1
    D2 = 1
    S1 = 1
    D1 = param
    pressure = 1

    coeffs = compute_coeffs(e, r_0, D1, D2, S1, S2, L, pressure**0.5*S1)

    x = np.linspace(r_0, r_0 + L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x, c, color=colour)

plt.colorbar(sm, label="$D_{\mathrm{coating}}$")
plt.xlabel("r")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()

# varying e only
for param in param_vals:
    r_0 = 0.5
    e = param
    L = 1
    S2 = 1
    D2 = 1
    S1 = 1
    D1 = 1
    pressure = 1

    coeffs = compute_coeffs(e, r_0, D1, D2, S1, S2, L, pressure**0.5*S1)

    x = np.linspace(r_0, r_0 + L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x, c, color=colour)

plt.colorbar(sm, label="$e_{\mathrm{coating}}$")
plt.xlabel("r")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()

# varying r_0 only

r_0_vals = np.logspace(-1, 2, num=4)

for param in r_0_vals:
    r_0 = param
    e = 0.1
    L = 1
    S2 = 1
    D2 = 1
    S1 = 1
    D1 = 1
    pressure = 1

    coeffs = compute_coeffs(e, r_0, D1, D2, S1, S2, L, pressure**0.5*S1)

    x = np.linspace(r_0, r_0 + L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x - r_0, c, color=colour)

plt.colorbar(sm, label="$r_0$")
plt.xlabel("$r - r_0$")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()
