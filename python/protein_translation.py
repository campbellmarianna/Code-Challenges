"""
Functions that translate RNA into their actual Proteins.

Args:
    "AUGUUUUCU"

Returns:
    ["Methionine", "Phenylalanine", "Serine"]

"""
# Exercism Problem
# Translate RNA into their actual Proteins

# Clarifying Questions
# What is the data type of the output? A list
# Are there duplicates? Only in the STOP situation
# Can I manipulate the input strand? Yes

# Assumptions:
# Input -> Output: String -> List
# Only duplicates in the STOP Condition
# I can change the input strand

# Brainstorm Solutions
# 1 T => O(n), S => 0(1)
# Make the input strand a list
# Check to see of the strand was a STOP condition
# Check the dictionary of Codon (key) and Protein (value) to see if a key strand is found
# pop the strand and append the protein value from dict
# return strand
# 2
# Create protein list
# Check to see of the strand was a STOP condition
# Check the dictionary of Codon (key) and Protein (value) to see if a key strand is found
# append the value found in dict
# return protein list

# Protein function brainstorming ideas
# separate the string into a list - keep string
# get protein for each codon
# append to proteins
# return proteins

# slice the first three charc in the string
# check if it has a protein
# return proteins

def proteins(strand):
    """Returns of collection of proteins for given RNA sequences."""
    if len(strand) == 3:  # one codon
        return protein(strand)
    else:  # RNA T => O(s) S => 0(c)
        proteins = []
        STOP = ['UAA', 'UAG', 'UGA']
        strand_list = [(strand[i:i+3]) for i in range(0, len(strand), 3)]
        for codon in strand_list:
            # stop at the beginning
            if codon == strand_list[0] and codon in STOP:
                break
            elif codon in STOP:  # stop in the middle
                break
            else:  # no stop found
                amino_acid = protein(codon)
                if amino_acid != [] and amino_acid[0] not in proteins:
                    proteins.append(amino_acid[0])
        return list(proteins)


def protein(strand):
    """Returns an individual protein as a result of a given
    nucleotide sequence (codon)."""
    strand = strand.split()
    codons_and_proteins = {
        'AUG':  'Methionine',
        'UUU':	'Phenylalanine',
        'UUC':	'Phenylalanine',
        'UUA':	'Leucine',
        'UUG':	'Leucine',
        'UCU':  'Serine',
        'UCC':  'Serine',
        'UCA':  'Serine',
        'UCG':  'Serine',
        'UAU' : 'Tyrosine',
        'UAC' : 'Tyrosine',
        'UGU':	'Cysteine',
        'UGC':	'Cysteine',
        'UGG':	'Tryptophan'
    }
    # Replace the strand with its protein
    if strand[0] in codons_and_proteins.keys():
        proteina_value = strand.pop()
        strand.append(codons_and_proteins[proteina_value])
        return strand
    else:  # Codon doesn't result in a protein
        return []

if __name__ == '__main__':
    print(proteins('UGGUAGUGG'))
