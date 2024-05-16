import matplotlib.pyplot as plt
import numpy as np
import shutil
from matplotlib import cm, rcParams

rcParams["text.usetex"] = True if shutil.which("latex") else False

# with barrier
datafile_with_barrier = "Results/cartesian_reproduction/profiles/with_barrier.txt"
data_with_barrier = np.genfromtxt(datafile_with_barrier, delimiter=",", names=True)
solute_with_barrier = data_with_barrier["solute"]
x_values = data_with_barrier["arc_length"]
x_values *= 1e03

# without barrier
datafile_without_barrier = "Results/cartesian_reproduction/profiles/without_barrier.txt"
data_without_barrier = np.genfromtxt(
    datafile_without_barrier, delimiter=",", names=True
)
solute_without_barrier = data_without_barrier["solute"]


# with modification
datafile_with_modification = (
    "Results/cartesian_reproduction/profiles/with_modification.txt"
)
data_with_modification = np.genfromtxt(
    datafile_with_modification, delimiter=",", names=True
)
solute_with_modification = data_with_modification["solute"]

plt.figure()

plt.plot(x_values, solute_with_barrier, color="red", label="with barrier")
plt.plot(x_values, solute_without_barrier, color="black", label="without barrier")

plt.legend()
plt.yscale("log")
plt.ylabel(r"Solute concentration (Hm$^{-3}$)")
plt.xlabel(r"x (mm)")
plt.ylim(1e09, 1e19)
plt.xlim(0, 4)
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("Results/cartesian_reproduction/interface_condition_1.svg")


plt.figure()

plt.plot(x_values, solute_with_barrier, color="red", label="with barrier")
plt.plot(x_values, solute_without_barrier, color="black", label="without barrier")
plt.plot(
    x_values,
    solute_with_modification,
    color="grey",
    linestyle="dashed",
    label="modification",
)

plt.legend()
plt.yscale("log")
plt.ylabel(r"Solute concentration (Hm$^{-3}$)")
plt.xlabel(r"x (mm)")
plt.ylim(1e09, 1e19)
plt.xlim(0, 4)
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("Results/cartesian_reproduction/interface_condition_2.svg")

plt.figure()

plt.plot(x_values, solute_with_barrier, color="red", label="barrier")
plt.plot(x_values, solute_without_barrier, color="black", label="without barrier")

plt.legend()
plt.yscale("log")
plt.ylabel(r"Solute concentration (Hm$^{-3}$)")
plt.xlabel(r"x (mm)")
plt.ylim(1e011, 1e19)
e = 5e-03
xmin = 2 - 2 * e
xmax = 2 + 2 * e
plt.xlim(xmin, xmax)
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("Results/cartesian_reproduction/interface_condition_zoom_1.svg")


plt.figure()

plt.plot(x_values, solute_with_barrier, color="red", label="with barrier")
plt.plot(x_values, solute_without_barrier, color="black", label="without barrier")
plt.plot(
    x_values,
    solute_with_modification,
    color="grey",
    linestyle="dashed",
    label="with modification",
)

plt.legend()
plt.yscale("log")
plt.ylabel(r"Solute concentration (Hm$^{-3}$)")
plt.xlabel(r"x (mm)")
plt.ylim(1e011, 1e19)
e = 5e-03
xmin = 2 - 2 * e
xmax = 2 + 2 * e
plt.xlim(xmin, xmax)
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.savefig("Results/cartesian_reproduction/interface_condition_zoom_2.svg")


# plt.show()
