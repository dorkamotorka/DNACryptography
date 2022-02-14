from encrypt import *
from error_correction import *

if __name__ == '__main__':
    string = sys.argv[2]
    #print(string)
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
    print_blocks(hashes)

    # Compute hash blocks
    M = 3
    hash_blocks = compute_hash_blocks(dna_text,key, m = M)
    print_blocks(hash_blocks)

    # Convert hash digest to DNA sequence and store it
    binaries = convert_hex_to_bin(hashes)
    #print_blocks(binaries)

    dna_hashes = convert_binary_to_dna(binaries)
    #print_blocks(dna_hashes)


