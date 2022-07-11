import sympy as sp
import numpy as np
from context import FESTIM
from FESTIM.generic_simulation import run
import properties

vertices = np.unique(
    np.concatenate([np.linspace(0, 10e-6, num=1990), np.linspace(10e-6, 20e-6, num=10)])
)

parameters = {
    "mesh_parameters": {"vertices": vertices},
    "materials": [
        {
            # LiPb
            "borders": [0, 10e-06],
            "D_0": properties.D_0_lipb,
            "E_D": properties.E_D_lipb,
            "S_0": properties.S_0_lipb,
            "E_S": properties.E_S_lipb,
            "id": 1,
        },
        {
            # EUROfer
            "borders": [10e-06, 20e-06],
            "D_0": properties.D_0_eurofer,
            "E_D": properties.E_D_eurofer,
            "S_0": properties.S_0_eurofer * (1 / 1e2),
            "E_S": properties.E_S_eurofer,
            "id": 2,
        },
    ],
    "traps": [],
    "temperature": {
        "type": "expression",
        "value": 598.15,
    },
    "boundary_conditions": [
        {"type": "dc", "value": 1e20, "surfaces": 1},
        {"type": "dc", "value": 0, "surfaces": 2},
    ],
    "solving_parameters": {
        "type": "solve_stationary",
        "final_time": 864000,
        "initial_stepsize": 100,
        "adaptive_stepsize": {
            "stepsize_change_ratio": 1.1,
            "t_stop": 1e618,
            "stepsize_stop_max": 1 / 10,
            "dt_min": 1e-4,
        },
        "newton_solver": {
            "absolute_tolerance": 1e10,
            "relative_tolerance": 1e-8,
            "maximum_iterations": 50,
        },
        "traps_element_type": "DG",
    },
    "exports": {
        "xdmf": {
            "functions": ["solute"],
            "labels": ["solute"],
            "folder": "Results/1D_Results/reduction_factor/rf_100",
            "nb_iterations_between_exports": 1,
            # "last_timestep_only": True
            "checkpoint": False,
        },
        "derived_quantities": {
            "total_volume": [
                {"volumes": [1, 2], "field": "solute"},
            ],
            "surface_flux": [{"surfaces": [2], "field": "solute"}],
            "file": "derived_quantities.csv",
            "folder": "Results/1D_Results",
            "nb_iterations_between_exports": 1,
        },
    },
}
