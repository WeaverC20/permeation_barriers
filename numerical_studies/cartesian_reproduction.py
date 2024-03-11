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

# taken from
D_0_al2o3 = 7.35e-07  # Diffusivity coefficient pre-exponential factor
E_D_al2o3 = 1.899  # Diffusivity coefficient activation energy (eV)
S_0_al2o3 = 2.519e25  # Solubility coefficient pre-exponential factor
E_S_al2o3 = 0.902  # Solutbiility coefficient activation energy (eV)


def model_with_barrier():

    my_model = F.Simulation(log_level=40)

    # define mesh
    my_model.mesh = F.MeshFromVertices(vertices=np.linspace(0, 1.0e-5, num=1000))

    # define materials
    lipb = F.Material(
        id=1,
        borders=[0, 4.0e-06],
        D_0=1.0,
        E_D=0,
        S_0=1.0,
        E_S=0,
    )
    barrier = F.Material(
        id=2,
        borders=[4.0e-06, 6.0e-06],
        D_0=0.8,
        E_D=0,
        S_0=0.8,
        E_S=0,
    )
    eurofer = F.Material(
        id=3,
        borders=[6.0e-06, 1.0e-05],
        D_0=1.5,
        E_D=0,
        S_0=1.5,
        E_S=0,
    )
    my_model.materials = F.Materials([lipb, barrier, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=600)

    # define boundary conditions
    my_model.boundary_conditions = [
        F.DirichletBC(surfaces=1, value=1000, field="solute"),
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
    results_folder = "Results/cartesian_reproduction/with_barrier/"
    my_derived_quantities = F.DerivedQuantities(
        [
            F.TotalVolume("solute", volume=1),
            F.TotalVolume("solute", volume=2),
            F.TotalVolume("solute", volume=3),
            F.SurfaceFlux("solute", surface=2),
        ],
        filename=results_folder + "Derived_quantities.csv",
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


def model_without_barrier():

    my_model = F.Simulation(log_level=40)

    # define mesh
    my_model.mesh = F.MeshFromVertices(vertices=np.linspace(0, 1.0e-5, num=1000))

    # define materials
    lipb = F.Material(
        id=1,
        borders=[0, 5.0e-06],
        D_0=1.0,
        E_D=0,
        S_0=2.0,
        E_S=0,
    )
    eurofer = F.Material(
        id=2,
        borders=[5.0e-06, 1.0e-05],
        D_0=D_0_eurofer,
        E_D=E_D_eurofer,
        S_0=S_0_eurofer,
        E_S=E_S_eurofer,
    )
    my_model.materials = F.Materials([lipb, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=600)

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
    results_folder = "Results/cartesian_reproduction/without_barrier/"
    my_derived_quantities = F.DerivedQuantities(
        [
            F.TotalVolume("solute", volume=1),
            F.TotalVolume("solute", volume=2),
            F.SurfaceFlux("solute", surface=2),
        ],
        filename=results_folder + "Derived_quantities.csv",
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


model_with_barrier()
# model_without_barrier()
