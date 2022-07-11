import numpy as np
import FESTIM as F
import properties

vertices = np.unique(
    np.concatenate([np.linspace(0, 10e-6, num=1990), np.linspace(10e-6, 20e-6, num=10)])
)

my_model = F.Simulation(log_level=30)

# define mesh
my_model.mesh = F.MeshFromVertices(vertices=vertices)

# define materials
lipb = F.Material(
    id=1,
    borders=[0, 10e-06],
    D_0=properties.D_0_lipb,
    E_D=properties.E_D_lipb,
    S_0=properties.S_0_lipb,
    E_S=properties.E_S_lipb,
)
eurofer = F.Material(
    id=2,
    borders=[10e-06, 20e-06],
    D_0=properties.D_0_eurofer,
    E_D=properties.E_D_eurofer,
    S_0=properties.S_0_eurofer,
    E_S=properties.E_S_eurofer,
)
my_model.materials = F.Materials([lipb, eurofer])

# define traps
# trap_1 = F.Trap(
#     k_0=5.22e-17, E_k=0.39, p_0=1e13 * 0, E_p=1.0, materials=eurofer, density=3
# )
# my_model.traps = F.Traps([trap_1])

# define temperature
my_model.T = F.Temperature(value=598.15)

# define boundary conditions
my_model.boundary_conditions = [
    F.DirichletBC(surfaces=[1], value=1e20),
    F.DirichletBC(surfaces=[2], value=0),
]

# define settings
my_model.dt = F.Stepsize(initial_value=100, stepsize_change_ratio=1.1, dt_min=1e-4)
my_model.settings = F.Settings(
    absolute_tolerance=1e10,
    relative_tolerance=1e-08,
    maximum_iterations=30,
    final_time=864000,
)

# define exports
my_derived_quantities = F.DerivedQuantities(filename="Results/derived_quantities.csv")

my_model.exports = F.Exports(
    [
        F.XDMFExport(
            "solute", label="solute", folder="Results", checkpoint=False, mode=1
        ),
        my_derived_quantities,
    ]
)


# run simulation

if __name__ == "__main__":
    my_model.initialise()
    my_model.run()
