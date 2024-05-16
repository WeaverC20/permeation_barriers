import numpy as np
import festim as F

# taken from (Chen, 2021)
D_0_eurofer = 3.15e-08
E_D_eurofer = 0.0622


def festim_sim_permeation_barrier(
    L_eurofer=1e-05, PRF=1, T=600, results_folder="Results/", testing=False
):

    my_model = F.Simulation(log_level=40)

    # define mesh
    vertices = np.linspace(0, L_eurofer, num=100)
    my_model.mesh = F.MeshFromVertices(vertices=vertices)

    # define materials
    eurofer = F.Material(
        id=2,
        borders=[0, L_eurofer],
        D_0=D_0_eurofer,
        E_D=E_D_eurofer,
    )
    my_model.materials = F.Materials([eurofer])

    # define temperature
    my_model.T = F.Temperature(value=T)

    # define boundary conditions
    if PRF == 1:
        my_model.boundary_conditions = [
            F.DirichletBC(surfaces=1, value=1e20, field="solute"),
            F.RecombinationFlux(Kr_0=1.41e-26, E_Kr=0.257, order=2, surfaces=2),
        ]
    else:
        modified_kr_0 = PRF
        my_model.boundary_conditions = [
            F.DirichletBC(surfaces=1, value=1e20, field="solute"),
            F.RecombinationFlux(Kr_0=modified_kr_0, E_Kr=0, order=2, surfaces=2),
        ]

    # define settings
    my_model.settings = F.Settings(
        absolute_tolerance=1e10,
        relative_tolerance=1e-10,
        maximum_iterations=30,
        transient=False,
    )

    # define exports
    my_derived_quantities = F.DerivedQuantities(
        [F.SurfaceFlux("solute", surface=2)],
        filename=results_folder + "derived_quantities.csv",
    )
    my_model.exports = F.Exports([my_derived_quantities])

    # run simulation
    my_model.initialise()
    my_model.run()


if __name__ == "__main__":
    T = 600
    results_folder = "Results/recombination_testing/"

    # standard case
    festim_sim_permeation_barrier(
        T=T, PRF=1, results_folder=results_folder + "standard/"
    )

    # testing
    test_values = np.geomspace(1e-28, 1e-18, num=50)
    for value in test_values:
        print("testing PRF value = {:.2e}".format(value))
        testing_results_folder = results_folder + "modification={:.2e}/".format(value)
        festim_sim_permeation_barrier(
            T=T, PRF=value, results_folder=testing_results_folder, testing=True
        )

    # show correlation
    PRF_values = np.geomspace(1e0, 1e5, num=50)
    for PRF in PRF_values:
        PRF_value = 1e-28 / (PRF - 1e-05)
        testing_results_folder = results_folder + "prf={:.2e}/".format(PRF)
        festim_sim_permeation_barrier(
            T=T, PRF=PRF_value, results_folder=testing_results_folder
        )
