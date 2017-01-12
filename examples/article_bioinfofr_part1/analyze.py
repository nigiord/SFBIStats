# -*- coding: utf-8 -*-
""" Analyze

Main script.
Define some global matplotlib style.
Load the data and then run the modules who produce the plots.

"""
from __future__ import unicode_literals, print_function

import argparse
import os

from sfbistats import utils
import global_lins

if __name__ == '__main__':
    # parse and check arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--json', required=True, type=open)
    argparser.add_argument('--output_dir', required=True)
    args = vars(argparser.parse_args())
    input_file = args['json']
    output_dir = args['output_dir']
    if not os.path.exists(output_dir):
        raise ValueError('output_dir argument ' + str(output_dir)+' does not exist.')
    if not os.path.isdir(output_dir):
        raise ValueError('output_dir argument ' + str(output_dir)+' is not a directory.')
    output_dir = os.path.abspath(output_dir)

    print("Loading and sanitizing data...")
    # load the data
    job_list = utils.load_from_json(input_file)

    # run the scripts
    global_lins.run(job_list, output_dir)
    print ("Complete")
