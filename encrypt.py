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

if __name__ == '__main__':
    string = "Pozdravljena zaspanka"
    encoded = ''
    for c in string:
        # Spaces and symbols are missing
        if c in he:
            encoded += he[c.lower()]

    #print(encoded)
    #print(len(encoded))

    n = 32 # 32 dušikovih baz
    blocks = [encoded[i:i+n] for i in range(0, len(encoded), n)]

    # Padding
    padded_blocks = []
    for b in blocks:
        if len(b) < 32:
            m = 32 - len(b)
            for _ in range(m):
                b += 'C'

        padded_blocks.append(b)

    #print(padded_blocks)
    for pb in padded_blocks:
        pass
        #print(len(pb))

    # Substitucija

    # Permutacija
    perm = []
    for pb in padded_blocks:
        tmp = ''
        for c in pb:
            tmp += tRNA[mRNA[c]]
        perm.append(tmp)

    for p in perm:
        pass
        #print(p)
        #print(len(p))

    # Za DNA sekvenco zamenjaj Uracil z Timinom
    dna = []
    for p in perm:
        tmp = p.replace('U', 'T')
        dna.append(tmp)

    for p in dna:
        print(p)
        #print(len(p))

    # Convert key and text to binary
    key = '1010101010110111010101010101010101010101010101010110101010101011'
    assert 64 == len(key)

    binary_text = []
    for p in dna:
        tmp = ''
        for c in p:
            tmp += binary[c]
        binary_text.append(tmp)

    for b in binary_text:
        #print(b)
        #print(len(b))
        assert 64 == len(b)

    # XOR
    xored = []
    for b in binary_text:
        y = int(b,2) ^ int(key,2)
        bino = '{0:0{1}b}'.format(y,len(b))
        assert 64 == len(bino)
        xored.append(bino)

    dna_text = []
    for s in xored:
        tmp = ''
        tmp2 = ''
        for b in s:
            tmp += b
            if len(tmp) == 2:
                tmp2 += dnab[tmp] 
                tmp = ''
        dna_text.append(tmp2)

    # Convert back to DNA
    for b in dna_text:
        print(b)

# TODO: Everything in functions
