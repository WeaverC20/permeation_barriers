import matplotlib.pyplot as plt
import numpy as np


T_400 = []
T_1200 = []

reduction_factors = [500, 1000]

results_folder = "Results/testing/"

standard_case_400 = results_folder + "T=400/PRF=1/derived_quantities.csv"
standard_data_400 = np.genfromtxt(standard_case_400, delimiter=",", names=True)
standard_flux_400 = standard_data_400["Flux_surface_2_solute"]

standard_case_1200 = results_folder + "T=1200/PRF=1/derived_quantities.csv"
standard_data_1200 = np.genfromtxt(standard_case_1200, delimiter=",", names=True)
standard_flux_1200 = standard_data_1200["Flux_surface_2_solute"]

for factor in reduction_factors:
    filename_data_400 = (
        results_folder + "T=400/PRF={:.0f}/derived_quantities.csv".format(factor)
    )
    data_400 = np.genfromtxt(filename_data_400, delimiter=",", names=True)
    T_400.append(data_400["Flux_surface_2_solute"])

    filename_data_1200 = (
        results_folder + "T=1200/PRF={:.0f}/derived_quantities.csv".format(factor)
    )
    data_1200 = np.genfromtxt(filename_data_1200, delimiter=",", names=True)
    T_1200.append(data_1200["Flux_surface_2_solute"])


T_400 = np.array(T_400)
T_1200 = np.array(T_1200)

normalised_fluxes_400 = standard_flux_400 / T_400
normalised_fluxes_1200 = standard_flux_1200 / T_1200


plt.figure()

plt.plot(reduction_factors, normalised_fluxes_400, label="T = 400")
plt.plot(reduction_factors, normalised_fluxes_1200, label="T = 1200")

plt.legend()


# res = linregress(solubilities_normalised, flux_normalised)
# behaviour_law = np.exp(res.intercept)*np.exp(solubilities_normalised*res.slope)
# print(res.rvalue**2)
# print(res.intercept)
# print(res.slope)
# print("Behaviour Law : {:.4e} exp ({:.4}*x)".format(np.exp(res.intercept), res.slope))


# plt.yscale("log")
# plt.xscale("log")
plt.ylabel(r"PRF")
plt.xlabel(r"Modification factor")

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()

plt.show()
