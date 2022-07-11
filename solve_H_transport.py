from fenics import *
import os, sys, inspect
import sympy as sp
import numpy as np
from context import FESTIM

from parameters import parameters


def run_H_transport(parameters, log_level=20):
    """Runs a hydrogen transport simulation 
    Args:
        parameters ([type]): [description]
        S_0_lipb (float, optional): pre-exponential factor of solubility in
            LiPb. Defaults to S_0_lipb.
        E_S_lipb (float, optional): activation energy of solubility in LiPb.
            Defaults to E_S_lipb.
        log_level (int, optional): [description]. Defaults to 20.
    Returns:
        [type]: [description]
    """
    # create a simulation with these normal parameters
    my_sim = FESTIM.Simulation(parameters, log_level=log_level)
    my_sim.initialise()

    return my_sim.run()


if __name__ == "__main__":
    run_H_transport(parameters)