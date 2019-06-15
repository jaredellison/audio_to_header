import sys

import normalize

in_file = sys.argv[1]

def write_from_template(file_path):
    template = open(file_path, "r")
    for line in template:
        sys.stdout.write(line)
    template.close()

data = normalize.get_processed_data(in_file)

write_from_template("./templates/header_template_pt1.h")

cols = 16
col = 0

for d in data[:-1]:
    col = col + 1
    sys.stdout.write(f"{d:>3}, ")
    if (col % cols == 0):
        sys.stdout.write(f"\n    ")

# No trailing comma for last line
sys.stdout.write(f"{data[-1]}")

write_from_template("./templates/header_template_pt2.h")
