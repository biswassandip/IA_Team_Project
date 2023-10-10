import py3Dmol

# Read the PDB file
with open("rna_structure.pdb", "r") as pdb_file:
    pdb_data = pdb_file.read()

# Create a 3Dmol viewer object
viewer = py3Dmol.view(width=400, height=400)

# Add the PDB data to the viewer
viewer.addModel(pdb_data, "pdb")

# Style the visualization (you can customize this)
viewer.setStyle({"cartoon": {"color": "spectrum"}})
viewer.zoomTo()

# Show the 3D visualization
viewer.show()
