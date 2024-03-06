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

my_model = F.Simulation(log_level=40)

# define mesh
vertices = np.unique(
    np.concatenate([np.linspace(0, 1e-5, num=100), np.linspace(1e-5, 2e-5, num=100)])
)
my_model.mesh = F.MeshFromVertices(vertices=vertices)

# define materials
lipb = F.Material(
    id=1,
    borders=[0, 1e-05],
    D_0=D_0_lipb,
    E_D=E_D_lipb,
    S_0=S_0_lipb,
    E_S=E_S_lipb,
)
eurofer = F.Material(
    id=2,
    borders=[1e-05, 2e-05],
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
my_derived_quantities = F.DerivedQuantities(
    [
        F.TotalVolume("solute", volume=1),
        F.TotalVolume("solute", volume=2),
        F.SurfaceFlux("solute", surface=2),
    ],
    filename="Results/parametric_study/standard/derived_quantities.csv",
)
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
