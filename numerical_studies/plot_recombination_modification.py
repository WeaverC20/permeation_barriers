import matplotlib.pyplot as plt
import numpy as np

test_values = np.geomspace(1e-28, 1e-18, num=50)
prf_values = np.geomspace(1e0, 1e5, num=50)
results_folder = "Results/recombination_testing/"

standard_case = results_folder + "standard/derived_quantities.csv"
standard_data = np.genfromtxt(standard_case, delimiter=",", names=True)
standard_flux = standard_data["Flux_surface_2_solute"] * -1

testing_modified_fluxes = []
for value in test_values:
    filename_data = (
        results_folder + "modification={:.2e}/derived_quantities.csv".format(value)
    )
    data = np.genfromtxt(filename_data, delimiter=",", names=True)
    testing_modified_fluxes.append(data["Flux_surface_2_solute"] * -1)

testing_modified_fluxes = np.array(testing_modified_fluxes)
testing_PRF = standard_flux / testing_modified_fluxes

modified_fluxes = []
for value in prf_values:
    filename_data = results_folder + "prf={:.2e}/derived_quantities.csv".format(value)
    data = np.genfromtxt(filename_data, delimiter=",", names=True)
    modified_fluxes.append(data["Flux_surface_2_solute"] * -1)

modified_fluxes = np.array(modified_fluxes)
PRF = standard_flux / modified_fluxes

# for i in PRF:
#     print(i)
# print("...")
# for i in test_values:
#     print(i)
# quit()

test_x = (1e-28 / test_values) + 1e-05

# plt.figure()
# plt.plot(test_values, testing_PRF, color="black")
# plt.plot(test_values, test_x, color="red")
# plt.yscale("log")
# plt.xscale("log")
# plt.ylabel(r"PRF")
# plt.xlabel(r"Modification factor")
# ax = plt.gca()
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
# plt.tight_layout()


plt.figure()
plt.plot(prf_values, PRF, color="black")
plt.yscale("log")
plt.xscale("log")
plt.ylabel(r"PRF")
plt.xlim(1e00, 1e05)
# plt.ylim(1e00, 1e05)
plt.xlabel(r"Input PRF")
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.grid()

plt.show()
