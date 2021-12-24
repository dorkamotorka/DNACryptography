#!/usr/bin/env python

import parse_sbox
import random

inv_he = {
    'GC': 'a',
    'TTA': 'b',
    'GGA': 'c',
    'TC': 'd',
    'C': 'e',
    'GTA': 'f',
    'GTC': 'g',
    'TG': 'h',
    'AA': 'i',
    'TTTA': 'j',
    'GTT': 'y',
    'TTTG': 'k',
    'GGG': 'l',
    'GTG': 'm',
    'GGC': 'w',
    'AT': 'n',
    'AG': 'o',
    'TTG': 'p',
    'TA': 'r',
    'GA': 't',
    'TTTCG': 'q',
    'AC': 's',
    'GGT': 'u',
    'TTC': 'v',
    'TTTCA': 'z',
    'TTTT': 'x',
}

def decode_from_blocks(blocks):
    decoded = []
    for b in blocks:
        for k in sorted(inv_he, key=len, reverse=True):
            b = b.replace(k, inv_he[k])
        decoded.append(b)

    return decoded


inverse_sbox = parse_sbox.inverse_sbox
# DNA base to binary
binary = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11',
}

# Binary to DNA
dnab = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T',
}

# Timin v Uracil, ostalo enako
inv_mRNA = {
    'G': 'G',
    'C': 'C',
    'U': 'T',
    'A': 'A',
}

# komplementi baz
inv_tRNA = {
    'C': 'G',
    'G': 'C',
    'U': 'A',
    'A': 'U',
}

inv_permute = {
    1 : 40,
    2 : 8,
    3 : 48,
    4 : 16,
    5 : 56,
    6 : 24,
    7 : 64,
    8 : 32,
    9 : 39,
    10 : 7,
    11 : 47,
    12 : 15,
    13 : 55,
    14 : 23,
    15 : 63,
    16 : 31,
    17 : 38,
    18 : 6,
    19 : 46,
    20 : 14,
    21 : 54,
    22 : 22,
    23 : 62,
    24 : 30,
    25 : 37,
    26 : 5,
    27 : 45,
    28 : 13,
    29 : 53,
    30 : 21,
    31 : 61,
    32 : 29,
    33 : 36,
    34 : 4,
    35 : 44,
    36 : 12,
    37 : 52,
    38 : 20,
    39 : 60,
    40 : 28,
    41 : 35,
    42 : 3,
    43 : 43,
    44 : 11,
    45 : 51,
    46 : 19,
    47 : 59,
    48 : 27,
    49 : 34,
    50 : 2,
    51 : 42,
    52 : 10,
    53 : 50,
    54 : 18,
    55 : 58,
    56 : 26,
    57 : 33,
    58 : 1,
    59 : 41,
    60 : 9,
    61 : 49,
    62 : 17,
    63 : 57,
    64 : 25,
}

def change_timin_to_uracil(blocks):
    dna = []
    for p in blocks:
        tmp = p.replace('T', 'U')
        dna.append(tmp)

    return dna

def convert_binary_to_dna(blocks):
    dna_text = []
    for s in blocks:
        tmp = ''
        tmp2 = ''
        for b in s:
            tmp += b
            if len(tmp) == 2:
                tmp2 += dnab[tmp]
                tmp = ''
        dna_text.append(tmp2)

    return dna_text

def inv_mrna_trna(blocks):
    perm = []
    for sb in blocks:
        tmp = ''
        for c in sb:
            tmp += inv_mRNA[inv_tRNA[c]]
        perm.append(tmp)

    return perm

def convert_dna_to_binary(blocks):
    binary_text = []
    for p in blocks:
        tmp = ''
        for c in p:
            tmp += binary[c]
        binary_text.append(tmp)

    return binary_text

def xor(blocks, key):
    xored = []
    for b in blocks:
        y = int(b,2) ^ int(key,2)
        bino = '{0:0{1}b}'.format(y,len(b))
        assert 64 == len(bino)
        xored.append(bino)

    return xored

def inv_permutation(blocks):
    perm = []
    for p in blocks:
        tmp = ''
        for i, c in enumerate(p):
            tmp += p[inv_permute[i+1] - 1]
        perm.append(tmp)
        tmp = ''

    return perm

def inv_substitution(blocks):
    sub_text = []
    for pb in blocks:
        tmp = ''
        tmp2 = ''
        for b in pb:
            tmp += b
            if len(tmp) == 4:
                # prva dva znaka row
                # druga dva znaka column
                tmp2 += inverse_sbox[tmp[0:2]][tmp[2:4]]
                tmp = ''
        sub_text.append(tmp2)

    return sub_text

def print_blocks(blocks):
    for b in blocks:
        print(b)

def generate_round_keys(src):
    num_keys = 16
    round_keys = []
    for k in range(num_keys):
        random.seed(src + k)
        x = random.getrandbits(64)
        bino = '{0:0{1}b}'.format(x,64)
        assert len(bino) == 64
        round_keys.append(bino)

    return round_keys

if __name__ == '__main__':
    # DNA cipher text
    ct = ['GCACAAACAAATAATCTAAACACAATCATTCA']
    key = 1234
    round_keys = round_keys = generate_round_keys(key)

    # Convert DNA to binary
    binary = convert_dna_to_binary(ct)
    #print_blocks(binary)

    # XOR with key
    xored = xor(binary, round_keys[0])
    #print_blocks(xored)

    # Inverse permutation
    perm = inv_permutation(xored)
    #print_blocks(perm)

    # Convert back to DNA
    rna = convert_binary_to_dna(perm)
    #print_blocks(rna)

    # Change Timin to Uracil
    dna = change_timin_to_uracil(rna)
    #print_blocks(dna)

    # Inverse tRNA and mRNA
    inv = inv_mrna_trna(dna)
    #print_blocks(inv)

    # Inverse Substitution
    invsub = inv_substitution(inv)
    #print_blocks(invsub)

    # Remove padding
    decoded = decode_from_blocks(invsub)
    print_blocks(decoded)

    # Decode text
