from Bio.Seq import Seq
import matplotlib.pyplot as plt

# Define your RNA triplet sequence string
rna_sequence = "AUGUAGCGUAAUCCGUUGACAUAA"

# Create a Seq object from the RNA sequence
rna_seq = Seq(rna_sequence)

# Split the sequence into triplets
triplets = [rna_seq[i:i+3] for i in range(0, len(rna_seq), 3)]

# Count the frequencies of each triplet
triplet_counts = {triplet: triplets.count(triplet) for triplet in set(triplets)}

# Extract triplet labels and frequencies as strings
labels = [str(triplet) for triplet in triplet_counts.keys()]
frequencies = list(triplet_counts.values())

# Create a bar chart to visualize the triplet frequencies
plt.bar(labels, frequencies)
plt.xlabel("RNA Triplets")
plt.ylabel("Frequency")
plt.title("RNA Triplet Sequence Visualization")
plt.xticks(rotation=90)
plt.tight_layout()

# Show the chart
plt.show()
