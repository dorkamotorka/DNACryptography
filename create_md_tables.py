#!/usr/bin/env python

import parse_sbox
from tomark import Tomark

def transform_to_list(box,first_line):
    list_dicts = []
    for i, key in enumerate(box):
        new_dict = {}
        new_dict[' '] = first_line[i]
        nnew_dict = {**new_dict, **box[key]}
        list_dicts.append(nnew_dict)
    return list_dicts

list_sbox = transform_to_list(parse_sbox.sbox, parse_sbox.first_line_transcribed_sbox)
list_inverse_sbox = transform_to_list(parse_sbox.inverse_sbox, parse_sbox.first_line_transcribed_inverse_sbox)

markdown_sbox = Tomark.table(list_sbox)
markdown_inverse_sbox = Tomark.table(list_inverse_sbox)
with open("s_tables.md", 'w') as f:
    f.write("### Rijandel S-Škatla\n")
    f.write(markdown_sbox)
    f.write("\n\n\n")
    f.write("### Inverzna Rijandel S-Škatla\n")
    f.write(markdown_inverse_sbox)
