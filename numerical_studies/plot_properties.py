import matplotlib.pyplot as plt
import numpy as np
import festim as F


# taken from (Aiello, 2008)
S_0_lipb = 1.427214e23
E_S_lipb = 0.133

# taken from (Chen, 2021)
S_0_eurofer = 2.4088e23
E_S_eurofer = 0.3026

# taken from
S_0_al = 9.133e19  # Solubility coefficient pre-exponential factor
E_S_al = 0.234  # Solutbiility coefficient activation energy (eV)


def solutbility(S_0, E_S, T):
    return S_0 * np.exp(-E_S / F.k_B / T)


T = np.linspace(300, 1000, num=1000)

solutbility_lipb = solutbility(S_0_lipb, E_S_lipb, T)
solutbility_eurofer = solutbility(S_0_eurofer, E_S_eurofer, T)
solutbility_al = solutbility(S_0_al, E_S_al, T)

# eurofer/lipb
s_comp_eurofer_lipb = solutbility_eurofer / solutbility_lipb
ref_600K = solutbility(S_0_eurofer, E_S_eurofer, 600) / solutbility(
    S_0_lipb, E_S_lipb, 600
)
normalised_s_comp_eurofer_lipb = s_comp_eurofer_lipb / ref_600K


plt.figure()
plt.plot(1 / T, solutbility_lipb, label="LiPb")
plt.plot(1 / T, solutbility_eurofer, label="Eurofer")
plt.plot(1 / T, solutbility_al, label="Al")
plt.legend()
plt.yscale("log")

# plt.figure()
# plt.plot(T, s_comp_eurofer_lipb)

plt.figure()
plt.plot(T, normalised_s_comp_eurofer_lipb)

plt.show()
