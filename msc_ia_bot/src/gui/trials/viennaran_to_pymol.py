import pymol

# Initialize PyMOL
pymol.finish_launching()

# Load the PDB file
pymol.cmd.load("rna_structure.pdb", "rna_structure")

# Display the molecule
pymol.cmd.show("cartoon")
pymol.cmd.color("blue", "rna_structure")

# Add labels (optional)
pymol.cmd.label("name CA", '"%s" % resn + resi', quiet=0)

# You can customize the view, colors, and labels as needed

# Save a static image (optional)
pymol.cmd.png("rna_structure.png", width=800, height=600, dpi=300)

# Enter interactive mode (optional)
pymol.cmd.rock()
