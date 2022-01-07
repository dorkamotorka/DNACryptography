import random
import sys 

nucleotides = ["A", "T", "G", "C"]

def mutatate_nucleotides(seq, num_mutations = 1):
    seq_list = list(seq) 
    n  = len(seq_list)

    for i in range(num_mutations):
        pos = random.randrange(0, n)
        _nucleotides = list(nucleotides)
        _nucleotides.remove(seq_list[pos])
        seq_list[pos] = random.choice(_nucleotides)

    return "".join(seq_list)


def insert_nucletotide(seq, num_mutations = 1):
    seq_list = list(seq) 
    n =  len(seq_list)
    for i in range(num_mutations):
        pos  = random.randrange(0, n)
        seq_list.insert(pos, random.choice(nucleotides))

    return "".join(seq_list)


def remove_nucletotide(seq, num_mutations = 1):
    seq_list = list(seq) 
    n = len(seq_list)

    for i in range(num_mutations):
        pos  = random.randrange(0, n)
        del seq_list[pos]

    return "".join(seq_list)


if __name__ == '__main__':
    '''
    dna_text = "TCTCCCCCTCATACCGAAAAGCTTCCAGACCC"
    dna_text_mutated = mutatate_nucleotides(dna_text, len(dna_text)) 
    print(dna_text_mutated)

    dna_text_mutated = insert_nucletotide(dna_text)
    print(dna_text_mutated)

    dna_text_mutated = remove_nucletotide(dna_text)
    print(dna_text_mutated)
    '''
    pass
    

    

