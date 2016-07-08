# -*- coding: utf-8 -*-
""" Analyze

Main script.
Define some global matplotlib style.
Load the data and then run the modules who produce the plots.

"""
from __future__ import unicode_literals

import argparse
import os



import sfbistats.analysis.time_series as sfbi_time_series
import sfbistats.analysis.summary as sfbi_summary
import sfbistats.analysis.global_lins as sfbi_global_lins
import sfbistats.analysis.lexical_analysis as sfbi_lexical_analysis
import sfbistats.analysis.maps as sfbi_maps
import utils

if __name__ == '__main__':

    # parse and check arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--json', required=True, type=file)
    argparser.add_argument('--output_dir', required=True)
    args = vars(argparser.parse_args())
    input_file = args['json']
    output_dir = args['output_dir']
    if not os.path.exists(output_dir):
        raise ValueError('output_dir argument ' + str(output_dir)+' does not exist.')
    if not os.path.isdir(output_dir):
        raise ValueError('output_dir argument ' + str(output_dir)+' is not a directory.')
    output_dir = os.path.abspath(output_dir)
    print str(input_file)+' '+output_dir

    # load the data
    job_list = utils.load_from_json(input_file)

    # run the scripts
    sfbi_summary.run(job_list, output_dir)
    sfbi_global_lins.run(job_list, output_dir)
    sfbi_lexical_analysis.run(job_list, output_dir)
    sfbi_time_series.run(job_list, output_dir)
    sfbi_maps.run(job_list, output_dir)

    print ("Complete")
