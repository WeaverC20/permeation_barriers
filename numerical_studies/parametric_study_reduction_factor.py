from festim_sim import festim_sim_permeation_barrier
import numpy as np

reduction_factors = np.geomspace(1e0, 1e08, num=50)

folder = "Results/parametric_study/reduction_factor/"


for reduction_factor in reduction_factors:

    results_folder = folder + "prf={:.1e}/".format(reduction_factor)

    festim_sim_permeation_barrier(
        PRF=reduction_factor, T=600, results_folder=results_folder
    )

# standard case
results_folder = folder + "prf=1/"

festim_sim_permeation_barrier(PRF=1, T=600, results_folder=results_folder)
