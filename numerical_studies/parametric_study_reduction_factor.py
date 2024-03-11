from numerical_studies.festim_sim import my_model, eurofer
import festim as F
import numpy as np

S_0_eur_original = 2.4088e23
E_S_eurofer = 0.3026

reduction_factors = np.geomspace(1e0, 1e08, num=50)

folder = "Results/parametric_study/reduction_factor/"

for export in my_model.exports.exports:
    if isinstance(export, F.DerivedQuantities):
        export.filename = folder + "standard_case/derived_quantities.csv"
    elif isinstance(export, F.XDMFExport):
        export.folder = folder + "standard_case/"
        export.append = False
        export.define_xdmf_file()

my_model.initialise()
my_model.run()

for reduction_factor in reduction_factors:
    reduced_S_0_eurofer = S_0_eur_original / reduction_factor
    eurofer.S_0 = reduced_S_0_eurofer
    eurofer.E_S = E_S_eurofer

    results_folder = folder + "factor={:.1e}/".format(reduction_factor)

    for export in my_model.exports.exports:
        if isinstance(export, F.DerivedQuantities):
            export.filename = results_folder + "derived_quantities.csv"
        elif isinstance(export, F.XDMFExport):
            export.folder = results_folder
            export.append = False
            export.define_xdmf_file()

    print("Reduction factor ={:.1e}".format(reduction_factor))
    my_model.initialise()
    my_model.run()
