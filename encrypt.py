#!/usr/bin/env python

import sys
import random
import hashlib
import parse_sbox

sbox_parsed = parse_sbox.sbox 
# Huffman Enkodiranje
he = {
    'a': 'ACAT',
    'b': 'ACTG',
    'c': 'ACCC',
    'd': 'ACGA',
    'e': 'TCAT',
    'f': 'TCTG',
    'g': 'TCCG',
    'h': 'TCGT',
    'i': 'CCAG',
    'j': 'CCTA',
    'y': 'AAAA',
    'k': 'CCCG',
    'l': 'CCGG',
    'm': 'GCAA',
    'w': 'GCTA',
    'n': 'GCTT',
    'o': 'GCCG',
    'p': 'GCGC',
    'r': 'ACCG',
    't': 'TCCC',
    'q': 'ACTC',
    's': 'TCTC',
    'u': 'CCTT',
    'v': 'CCCC',
    'z': 'AATT',
    'x': 'GCCC',
    '': 'GGGG',
}

# Timin v Uracil, ostalo enako
mRNA = {
    'G': 'G',
    'C': 'C',
    'T': 'U',
    'A': 'A',
}

# komplementi baz
tRNA = {
    'G': 'C',
    'C': 'G',
    'A': 'U',
    'U': 'A',
}

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

