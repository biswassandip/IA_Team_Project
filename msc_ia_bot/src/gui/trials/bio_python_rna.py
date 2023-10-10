import matplotlib.pyplot as plt

# Define your DNA or RNA sequence
sequence = "ATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Set the y-coordinate for plotting
y = 0

# Plot each base in the sequence
for base in sequence:
    color = 'green' if base in 'AG' else 'blue'  # Assign colors for A/G and C/T
    ax.plot([y, y + 1], [0, 0], color=color, linewidth=5)
    y += 1

# Set axis limits and labels
ax.set_xlim(0, len(sequence))
ax.set_ylim(-1, 1)
ax.axis('off')

# Add a title
plt.title("DNA/RNA Sequence Visualization")

# Show the sequence plot
plt.show()
