from Bio.Seq import Seq
from Bio.SeqUtils import seq1
import matplotlib.pyplot as plt

# Define your RNA sequence string with STOP codons
rna_sequence = "AUGUAGCGUAAUCCGUUGACAUAAUAGAAACCC"

# Create a Seq object from the RNA sequence
rna_seq = Seq(rna_sequence)

# Split the sequence into triplets
triplets = [rna_seq[i:i+3] for i in range(0, len(rna_seq), 3)]

# Define a dictionary to map RNA codons to amino acids, including STOP codons
codon_to_aa = {
    'AUG': 'M', 'UAG': 'STOP', 'CGU': 'R', 'AAU': 'N', 'CCG': 'P',
    'UUU': 'F', 'GAC': 'D', 'AUA': 'I', 'UAA': 'STOP', 'UCA': 'STOP'
    # Add more codon-to-amino-acid mappings as needed
}

# Count the frequencies of each triplet
triplet_counts = {triplet: triplets.count(triplet) for triplet in set(triplets)}

# Extract triplet labels and frequencies as strings, including amino acids and STOP
labels = [f"{triplet} ({codon_to_aa.get(str(triplet), '?')})" for triplet in triplet_counts.keys()]
frequencies = list(triplet_counts.values())

# Create a bar chart to visualize the triplet frequencies
plt.bar(labels, frequencies)
plt.xlabel("RNA Triplets (Amino Acids or STOP)")
plt.ylabel("Frequency")
plt.title("RNA Triplet Sequence Visualization with Amino Acids and STOP Codons")
plt.xticks(rotation=90)
plt.tight_layout()

# Show the chart
plt.show()
