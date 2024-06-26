# Counting DNA Nucleotides

# use to run code:
# python3 start.py (WSL)

# py start.py (bash)

def count_nucleotides(dna_string):
    # Count occurrences of each nucleotide
    count_A = dna_string.count('A')
    count_C = dna_string.count('C')
    count_G = dna_string.count('G')
    count_T = dna_string.count('T')
    
    # Return the counts as a tuple
    return count_A, count_C, count_G, count_T

def read_dna_from_file(file_path):
    with open(file_path, 'r') as file:
        dna_string = file.readline().strip()  # Read only the first line and strip any whitespace
    return dna_string

# Specify the path to your input file
file_path = 'rosalind_dna.txt'

# Read the DNA string from the file
dna_string = read_dna_from_file(file_path)

# Get the counts
counts = count_nucleotides(dna_string)

# Print the results separated by spaces
print(' '.join(map(str, counts)))