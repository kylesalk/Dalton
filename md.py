# -*- coding: utf-8 -*-

from libdalton import fileio
from libdalton import simulate


def run(input_file):
    simulation = simulate.MolecularDynamics(input_file)
    simulation.run()


if __name__ == '__main__':
    input_file_name = fileio.validate_input(__file__)
    run(input_file_name)
