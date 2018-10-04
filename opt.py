# -*- coding: utf-8 -*-

from libdalton import fileio
from libdalton import optimize


def run(input_file):
    optimization = optimize.Optimization(input_file)
    optimization.optimize()


if __name__ == '__main__':
    input_file_name = fileio.validate_input(__file__)
    run(input_file_name)
