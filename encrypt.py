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
