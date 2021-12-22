#!/usr/bin/env python

# Huffman Enkodiranje
he = {
    'a': 'GC',
    'b': 'TTA',
    'c': 'GGA',
    'd': 'TC',
    'e': 'C',
    'f': 'GTA',
    'g': 'GTC',
    'h': 'TG',
    'i': 'AA',
    'j': 'TTTA',
    'y': 'GTT',
    'k': 'TTTG',
    'l': 'GGG',
    'm': 'GTG',
    'w': 'GGC',
    'n': 'AT',
    'o': 'AG',
    'p': 'TTG',
    'r': 'TA',
    't': 'GA',
    'q': 'TTTCG',
    's': 'AC',
    'u': 'GGT',
    'v': 'TTC',
    'z': 'TTTCA',
    'x': 'TTTT',
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
        'AA': 'CTTC',	
        'AG': 'AACT',
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
                b += 'C'
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
    for sb in sub_text:
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

def xor(blocks):
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

if __name__ == '__main__':
    string = "Zapadeljeprvisn"
    blocks = encode_into_blocks(string)

    # Padding
    padded_blocks = padding(blocks)
    print_blocks(padded_blocks)

    # Substitucija
    sub_text = substitution(padded_blocks)
    #print_blocks(sub_text)

    # Permutacija
    perm = permutation(sub_text)
    #print_blocks(perm)

    # Za DNA sekvenco zamenjaj Uracil z Timinom
    dna = change_uracil_to_timin(perm)
    #print_blocks(dna)

    # Convert key and text to binary
    # TODO: key generation
    key = '1010101010110111010101010101010101010101010101010110101010101011'
    assert 64 == len(key)

    binary_text = convert_dna_to_binary(dna)
    #print_blocks(binary_text)
    
    # XOR
    xored = xor(binary_text)
    #print_blocks(xored)

    dna_text = convert_binary_to_dna(xored)
    print_blocks(dna_text)
