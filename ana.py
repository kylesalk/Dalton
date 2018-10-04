# -*- coding: utf-8 -*-

from libdalton import fileio
from libdalton import analyze


def run(input_file):
    """Run analysis on the input file using libdalton.analyze"""
    analysis = analyze.Analysis(input_file)
    analysis.run()


if __name__=='__main__':
    input_file_name = fileio.validate_input(__file__)
    run(input_file_name)
