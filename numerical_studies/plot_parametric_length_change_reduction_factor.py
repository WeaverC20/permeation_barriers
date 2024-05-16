import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm
import numpy as np

reduction_factors = np.geomspace(1e0, 1e08, num=50)
lengths = np.geomspace(1e-02, 1e-06, num=10)

prf_values = []

folder = "Results/parametric_study/length_change/"
for length in lengths:
    standard_case = folder + "L={:.1e}m/prf=1/derived_quantities.csv".format(length)
    standard_data = np.genfromtxt(standard_case, delimiter=",", names=True)
    standard_flux = standard_data["Flux_surface_2_solute"] * -1

    prf_values_per_length = []
    for factor in reduction_factors:
        filename_data = folder + "L={:.1e}m/prf={:.1e}/derived_quantities.csv".format(
            length, factor
        )
        data = np.genfromtxt(filename_data, delimiter=",", names=True)
        modified_flux = data["Flux_surface_2_solute"] * -1

        prf_value = standard_flux / modified_flux
        prf_values_per_length.append(prf_value)

    prf_values.append(prf_values_per_length)


plt.figure()

for case, length in zip(prf_values, lengths):
    plt.plot(reduction_factors, case, label="L = {:.1e}m".format(length))

plt.legend()
plt.yscale("log")
plt.xscale("log")
plt.ylabel(r"PRF")
plt.xlabel(r"Modification factor")
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.grid()

plt.show()
