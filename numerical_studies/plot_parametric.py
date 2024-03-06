import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import linregress

reduction_factors = np.geomspace(1e2, 1e04, num=10)
temperature_values = [400, 500, 600, 700]


# standard case
filename_standard_data = "Results/parametric_study/standard/derived_quantities.csv"
standard_data = np.genfromtxt(filename_standard_data, delimiter=",", names=True)
standard_flux = standard_data["Flux_surface_2_solute"]


modified_fluxes = []
folder = "Results/parametric_study/"
for T in temperature_values:
    values_per_T = []
    for factor in reduction_factors:
        filename_data = folder + "T={:.0f}/factor={:.0e}/derived_quantities.csv".format(
            T, factor
        )
        data = np.genfromtxt(filename_data, delimiter=",", names=True)
        values_per_T.append(data["Flux_surface_2_solute"])
    modified_fluxes.append(values_per_T)

modified_fluxes = np.array(modified_fluxes)

normalised_fluxes = standard_flux / modified_fluxes


plt.figure()

for case, T in zip(normalised_fluxes, temperature_values):
    plt.plot(reduction_factors, case, label="T = {:.0f}".format(T))

plt.legend()


# res = linregress(solubilities_normalised, flux_normalised)
# behaviour_law = np.exp(res.intercept)*np.exp(solubilities_normalised*res.slope)
# print(res.rvalue**2)
# print(res.intercept)
# print(res.slope)
# print("Behaviour Law : {:.4e} exp ({:.4}*x)".format(np.exp(res.intercept), res.slope))


plt.yscale("log")
plt.xscale("log")
plt.ylabel(r"PRF")
plt.xlabel(r"Modification factor")

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()

plt.show()
