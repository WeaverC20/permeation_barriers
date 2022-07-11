from parameters import parameters
from context import FESTIM
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
    1728
    ]

    folder = "Results/1D_results/reduction_factor/log_scale"
    E_S_eurofer = 0.3026
    for reduction_factor in reduction_factors:
        reduced_S_0_eurofer = S_0_eur_original/reduction_factor
        parameters["materials"][1]["S_0"] = reduced_S_0_eurofer
        parameters["materials"][1]["E_S"] = E_S_eurofer

        results_folder = folder + '/S_0_eur={:.1e}'.format(reduced_S_0_eurofer)

        parameters['exports']["xdmf"]["folder"] = results_folder
        parameters['exports']["derived_quantities"]["folder"] = results_folder
        print('Current step is S_0_eur = {:.1e}'.format(reduced_S_0_eurofer))
        run_H_transport(parameters, log_level=40)