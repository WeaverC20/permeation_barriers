from festim_sim import festim_sim_permeation_barrier
import numpy as np

reduction_factors = np.geomspace(1e0, 1e08, num=50)

folder = "Results/parametric_study/length_change/"

lengths = np.geomspace(1e-02, 1e-06, num=10)

for length in lengths:
    for reduction_factor in reduction_factors:

        print("running case L={:.1e}m, prf={:.1e}/".format(length, reduction_factor))

        results_folder = folder + "L={:.1e}m/prf={:.1e}/".format(
            length, reduction_factor
        )

        festim_sim_permeation_barrier(
            PRF=reduction_factor, T=600, results_folder=results_folder, L_lipb=length
        )

    print("running case L={:.1e}m, prf=1/".format(length))

    results_folder = folder + "L={:.1e}m/prf=1/".format(length)
    festim_sim_permeation_barrier(
        PRF=1, T=600, results_folder=results_folder, L_lipb=length
    )
# # standard case
# results_folder = folder + "prf=1/"

# festim_sim_permeation_barrier(PRF=1, T=600, results_folder=results_folder)
