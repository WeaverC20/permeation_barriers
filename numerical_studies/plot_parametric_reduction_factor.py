import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

reduction_factors = np.geomspace(1e0, 1e08, num=50)
results_folder = "Results/parametric_study/reduction_factor/"

standard_case = results_folder + "standard_case/derived_quantities.csv"
standard_data = np.genfromtxt(standard_case, delimiter=",", names=True)
standard_flux = standard_data["Flux_surface_2_solute"] * -1

modified_fluxes = []

for factor in reduction_factors:
    filename_data = results_folder + "factor={:.1e}/derived_quantities.csv".format(
        factor
    )
    data = np.genfromtxt(filename_data, delimiter=",", names=True)
    modified_fluxes.append(data["Flux_surface_2_solute"] * -1)

modified_fluxes = np.array(modified_fluxes)
PRF = standard_flux / modified_fluxes

plt.figure()

plt.plot(reduction_factors, PRF, color="black")


res = linregress(PRF, reduction_factors)
# behaviour_law = np.exp(res.intercept) * np.exp(reduction_factors * res.slope)
# print(res.rvalue)
# print("{:.4f}".format(res.rvalue))
# print(res.intercept)
# print(res.slope)
print("Behaviour Law : {:.4e} * x + {:.4}".format(res.slope, res.intercept))


plt.yscale("log")
plt.xscale("log")
plt.ylabel(r"PRF")
plt.xlabel(r"Modification factor")
plt.ylim(1e0, 1e08)
plt.xlim(1e0, 1e08)

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.grid()

# x = 1000
# y = 1.5314 * x**1.0111
prf = 1000
x = res.slope * prf + res.intercept
print(x)
plt.vlines(x, ymin=1e0, ymax=prf, color="red")
plt.hlines(1000, xmin=1e0, xmax=x, color="red")


plt.annotate("PRF = 1000", (1e01, 1500), color="red")
plt.annotate("Modification factor = {:.0f}".format(x), (2000, 10), color="red")

# behaviour_law = reduction_factors * res.slope + res.intercept
# plt.plot(reduction_factors, behaviour_law, color="red")

plt.show()
