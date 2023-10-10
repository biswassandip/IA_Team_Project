import matplotlib.pyplot as plt
import numpy as np

# Define the RNA sequence
rna_sequence = "AUGCGUACGAUCGAUCGAUCGAU"

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, len(rna_sequence))
ax.set_ylim(-5, 5)

# Define the base pairing rules (you can customize this)
base_pairing = {
    'A': 'U',
    'U': 'A',
    'C': 'G',
    'G': 'C',
}

# Initialize variables for plotting
x = np.arange(len(rna_sequence))
y = np.zeros(len(rna_sequence))

# Plot the helix
for i, base in enumerate(rna_sequence):
    y[i] = i % 2  # Alternating heights for helix appearance
    ax.text(x[i], y[i], base, fontsize=12, ha='center', va='center')

# Connect complementary bases with lines
for i, base in enumerate(rna_sequence):
    if i < len(rna_sequence) - 1:
        next_base = rna_sequence[i + 1]
        if base_pairing.get(base) == next_base:
            ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], color='blue')

# Set axis labels and title
ax.set_xlabel("Position")
ax.set_ylabel("Helix Level")
ax.set_title("RNA Sequence as a Helix")

# Remove ticks and show the plot
ax.set_xticks([])
ax.set_yticks([])
plt.grid(visible=False)
plt.show()
