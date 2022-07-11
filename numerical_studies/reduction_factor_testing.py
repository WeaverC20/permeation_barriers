from parameters import my_model, eurofer
import FESTIM as F
from solve_H_transport import run_H_transport

if __name__ == "__main__":

    S_0_eur_original = 2.4088e23

    reduction_factors = [
        1e0,
        # 2.5e0,
        # 5e0,
        # 7.5e0,
        1e1,
        1e2,
        1e3,
        1e4,
        1e5,
        1e6,
        1e7,
        1728,
    ]

    folder = "Results/1D_results/reduction_factor/log_scale"
    E_S_eurofer = 0.3026
    for reduction_factor in reduction_factors:
        reduced_S_0_eurofer = S_0_eur_original / reduction_factor
        eurofer.S_0 = reduced_S_0_eurofer
        eurofer.E_S = E_S_eurofer

        results_folder = folder + "/S_0_eur={:.1e}/".format(reduced_S_0_eurofer)

        for export in my_model.exports.exports:
            if isinstance(export, F.DerivedQuantities):
                export.filename = results_folder + "derived_quantities.csv"
            elif isinstance(export, F.XDMFExport):
                export.folder = results_folder
                export.append = False
                export.define_xdmf_file()

        print("Current step is S_0_eur = {:.1e}".format(reduced_S_0_eurofer))
        run_H_transport(my_model)
