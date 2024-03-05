import govindarajan_deepak_helper as helper
from govindarajan_deepak_helper import amino_acids

def transcription(dna_sequence):
    mrna = ""
    dna_sequence = dna_sequence.replace('T', 'U')
    for char in dna_sequence:
        if(char == 'A'):
            mrna += 'U'
        elif(char == 'U'):
            mrna += 'A'
        elif(char == 'G'):
            mrna += 'C'
        elif(char == 'C'): 
            mrna += 'G'
    return mrna

def translate(mrna):
    protein = ''
    # Split mrna into nucleotide triplets
    triplets = helper.chunk(mrna, 3)
    
    # Replace Triplets with Amino Acids
    for triplet in triplets:
        protein += helper.amino_acids[triplet] + " "

    return protein


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

mrna = transcription(dna)
protein = translate(mrna)
print(protein)