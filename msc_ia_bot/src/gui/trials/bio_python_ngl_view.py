from Bio import PDB
import nglview as nv

# Create a PDB parser
parser = PDB.PDBParser(QUIET=True)

# Load the PDB structure from the file
structure = parser.get_structure("RNA_Structure", "rna_structure.pdb")

# Create a viewer using nglview
view = nv.show_biopython(structure)

# Display the viewer
view._remote_call("setSize", target="Widget", args=["600px", "400px"])
view
