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


if __name__ == '__main__':
    string = "Pozdravljena zaspanka"
    enc = ''
    for c in string:
        # Spaces and symbols are missing
        if c in he:
            enc += he[c.lower()]

    print(enc)
