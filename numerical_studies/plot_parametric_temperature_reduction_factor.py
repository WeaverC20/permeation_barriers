import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm
import numpy as np

reduction_factors = np.geomspace(1e2, 1e04, num=10)
temperature_values = [400, 600, 800, 1000, 1200]


prf_values = []

folder = "Results/parametric_study/"
for T in temperature_values:
    standard_case = folder + "T={:.0f}/factor=1/derived_quantities.csv".format(T)
    standard_data = np.genfromtxt(standard_case, delimiter=",", names=True)
    standard_flux = standard_data["Flux_surface_2_solute"] * -1

    prf_values_per_T = []
    for factor in reduction_factors:
        filename_data = folder + "T={:.0f}/factor={:.1e}/derived_quantities.csv".format(
            T, factor
        )
        data = np.genfromtxt(filename_data, delimiter=",", names=True)
        modified_flux = data["Flux_surface_2_solute"] * -1

        prf_value = standard_flux / modified_flux
        prf_values_per_T.append(prf_value)

    prf_values.append(prf_values_per_T)


plt.figure()

for case, T in zip(prf_values, temperature_values):
    plt.plot(reduction_factors, case, label="T = {:.0f}".format(T))

plt.legend()
plt.yscale("log")
plt.xscale("log")
plt.ylabel(r"PRF")
plt.xlabel(r"Modification factor")
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()

plt.show()
