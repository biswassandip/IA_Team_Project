import forgi
import forgi.graph.bulge_graph as fgb
import forgi.visual.mplotlib as fvm

# Define your RNA sequence and dot-bracket notation for secondary structure
rna_sequence = "AUGUAGCGUAAUCCGUUGACAUAA"
dot_bracket = "((((((....))))))....(((....)))....)"

# Create a BulgeGraph from the dot-bracket notation
bg = fgb.BulgeGraph.from_dotbracket(dot_bracket)

# Create a matplotlib figure
fig, ax = plt.subplots()

# Plot the RNA sequence
fvm.plot_rna(rna_sequence, bg, text_kwargs={'size': 16}, ax=ax)

# Add a title
plt.title("RNA Sequence with Secondary Structure")

# Show the plot
plt.show()
