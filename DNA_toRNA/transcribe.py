
""" 
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t

having length at most 1000 nt.

Return: The transcribed RNA string of t 
"""

""" 
Input:
GATGGAACTTGACTACGTAAATT
Output:
GAUGGAACUUGACUACGUAAAUU 
"""

def transcribe(string):
    # replace all occurances of T with U
    rna = string.replace('T', 'U')
    return rna

def read_dna_from_file(file_path):
    with open(file_path, 'r') as file:
        dna_string = file.readline().strip()  # Read only the first line and strip any whitespace
    return dna_string

#set file path for text input
file_path = 'DNA_toRNA/rosalind_rna.txt'

# Read the DNA string from the file
dna_string = read_dna_from_file(file_path)

# transcribe dna to rna
rna_string = transcribe(dna_string)

# Print results separated by spaces
print(rna_string)

