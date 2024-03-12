import numpy as np
import festim as F

# taken from (Reiter, 1990)
D_0_lipb = 4.03e-08
E_D_lipb = 0.2021

# taken from (Aiello, 2008)
S_0_lipb = 1.427214e23
E_S_lipb = 0.133

# taken from (Chen, 2021)
D_0_eurofer = 3.15e-08
E_D_eurofer = 0.0622
S_0_eurofer = 2.4088e23
E_S_eurofer = 0.3026


def festim_sim_permeation_barrier(
    L_eurofer=1e-05, L_lipb=1e-05, PRF=1, T=600, results_folder="Results/"
):

    my_model = F.Simulation(log_level=40)

    # define mesh
    if L_eurofer < L_lipb:
        dx = L_eurofer / 100
    else:
        dx = L_lipb / 100
    size = L_eurofer + L_lipb
    cells_required = int(size / dx)
    vertices = np.linspace(0, size, num=cells_required)
    my_model.mesh = F.MeshFromVertices(vertices=vertices)

    # define materials
    lipb = F.Material(
        id=1,
        borders=[0, L_lipb],
        D_0=D_0_lipb,
        E_D=E_D_lipb,
        S_0=S_0_lipb,
        E_S=E_S_lipb,
    )
    eurofer = F.Material(
        id=2,
        borders=[L_lipb, size],
        D_0=D_0_eurofer,
        E_D=E_D_eurofer,
        S_0=S_0_eurofer / PRF,
        E_S=E_S_eurofer,
    )
    my_model.materials = F.Materials([lipb, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=T)

    # define boundary conditions
    my_model.boundary_conditions = [
        F.DirichletBC(surfaces=1, value=1e20, field="solute"),
        F.DirichletBC(surfaces=2, value=0, field="solute"),
    ]

    # define settings
    my_model.settings = F.Settings(
        absolute_tolerance=1e10,
        relative_tolerance=1e-10,
        maximum_iterations=30,
        transient=False,
        chemical_pot=True,
    )

    # define exports
    my_derived_quantities = F.DerivedQuantities(
        [
            F.TotalVolume("solute", volume=1),
            F.TotalVolume("solute", volume=2),
            F.SurfaceFlux("solute", surface=2),
        ],
        filename=results_folder + "derived_quantities.csv",
    )
    my_model.exports = F.Exports(
        [
            F.XDMFExport(
                "solute",
                label="solute",
                folder=results_folder,
                checkpoint=False,
                mode=1,
            ),
            my_derived_quantities,
        ]
    )

    # run simulation
    my_model.initialise()
    my_model.run()


if __name__ == "__main__":
    PRF = 500
    T = 400
    results_folder = "Results/testing/T=400/PRF=500/"
    festim_sim_permeation_barrier(PRF, T, results_folder)
    print("Simulation completed")
