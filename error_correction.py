import hashlib
import itertools
import mutations

def compute_hash(seq, key):
    m_ = hashlib.sha256()
    m_.update(str(key).encode('utf-8'))
    m_.update(seq.encode('utf-8'))
    h = m_.hexdigest()

    return h

def compute_hash_blocks(blocks, key, m = 3):
    hashes = []
    for block in blocks:
        block_hashes = []
        for i in range(0, len(block) - m + 1, m):
            seq = block[i : i + m]
            block_hashes.append(compute_hash(seq, key))
        
        if i + m != len(block):
            block_hashes.append(compute_hash(block[i + m :], key))

        hashes.append(block_hashes)             

    return hashes

def error_correction(ct, hash_blocks, key, m = 3):
    ct_matrix = []
    for j in range(len(ct)):
        block = ct[j]
        corrected_ct = ""
        cnt = 0
        for i in range(0, len(block) - m + 1, m):
            seq = block[i : i + m]
            if compute_hash(seq, key) != hash_blocks[j][cnt]:
                for curr_seq in itertools.product("AGTC", repeat = m):
                    curr_seq = "".join(curr_seq)
                    if compute_hash(curr_seq, key) == hash_blocks[j][cnt]:
                        seq = curr_seq
                        break

            corrected_ct += seq
            cnt += 1

        #Check for remaing chars.
        if i + m != len(block):
            seq = block[i + m : ]
            if compute_hash(seq, key) != hash_blocks[j][cnt]:
                for curr_seq in itertools.product("AGTC", repeat = len(seq)):
                    curr_seq = "".join(curr_seq)
                    if compute_hash(curr_seq, key) == hash_blocks[j][cnt]:
                        seq = curr_seq                        
                        break

            corrected_ct += seq
        ct_matrix.append(corrected_ct)

    return ct_matrix
        

if __name__ == '__main__':
    #Compute hash blocks of size m from encrypted text.
    dna_text = ["TAGTCCGATTAGTCAAGTCAGTCCTTCTGTGCCTG"]
    KEY = 12
    M   = 3
    hash_blocks = compute_hash_blocks(dna_text, key = KEY, m = M)
    #print(hash_blocks)

    # Ideal scenario. Ciphertext is not mutated.
    ct = dna_text
    print("Original  = " + str(ct))

    # Apply random mutation.
    NUM_OF_MUTATIONS = 6
    ct_mutated = [] 
    for block in dna_text:
        ct_mutated.append(mutations.mutatate_nucleotides(block, num_mutations = NUM_OF_MUTATIONS))

    print("Mutated   = " + str(ct_mutated))

    # Correct the error.
    ct_corrected = error_correction(ct_mutated, hash_blocks, key = KEY, m = M)
    print("Corrected = " + str(ct_corrected))

    #Error check.
    if ct_corrected != ct:
        raise Exception("[Error] : " + str(ct_corrected) + " != " + str(ct))

