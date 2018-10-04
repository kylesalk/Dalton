# -*- coding: utf-8 -*-

from libdalton import fileio
from libdalton import molecule


def run(input_file):
    molecule = molecule.Molecule(input_file)

    molecule.set_kinetic_calc_method('nokinetic')
    molecule.set_gradient_calc_method('analytic')
    molecule.get_energy()
    molecule.get_gradient()

    molecule.print_data()
    molecule.print_gradient()


if __name__ == '__main__':
    input_file_name = fileio.validate_input(__file__)
    run(input_file_name)
