import numpy as np
import festim as F
import h_transport_materials as htm


# Al2O3 properties
diffusivity_al2o3 = (
    htm.diffusivities.filter(material="alumina")
    .filter(isotope="h")
    .filter(author="serra")
)
D_al2o3 = diffusivity_al2o3[0]
solubility_al2o3 = (
    htm.solubilities.filter(material="alumina")
    .filter(isotope="h")
    .filter(author="serra")
)
S_al2o3 = solubility_al2o3[0]

# PbLi properties
diffusivity_pbli = (
    htm.diffusivities.filter(material="lipb")
    .filter(isotope="h")
    .filter(author="reiter")
)
D_pbli = diffusivity_pbli[0]
solubility_pbli = (
    htm.solubilities.filter(material="lipb").filter(isotope="h").filter(author="aiello")
)
S_pbli = solubility_pbli[0]


# eurofer properties
diffusivity_eurofer = htm.diffusivities.filter(material="eurofer_97").filter(
    author="chen"
)
D_eurofer = diffusivity_eurofer[0]

solubility_eurofer = htm.solubilities.filter(material="eurofer_97").filter(
    author="chen"
)
S_eurofer = solubility_eurofer[0]


def model_with_barrier():

    my_model = F.Simulation(log_level=40)

    # define mesh
    dx = 5e-08
    size = 4e-03
    cells_required = size / dx
    my_model.mesh = F.MeshFromVertices(
        vertices=np.linspace(0, size, num=int(cells_required))
    )

    e = 2.5e-06
    L = 2e-03
    # define materials
    lipb = F.Material(
        id=1,
        borders=[0, L - e],
        D_0=D_pbli.pre_exp.magnitude,
        E_D=D_pbli.act_energy.magnitude,
        S_0=S_pbli.pre_exp.magnitude,
        E_S=S_pbli.act_energy.magnitude,
    )
    barrier = F.Material(
        id=2,
        borders=[L - e, L + e],
        D_0=D_al2o3.pre_exp.magnitude,
        E_D=D_al2o3.act_energy.magnitude,
        S_0=S_al2o3.pre_exp.magnitude,
        E_S=S_al2o3.act_energy.magnitude,
    )
    eurofer = F.Material(
        id=3,
        borders=[L + e, 2 * L],
        D_0=D_eurofer.pre_exp.magnitude,
        E_D=D_eurofer.act_energy.magnitude,
        S_0=S_eurofer.pre_exp.magnitude,
        E_S=S_eurofer.act_energy.magnitude,
    )
    my_model.materials = F.Materials([lipb, barrier, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=600)

    # define boundary conditions
    my_model.boundary_conditions = [
        F.DirichletBC(surfaces=1, value=1e18, field="solute"),
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


def model_without_barrier():

    my_model = F.Simulation(log_level=40)

    # define mesh
    dx = 5e-08
    size = 4e-03
    cells_required = size / dx
    my_model.mesh = F.MeshFromVertices(
        vertices=np.linspace(0, size, num=int(cells_required))
    )

    # define materials
    lipb = F.Material(
        id=1,
        borders=[0, 2e-03],
        D_0=D_pbli.pre_exp.magnitude,
        E_D=D_pbli.act_energy.magnitude,
        S_0=S_pbli.pre_exp.magnitude,
        E_S=S_pbli.act_energy.magnitude,
    )
    eurofer = F.Material(
        id=2,
        borders=[2e-03, 4e-03],
        D_0=D_eurofer.pre_exp.magnitude,
        E_D=D_eurofer.act_energy.magnitude,
        S_0=S_eurofer.pre_exp.magnitude,
        E_S=S_eurofer.act_energy.magnitude,
    )
    my_model.materials = F.Materials([lipb, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=600)

    # define boundary conditions
    my_model.boundary_conditions = [
        F.DirichletBC(surfaces=1, value=1e18, field="solute"),
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


def model_with_modification(PRF=1000):

    my_model = F.Simulation(log_level=40)

    # define mesh
    dx = 5e-08
    size = 4e-03
    cells_required = size / dx
    my_model.mesh = F.MeshFromVertices(
        vertices=np.linspace(0, size, num=int(cells_required))
    )

    # define materials
    lipb = F.Material(
        id=1,
        borders=[0, 2e-03],
        D_0=D_pbli.pre_exp.magnitude,
        E_D=D_pbli.act_energy.magnitude,
        S_0=S_pbli.pre_exp.magnitude,
        E_S=S_pbli.act_energy.magnitude,
    )
    eurofer = F.Material(
        id=2,
        borders=[2e-03, 4e-03],
        D_0=D_eurofer.pre_exp.magnitude,
        E_D=D_eurofer.act_energy.magnitude,
        S_0=S_eurofer.pre_exp.magnitude / PRF,
        E_S=S_eurofer.act_energy.magnitude,
    )
    my_model.materials = F.Materials([lipb, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=600)

    # define boundary conditions
    my_model.boundary_conditions = [
        F.DirichletBC(surfaces=1, value=1e18, field="solute"),
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
    results_folder = "Results/cartesian_reproduction/with_modification/"
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


# model_with_barrier()
# model_without_barrier()
model_with_modification(PRF=3.85e4)
