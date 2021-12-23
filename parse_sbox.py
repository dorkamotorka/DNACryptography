#!/usr/bin/env python
import encrypt
transcribe = {
    '0': 'AA',
    '1': 'AG',
    '2': 'AC',
    '3': 'AT',
    '4': 'GA',
    '5': 'GG',
    '6': 'GC',
    '7': 'GT',
    '8': 'CA',
    '9': 'CG',
    'a': 'CC',
    'b': 'CT',
    'c': 'TA',
    'd': 'TC',
    'e': 'TG',
    'f': 'TT',
}

# inverse_sbox = {}
# with open("inverse_sbox.txt") as f:
#     first_line = next(f).split()
#     first_line_transcribed = []
#     for char in first_line[1:]:
#         first_line_transcribed.append(transcribe[char[1]])
#     for i, line in enumerate(f):
#         beginning_char = transcribe[line[0][0]]
#         line_dict = {}
#         for k, char in enumerate(first_line_transcribed):
#             transcribed1 = transcribe[line.split()[k + 2][0]]
#             transcribed2 = transcribe[line.split()[k + 2][1]]
#             line_dict[char] = transcribed1 + transcribed2
#         inverse_sbox[beginning_char] = line_dict

sbox = {}
with open("sbox.txt") as f:
    first_line = next(f).split()
    first_line_transcribed = []
    for char in first_line:
        first_line_transcribed.append(transcribe[char[1]])

    for i, line in enumerate(f):
        beginning_char = transcribe[line[0][0]]
        line_dict = {}
        for k, char in enumerate(first_line_transcribed):
            transcribed1 = transcribe[line.split()[k + 1][0]]
            transcribed2 = transcribe[line.split()[k + 1][1]]
            line_dict[char] = transcribed1 + transcribed2
        sbox[beginning_char] = line_dict


def test(s_box):
    try:
        if s_box['TC']['CC'] == 'GTCC':
            print("Pass boy")
        else:
            print("Failed :(")
    except:
        print("Failed hard")

s_box_test = {
    'TC': {
        'CC': 'GTCC',
    }
}

import json
print(json.dumps(sbox, indent=4))

for key in sbox:
    print(sbox[key] == encrypt.sbox[key])

