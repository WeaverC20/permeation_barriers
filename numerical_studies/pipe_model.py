import festim as F
import h_transport_materials as htm


id_lipb = 6
id_eurofer = 7
id_outer_boundary = 8
id_inner_boundary = 9

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


def festim_sim(PRF=1, results_folder="Results/"):

    my_model = F.Simulation(log_level=20)

    # define mesh
    my_model.mesh = F.MeshFromXDMF(
        boundary_file="mesh/mesh_boundaries.xdmf", volume_file="mesh/mesh_domains.xdmf"
    )

    # define materials
    lipb = F.Material(
        id=id_lipb,
        D_0=D_pbli.pre_exp.magnitude,
        E_D=D_pbli.act_energy.magnitude,
        S_0=S_pbli.pre_exp.magnitude,
        E_S=S_pbli.act_energy.magnitude,
    )
    eurofer = F.Material(
        id=id_eurofer,
        D_0=D_eurofer.pre_exp.magnitude,
        E_D=D_eurofer.act_energy.magnitude,
        S_0=S_eurofer.pre_exp.magnitude,
        E_S=S_eurofer.act_energy.magnitude,
    )
    my_model.materials = F.Materials([lipb, eurofer])

    # define temperature
    my_model.T = F.Temperature(value=800)

    # define boundary conditions
    if PRF == 1:
        my_model.boundary_conditions = [
            F.DirichletBC(value=1e20, field="solute", surfaces=id_outer_boundary),
            F.RecombinationFlux(
                Kr_0=4.28e-32, E_Kr=0.25, order=2, surfaces=id_inner_boundary
            ),
            # F.DirichletBC(value=0, field="solute", surfaces=id_inner_boundary),
        ]
    else:
        modified_kr_0 = 4.28e-32 / PRF
        my_model.boundary_conditions = [
            F.DirichletBC(value=1e20, field="solute", surfaces=id_outer_boundary),
            F.RecombinationFlux(
                Kr_0=modified_kr_0, E_Kr=0.25, order=2, surfaces=id_inner_boundary
            ),
        ]

    # my_model.dt = F.Stepsize(
    #     initial_value=10,
    #     stepsize_change_ratio=1.1,
    # )
    # define settings
    my_model.settings = F.Settings(
        final_time=24 * 3600 * 2,
        absolute_tolerance=1e-10,
        relative_tolerance=1e-14,
        maximum_iterations=30,
        transient=False,
        chemical_pot=True,
    )

    # define exports
    my_derived_quantities = F.DerivedQuantities(
        [F.SurfaceFlux("solute", surface=id_inner_boundary)],
        filename=results_folder + "derived_quantities.csv",
    )
    my_model.exports = F.Exports(
        [
            F.XDMFExport(
                "solute",
                label="solute",
                folder=results_folder,
                mode=1,
            ),
            my_derived_quantities,
        ]
    )

    # run simulation
    my_model.initialise()
    my_model.run()


if __name__ == "__main__":

    # standard case
    festim_sim(PRF=1, results_folder="Results/pipe_model/standard/")
    # PRF = 1000
    festim_sim(PRF=1000, results_folder="Results/pipe_model/PRF=1000/")
    print("Simulation completed")
