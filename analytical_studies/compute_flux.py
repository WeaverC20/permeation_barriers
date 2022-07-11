import numpy as np
import matplotlib.pyplot as plt


def compute_flux(alpha, beta, gamma, c_0, c_L, D1, L):
    """Returns the steady state flux of particles
    given a bunch of parameters
    from Influence of interface conditions on hydrogen transport studies
    R. Delaporte-Mathurin et al
    Eq 18b

    Args:
        alpha (float): D2/D1 ratio of diffusivities
        beta (float): S2/S1 ratio of solubilities
        gamma (float): x_interface / L ratio of the interface position to the
            total length (between 0 and 1)
        c_0 (float): concentration at x=0 (H/m3)
        c_L (float): concentration at x=L (H/m3)
        D1 (float): Diffusivity of the material on the left (m2/s)
        L (float): Length of the sample (mat1 + mat2) (m)

    Returns:
        float: outgassing flux (H/m2/s)
    """

    c_l_normalised = c_L / c_0
    a_0 = 2*alpha**0.5*(c_l_normalised - beta) / (2*(1 + alpha*beta*gamma - gamma))
    a_1 = a_0 * alpha**0.5
    flux = - D1 * a_1 * c_0/L
    return flux


values = np.linspace(0, 1)
XX, YY = np.meshgrid(values, values)

fig, axs = plt.subplots(1, 3, figsize=(6.4, 4))

plt.sca(axs[0])
flux = compute_flux(alpha=0.5, beta=XX, gamma=YY, c_0=1, c_L=0, D1=1, L=1)
CF = plt.contourf(XX, YY, flux, levels=1000)
plt.contour(XX, YY, flux, levels=30, colors="white")
plt.xlabel(r"$S_2/S_1$")
plt.ylabel(r"$x_{int}/L$")

plt.sca(axs[1])
flux = compute_flux(alpha=XX, beta=0.5, gamma=YY, c_0=1, c_L=0, D1=1, L=1)
CF = plt.contourf(XX, YY, flux, levels=1000)
plt.contour(XX, YY, flux, levels=30, colors="white")
plt.xlabel(r"$D_2/D_1$")
plt.ylabel(r"$x_{int}/L$")

plt.sca(axs[2])
flux = compute_flux(alpha=XX, beta=YY, gamma=0.5, c_0=1, c_L=0, D1=1, L=1)
CF = plt.contourf(XX, YY, flux, levels=1000)
plt.contour(XX, YY, flux, levels=30, colors="white")
plt.xlabel(r"$D_2/D_1$")
plt.ylabel(r"$S_2/S_1$")
# plt.colorbar(CF, label="Flux", ax=axs)

for ax in axs:
    ax.set_aspect("equal")
plt.tight_layout()
plt.show()
