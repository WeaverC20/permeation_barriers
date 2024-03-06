from parameters import my_model, eurofer
import festim as F
import numpy as np

S_0_eur_original = 2.4088e23

reduction_factors = np.geomspace(1e2, 1e04, num=10)
temperature_values = [400, 500, 600, 700]

folder = "Results/parametric_study/"

for T in temperature_values:
    # standard case

    E_S_eurofer = 0.3026

    for reduction_factor in reduction_factors:
        reduced_S_0_eurofer = S_0_eur_original / reduction_factor
        eurofer.S_0 = reduced_S_0_eurofer
        eurofer.E_S = E_S_eurofer

        results_folder = folder + "T={:.0f}/factor={:.0e}/".format(T, reduction_factor)

        for export in my_model.exports.exports:
            if isinstance(export, F.DerivedQuantities):
                export.filename = results_folder + "derived_quantities.csv"
            elif isinstance(export, F.XDMFExport):
                export.folder = results_folder
                export.append = False
                export.define_xdmf_file()

        my_model.T = F.Temperature(value=T)
        print("Current case: T = {}, reduction factor ={}".format(T, reduction_factor))
        my_model.initialise()
        my_model.run()