sbox = {
    'AA': {
        'AA': 'GCAT',	
        'AG': 'GTTA',
        'AC': 'GTGT',
        'AT': 'GTCT',
        'GA': 'TTAC',
        'GG': 'GCCT',
        'GC': 'GCTT',
        'GT': 'TAGG',
        'CA': 'ATAA',
        'CG': 'AAAG',
        'CC': 'GCGT',
        'CT': 'ACCT',
        'TA': 'TTTG',
        'TC': 'TCGT',
        'TG': 'CCCT',
        'TT': 'GTGC',
    },
    'AG':{
        'AA': 'TACC',	
        'AG': 'CAAC',
        'AC': 'TACG',
        'AT': 'GTTC',
        'GA': 'TTCC',
        'GG': 'GGCG',
        'GC': 'GAGT',
        'GT': 'TTAA',
        'CA': 'CCTC',
        'CG': 'TCGA',
        'CC': 'CCAC',
        'CT': 'CCTT',
        'TA': 'CGTA',
        'TC': 'CCGA',
        'TG': 'GTAC',
        'TT': 'TAAA',
    },
    'AC':{
        'AA': 'CTGT',	
        'AG': 'TTTC',
        'AC': 'CGAT',
        'AT': 'ACGC',
        'GA': 'ATGC',
        'GG': 'ATTT',
        'GC': 'TTGT',
        'GT': 'TATA',
        'CA': 'ATGA',
        'CG': 'CCGG',
        'CC': 'TGGG',
        'CT': 'TTAG',
        'TA': 'GTAG',
        'TC': 'TCCA',
        'TG': 'ATAG',
        'TT': 'AGGG',
    },
    'AT':{
        'AA': 'AAGA',	
        'AG': 'TAGT',
        'AC': 'ACAT',
        'AT': 'TAAT',
        'GA': 'AGCA',
        'GG': 'CGGC',
        'GC': 'AAGG',
        'GT': 'CGCC',
        'CA': 'AAGT',
        'CG': 'AGAC',
        'CC': 'CAAA',
        'CT': 'TGAC',
        'TA': 'TGCT',
        'TC': 'ACGT',
        'TG': 'CTAC',
        'TT': 'GTGG',
    },
    'GA':{
        'AA': 'AACG',	
        'AG': 'CAAT',
        'AC': 'ACTA',
        'AT': 'AGCC',
        'GA': 'AGCT',
        'GG': 'GCTG',
        'GC': 'GGCC',
        'GT': 'CCAA',
        'CA': 'GGAC',
        'CG': 'ATCT',
        'CC': 'TCGC',
        'CT': 'CTAT',
        'TA': 'ACCG',
        'TC': 'TGAT',
        'TG': 'ACTT',
        'TT': 'CAGA',
    },
    'GG':{
        'AA': 'GGAT',	
        'AG': 'TCAG',
        'AC': 'AAAA',
        'AT': 'TGTC',
        'GA': 'ACAA',
        'GG': 'TTTA',
        'GC': 'CTAG',
        'GT': 'GGCT',
        'CA': 'GCCC',
        'CG': 'TACT',
        'CC': 'CTTG',
        'CT': 'ATCG',
        'TA': 'GACC',
        'TC': 'GATA',
        'TG': 'GGCA',
        'TT': 'TATT',
    },
    'GC':{
        'AA': 'TCAA',	
        'AG': 'TGTT',
        'AC': 'CCCC',
        'AT': 'TTCT',
        'GA': 'GAAT',
        'GG': 'GATC',
        'GC': 'ATAT',
        'GT': 'CAGG',
        'CA': 'GAGG',
        'CG': 'TTCG',
        'CC': 'AAAC',
        'CT': 'GTTT',
        'TA': 'GGAA',
        'TC': 'ATTA',
        'TG': 'CGTT',
        'TT': 'CCCA',
    },
    'GT':{
        'AA': 'GGAG',	
        'AG': 'CCAT',
        'AC': 'GAAA',
        'AT': 'CATT',
        'GA': 'CGAC',
        'GG': 'CGTC',
        'GC': 'ATCA',
        'GT': 'TTGG',
        'CA': 'CTTA',
        'CG': 'CTGC',
        'CC': 'TCCC',
        'CT': 'ACAG',
        'TA': 'AGAA',
        'TC': 'TTTT',
        'TG': 'TTAT',
        'TT': 'TCAC',
    },
    'CA':{
        'AA': 'TATC',	
        'AG': 'AATA',
        'AC': 'AGAT',
        'AT': 'TGTA',
        'GA': 'GGTT',
        'GG': 'CGGT',
        'GC': 'GAGA',
        'GT': 'AGGT',
        'CA': 'TAGA',
        'CG': 'CCGT',
        'CC': 'GTTG',
        'CT': 'ATTC',
        'TA': 'GCGA',
        'TC': 'GGTC',
        'TG': 'AGCG',
        'TT': 'GTAT',
    },
    'CG':{
        'AA': 'GCAA',	
        'AG': 'CAAG',
        'AC': 'GATT',
        'AT': 'TCTA',
        'GA': 'ACAC',
        'GG': 'ACCC',
        'GC': 'CGAA',
        'GT': 'CACA',
        'CA': 'GAGC',
        'CG': 'TGTG',
        'CC': 'CTCA',
        'CT': 'AGGA',
        'TA': 'TCTG',
        'TC': 'GGTG',
        'TG': 'AACT',
        'TT': 'TCCT',
    },
    'CC':{
        'AA': 'TGAA',	
        'AG': 'ATAC',
        'AC': 'ATCC',
        'AT': 'AACC',
        'GA': 'GACG',
        'GG': 'AAGC',
        'GC': 'ACGA',
        'GT': 'GGTA',
        'CA': 'TAAC',
        'CG': 'TCAT',
        'CC': 'CCTA',
        'CT': 'GCAC',
        'TA': 'CGAG',
        'TC': 'CGGG',
        'TG': 'TGGA',
        'TT': 'GTCG',
    },
    'CT':{
        'AA': 'TGGT',	
        'AG': 'TACA',
        'AC': 'ATGT',
        'AT': 'GCTC',
        'GA': 'CATC',
        'GG': 'TCGG',
        'GC': 'GATG',
        'GT': 'CCCG',
        'CA': 'GCTA',
        'CG': 'GGGC',
        'CC': 'TTGA',
        'CT': 'TGCC',
        'TA': 'GCGG',
        'TC': 'GTCC',
        'TG': 'CCTG',
        'TT': 'AACA',
    },
    'TA':{
        'AA': 'CTCC',	
        'AG': 'GTCA',
        'AC': 'ACGG',
        'AT': 'ACTG',
        'GA': 'AGTA',
        'GG': 'CCGC',
        'GC': 'CTGA',
        'GT': 'TAGC',
        'CA': 'TGCA',
        'CG': 'TCTC',
        'CC': 'GTGA',
        'CT': 'AGTT',
        'TA': 'GACT',
        'TC': 'CTTC',
        'TG': 'CACT',
        'TT': 'CACC',
    },
    'TC':{
        'AA': 'GTAA',	
        'AG': 'ATTG',
        'AC': 'CTGG',
        'AT': 'GCGC',
        'GA': 'GACA',
        'GG': 'AAAT',
        'GC': 'TTGC',
        'GT': 'AATG',
        'CA': 'GCAG',
        'CG': 'ATGG',
        'CC': 'GGGT',
        'CT': 'CTCG',
        'TA': 'CAGC',
        'TC': 'TAAG',
        'TG': 'AGTC',
        'TT': 'CGTG',
    },
    'TG':{
        'AA': 'TGAG',	
        'AG': 'TTCA',
        'AC': 'CGCA',
        'AT': 'AGAG',
        'GA': 'GCCG',
        'GG': 'TCCG',
        'GC': 'CATG',
        'GT': 'CGGA',
        'CA': 'CGCT',
        'CG': 'AGTG',
        'CC': 'CAGT',
        'CT': 'TGCG',
        'TA': 'TATG',
        'TC': 'GGGG',
        'TG': 'ACCA',
        'TT': 'TCTT',
    },
    'TT':{
        'AA': 'CATA',	
        'AG': 'CCAG',
        'AC': 'CACG',
        'AT': 'AATC',
        'GA': 'CTTT',
        'GG': 'TGGC',
        'GC': 'GAAC',
        'GT': 'GCCA',
        'CA': 'GAAG',
        'CG': 'CGCG',
        'CC': 'ACTC',
        'CT': 'AATT',
        'TA': 'CTAA',
        'TC': 'GGGA',
        'TG': 'CTCT',
        'TT': 'AGGC',
    },
}

