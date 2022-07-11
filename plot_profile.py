import matplotlib.pyplot as plt
from matplotlib import ticker, colors, cm
import numpy as np
from solve_3_layers import PRF_expression, res, a1, a2, a3, b1, b2, b3

plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

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
        coeff_sub = coeff_sub.subs("c_0", pressure**0.5*S1)
        coeff_sub = coeff_sub.subs("c_L", 0)

        coeffs.append(coeff_sub)
    return coeffs


def concentration(x, coeffs):
    a1, a2, a3, b1, b2, b3 = coeffs
    if 0 < x <= e:
        return a1*x + b1
    elif e < x <= L + e:
        return a2*x + b2
    elif L + e < x <= L + 2*e:
        return a3*x + b3


param_vals = np.linspace(0.1, 1, num=4)
sm = plt.cm.ScalarMappable(cmap=cm.Blues, norm=colors.Normalize(vmin=0, vmax=max(param_vals)))

# varying D_coating only
for param in param_vals:
    e = 0.1
    L = 1
    S2 = 1
    D2 = 1
    S1 = 1
    D1 = param
    pressure = 1

    coeffs = compute_coeffs(e, L, S1, S2, D1, D2, pressure)

    x = np.linspace(0, L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x, c, color=colour)

plt.colorbar(sm, label="$D_{\mathrm{coating}}$")
plt.xlabel("x")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()

# varying e only
for param in param_vals:
    e = param
    L = 1
    S2 = 1
    D2 = 1
    S1 = 1
    D1 = 1
    pressure = 1

    coeffs = compute_coeffs(e, L, S1, S2, D1, D2, pressure)

    x = np.linspace(0, L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x, c, color=colour)

plt.colorbar(sm, label="$e$")
plt.xlabel("x")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()

# varying S_coating only
for param in param_vals:
    e = 0.1
    L = 1
    S2 = 1
    D2 = 1
    S1 = param
    D1 = 1
    pressure = 1

    coeffs = compute_coeffs(e, L, S1, S2, D1, D2, pressure)

    x = np.linspace(0, L + 2*e, num=200)
    c = [concentration(x_val, coeffs) for x_val in x]
    colour = cm.Blues(param/(param_vals.max()))
    plt.plot(x, c, color=colour)

plt.colorbar(sm, label="$S_{\mathrm{coating}}$")
plt.xlabel("x")
plt.ylabel("c$_{\mathrm{m}}$")
plt.show()
