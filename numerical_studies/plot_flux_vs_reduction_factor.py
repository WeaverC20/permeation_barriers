import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import linregress

# plt.rc("text", usetex=True)
# plt.rc("font", family="serif", size=12)

grey_eurofer = (153 / 255, 153 / 255, 153 / 255)
green_lipb = (146 / 255, 196 / 255, 125 / 255)

# ##### Reduction factor 1 - 1000 (linear) ##### #

S_0_values = [2.4e23, 2.4e22, 2.4e21, 2.4e20, 2.4e19, 2.4e18, 2.4e17, 2.4e16]
S_0_ref = 2.4088e23
k_B = 8.6e-5
solubilities = np.array(S_0_values) * np.exp(-0.3026 / k_B / 600)
S_ref = S_0_ref * np.exp(-0.3026 / k_B / 600)


flux = []
folder = "Results/1D_results/reduction_factor/log_scale"
for S_0 in S_0_values:
    filename = folder + "/S_0_eur={:.1e}/derived_quantities.csv".format(S_0)
    data = np.genfromtxt(filename, delimiter=",", names=True)
    flux.append(data["Flux_surface_2_solute"])


plt.figure(figsize=[6.4, 3.8])
solubilities_normalised = S_ref / solubilities

x_annotation = solubilities_normalised[-1] * 1.02
flux_normalised = flux[0] / flux

plt.plot(
    solubilities_normalised,
    flux_normalised,
    label="BZ pipes",
    color=grey_eurofer,
    marker="+",
)

# plt.annotate(
#     "FW cooling \n channel", (x_annotation, (y_fw_cooling/y_fw_cooling[0])[-1]), color=grey_eurofer)

# res = linregress(solubilities_normalised, flux_normalised)
# behaviour_law = np.exp(res.intercept)*np.exp(solubilities_normalised*res.slope)
# print(res.rvalue**2)
# print(res.intercept)
# print(res.slope)
# print("Behaviour Law : {:.4e} exp ({:.4}*x)".format(np.exp(res.intercept), res.slope))


plt.yscale("log")
plt.xscale("log")
# plt.xlim(0, 1150)
plt.ylabel(r"PRF")
plt.xlabel(r"Reduction factor")

ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()

plt.show()
