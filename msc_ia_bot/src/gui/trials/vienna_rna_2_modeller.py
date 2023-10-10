import os
from modeller import Environ, Model
import shutil

# Define the dot-bracket notation for the secondary structure
dot_bracket_notation = ".......((((((((((((((.((((((((((((((((((((((.........)))))))))))))).)))))))))))))))))))))).."  # Replace with your RNA's dot-bracket notation

# Create a temporary directory for MODELLER output files
temp_dir = "modeller_temp"
os.makedirs(temp_dir, exist_ok=True)

# Define a MODELLER environment
env = Environ()

# Create a model object
model = Model(env)

# Build a model from the dot-bracket notation
rna_sequence = "AUGCGUACGAUCGAUCGAUCGAUAUGCGUACGAUCGAUCGAUCGAUAUGCGUACGAUCGAUCGAUCGAUAUGCGUACGAUCGAUCGAUCGAU"
model.build_sequence(dot_bracket_notation, sequence=rna_sequence)

# Generate the 3D structure
model.build(initialize_xyz=False, build_method="INTERNAL_COORDINATES")

# Write the structure to a PDB file
output_pdb = "rna_structure.pdb"
model.write(file=output_pdb)

# Clean up temporary files and directories
shutil.rmtree(temp_dir)

print(f"RNA structure saved to {output_pdb}")
