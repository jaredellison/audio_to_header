#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    File name: aiff_to_header.py
    Author: Jared Ellison
    Date created: June 2019
    Python Version: 3.7.3
'''
import sys

from sample_process import get_samples

########################################
#  Configuration

# Get file name from command line input
in_file = sys.argv[1]
out_file = in_file.split(".")[0]

# For c type reference see
# https://en.cppreference.com/w/c/types/integer
params = {
    "header_file_name": out_file,
    "c_type": "uint8_t",
    "c_type_max": 255
}

########################################
#  Template Strings

top_template = f"""\
/** @file {out_file}.h
 *
 * @brief Audio file formatted as c style array.
 *
 */

#ifndef {params["header_file_name"].upper()}_H
#define {params["header_file_name"].upper()}_H

int {params["header_file_name"]}_LENGTH = %d;

{params["c_type"]} {params["header_file_name"]} [] = {{
    """

bottom_template = f"""
}};

#endif /* {params["header_file_name"].upper()}_H */

/*** end of file ***/
"""

########################################
#  Sample Processing

if __name__ == "__main__":
    # Process in_file
    data, sample_count = get_samples(in_file, params["c_type_max"])

    # Open output file
    out_file = open(out_file + '.h', 'w')

    # Write top of header file
    out_file.write(top_template % sample_count)

    cols = 16
    col = 0

    # Write data
    for d in data[:-1]:
        col = col + 1
        out_file.write(f"{d}, ")
        if (col % cols == 0):
            out_file.write(f"\n    ")

    # No trailing comma for last line
    out_file.write(f"{data[-1]}")

    # Write end of header file
    out_file.write(bottom_template)

    out_file.close()
