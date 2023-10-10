import nglview

# Initialize a Structure object with a PDB file path and a list of additional options using the `nglview.Structure.from_file()` method
structure = nglview.Structure.from_file("rna_structure.pdb", {"colorScheme": "rainbow"})

# Display the structure
view = nglview.View(structure)
view.show()