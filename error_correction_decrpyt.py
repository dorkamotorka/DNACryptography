from decrypt import *
from error_correction import *
import mutations

if __name__ == '__main__':
    # DNA cipher text
    ct  = [sys.argv[2]]
    key = int(sys.argv[1])

    # For now just compute hash blocks from un-mutated ct.
    M = 3
    hash_blocks = compute_hash_blocks(ct, key, m = M)
    print("Original  = " + str(ct))

    #Simulate mutations.
    ct_mutated = []
    for block in ct:
        ct_mutated.append(mutations.mutatate_nucleotides(block))
    print("Mutated   = " + str(ct_mutated))

    
    # Correct mutations.
    ct_corrected = error_correction(ct_mutated, hash_blocks, key)
    print("Corrected = " + str(ct_corrected))

    if ct_corrected != ct:
        raise Exception("[Error] : " + str(ct_corrected) + " != " + str(ct))


    # Set ct to its correct value.
    ct = ct_corrected
    round_keys = round_keys = generate_round_keys(key)

    for r in reversed(round_keys):
        # Convert DNA to binary
        bina = convert_dna_to_binary(ct)
        #print_blocks(bin)

        # XOR with key
        xored = xor(bina, r)
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

        ct = invsub

    # Remove padding
    unpadded = remove_padding(invsub)
    print_blocks(unpadded)

    # Decode text
    decoded = decode_from_blocks(unpadded)
    print_blocks(decoded)
