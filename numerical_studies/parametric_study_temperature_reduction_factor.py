from festim_sim import festim_sim_permeation_barrier
import numpy as np

reduction_factors = np.geomspace(1e2, 1e04, num=10)
temperature_values = [400, 600, 800, 1000, 1200]

folder = "Results/parametric_study/"

for T in temperature_values:
    for reduction_factor in reduction_factors:

        results_folder = folder + "T={:.0f}/factor={:.1e}/".format(T, reduction_factor)

        festim_sim_permeation_barrier(
            PRF=reduction_factor, T=T, results_folder=results_folder
        )


for T in temperature_values:

    results_folder = folder + "T={:.0f}/factor=1/".format(T, reduction_factor)

    festim_sim_permeation_barrier(PRF=1, T=T, results_folder=results_folder)
