#!/usr/bin/env python

import sys

he = {
    'a': 'ACAT', 'b': 'ACTG', 'c': 'ACCC', 'd': 'ACGA', 'e': 'TCAT',
    'f': 'TCTG', 'g': 'TCCG', 'h': 'TCGT', 'i': 'CCAG', 'j': 'CCTA',
    'y': 'AAAA', 'k': 'CCCG', 'l': 'CCGG', 'm': 'GCAA', 'w': 'GCTA',
    'n': 'GCTT', 'o': 'GCCG', 'p': 'GCGC', 'r': 'ACCG', 't': 'TCCC',
    'q': 'ACTC', 's': 'TCTC', 'u': 'CCTT', 'v': 'CCCC', 'z': 'AATT',
    'x': 'GCCC', '': 'GGGG',
}

def encode(text):
    encoded = ''
    for c in text:
        # Spaces and symbols are left out
        if c in he:
            encoded += he[c.lower()]

    return encoded 
    
if __name__ == '__main__':
    string = sys.argv[1]
    encoded_string = encode(string)
    print(encoded_string)