permute = {
    1 : 58,
    2 : 50,
    3 : 42,
    4 : 34,
    5 : 26,
    6 : 18,
    7 : 10,
    8 : 2,
    9 : 60,
    10 : 52,
    11 : 44,
    12 : 36,
    13 : 28,
    14 : 20,
    15 : 12,
    16 : 4,
    17 : 62,
    18 : 54,
    19 : 46,
    20 : 38,
    21 : 30,
    22 : 22,
    23 : 14,
    24 : 6,
    25 : 64,
    26 : 56,
    27 : 48,
    28 : 40,
    29 : 32,
    30 : 24,
    31 : 16,
    32 : 8,
    33 : 57,
    34 : 49,
    35 : 41,
    36 : 33,
    37 : 25,
    38 : 17,
    39 : 9,
    40 : 1,
    41 : 59,
    42 : 51,
    43 : 43,
    44 : 35,
    45 : 27,
    46 : 19,
    47 : 11,
    48 : 3,
    49 : 61,
    50 : 53,
    51 : 45,
    52 : 37,
    53 : 29,
    54 : 21,
    55 : 13,
    56 : 5,
    57 : 63,
    58 : 55,
    59 : 47,
    60 : 39,
    61 : 31,
    62 : 23,
    63 : 15,
    64 : 7,
}

def encode_into_blocks(text):
    encoded = ''
    for c in text:
        # Spaces and symbols are left out
        if c in he:
            encoded += he[c.lower()]

    n = 32 # 32 dušikovih baz
    blocks = [encoded[i:i+n] for i in range(0, len(encoded), n)]

    return blocks

def padding(blocks):
    padded_blocks = []
    for b in blocks:
        if len(b) < 32:
            m = 32 - len(b)
            for _ in range(m):
                b += 'G'
        padded_blocks.append(b)

    return padded_blocks

def print_blocks(blocks):
    for b in blocks:
        print(b)

def substitution(blocks):
    sub_text = []
    for pb in blocks:
        tmp = ''
        tmp2 = ''
        for b in pb:
            tmp += b
            if len(tmp) == 4:
                # prva dva znaka row
                # druga dva znaka column
                tmp2 += sbox[tmp[0:2]][tmp[2:4]] 
                tmp = ''
        sub_text.append(tmp2)

    return sub_text

def permutation(blocks):
    perm = []
    for p in blocks:
        tmp = ''
        for i, c in enumerate(p):
            tmp += p[permute[i+1] - 1] 
        perm.append(tmp)
        tmp = ''

    return perm

def mrna_trna(blocks):
    perm = []
    for sb in blocks:
        tmp = ''
        for c in sb:
            tmp += tRNA[mRNA[c]]
        perm.append(tmp)
    
    return perm

def change_uracil_to_timin(blocks):
    dna = []
    for p in blocks:
        tmp = p.replace('U', 'T')
        dna.append(tmp)

    return dna

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

def compute_hashes(blocks, key):
    hashes = []
    for b in blocks:
        m = hashlib.sha256()
        m.update(str(key).encode('utf-8'))
        m.update(b.encode('utf-8'))
        h = m.hexdigest()
        hashes.append(h)

    return hashes

def convert_hex_to_bin(blocks):
    binaries = []
    for b in blocks:
        scale = 16 ## equals to hexadecimal
        x = bin(int(b, scale))[2:]
        binaries.append(x)

    return binaries

if __name__ == '__main__':
    string = sys.argv[2]
    #print(string)
    # encodeing
    key = int.from_bytes(sys.argv[1].encode("utf-8"), byteorder='big')

    round_keys = generate_round_keys(key)
    #print(round_keys)
    blocks = encode_into_blocks(string)

    # Padding
    padded_blocks = padding(blocks)
    #print_blocks(padded_blocks)

    for r in round_keys:
        # Substitucija
        sub_text = substitution(padded_blocks)
        #print_blocks(sub_text)

        # Permutacija
        perm = mrna_trna(sub_text)
        #print_blocks(perm)

        # Za DNA sekvenco zamenjaj Uracil z Timinom
        dna = change_uracil_to_timin(perm)
        #print_blocks(dna)

        # Convert text to binary
        binary_text = convert_dna_to_binary(dna)
        #print_blocks(binary_text)

        # Permutacija binary - mRNA + tRNA samo vrne nasprotni par (back-and-forth)
        perm_bin = permutation(binary_text)
        #print_blocks(perm_bin)

        # XOR
        xored = xor(perm_bin, r)
        #print_blocks(xored)

        dna_text = convert_binary_to_dna(xored)
        padded_blocks = dna_text

    print_blocks(dna_text)
    # Compute hash from key and cipher text to provide integrity
    hashes = compute_hashes(dna_text, key)
    #print_blocks(hashes)

    # Convert hash digest to DNA sequence and store it
    binaries = convert_hex_to_bin(hashes)
    #print_blocks(binaries)

    dna_hashes = convert_binary_to_dna(binaries)
    #print_blocks(dna_hashes)


