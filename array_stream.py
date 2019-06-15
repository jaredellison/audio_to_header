import sys

from sample_process import get_samples
import templates

# Get file name from command line input
in_file = sys.argv[1]
out_file = in_file.split(".")[0]

# C Header templates
params = {
    "header_file_name": out_file,
    "c_type": "uint8_t",
    "c_type_max": 255
}

top_template = f"""\
/** @file {out_file}.h
 *
 * @brief Audio file formatted as c style array.
 *
 */

#ifndef {params["header_file_name"].upper()}_H
#define {params["header_file_name"].upper()}_H

{params["c_type"]} sample = {{
    """

bottom_template = f"""
}};

#endif /* {params["header_file_name"].upper()}_H */

/*** end of file ***/
"""

# Process in_file
data = get_samples(in_file, params["c_type_max"])

# Open output file
out_file = open(out_file + '.h', 'w')

# Write top of header file
out_file.write(top_template)

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