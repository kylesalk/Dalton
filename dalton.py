# -*- coding: utf-8 -*-

"""CLI interface for the Dalton library

Usage:
    dalton.py -[mm|mc|md|ana|opt] <file>

Example:
    dalton.py -mm -mc file1.md file2.md
    (runs mm and mc on both .md files)
"""

import argparse
import os
from libdalton import analyze, simulate, molecule, optimize


def ana_run(files):
    for f in files:
        analysis = analyze.Analysis(f)
        analysis.run()


def md_run(files):
    for f in files:
        simulation = simulate.MolecularDynamics(f)
        simulation.run()


def mc_run(files):
    for f in files:
        simulation = simulate.MonteCarlo(f)
        simulation.run()


def mm_run(files):
    for f in files:
        mol = molecule.Molecule(f)

        mol.set_kinetic_calc_method('nokinetic')
        mol.set_gradient_calc_method('analytic')
        mol.get_energy()
        mol.get_gradient()

        mol.print_data()
        mol.print_gradient()


def opt_run(files):
    for f in files:
        optimization = optimize.Optimization(f)
        optimization.optimize()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ana", action="store_true", default=False,
                        help="Use ana to call the file")
    parser.add_argument("-mc", action="store_true", default=False,
                        help="Use mc to call the file")
    parser.add_argument("-md", action="store_true", default=False,
                        help="Use md to call the file")
    parser.add_argument("-mm", action="store_true", default=False,
                        help="Use mm to call the file")
    parser.add_argument("-opt", action="store_true", default=False,
                        help="Use opt to call the file")
    parser.add_argument("files", nargs="*")

    known, unknown = parser.parse_known_args()

    files = set()
    for fname in known.files:
        if os.path.isfile(fname):
            files.add(fname)
    if len(files) == 0:
        raise ValueError("Valid input file(s) required!")

    for key, val in vars(known).items():
        if key == "files":
            continue
        if not val:
            continue
        globals()["{}_run".format(key)](files)


if __name__ == "__main__":
    main()
