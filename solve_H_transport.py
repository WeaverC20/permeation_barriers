from fenics import *
from parameters import my_model


def run_H_transport():
    """Runs a hydrogen transport simulation"""

    my_model.initialise()
    my_model.run()


if __name__ == "__main__":
    run_H_transport()
