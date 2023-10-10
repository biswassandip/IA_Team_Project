import RNA

# Replace "YOUR_RNA_SEQUENCE" with your RNA triplet sequence
rna_sequence = "AUGCGUACGAUCGAUCGAUCGAUAUGCGUACGAUCGAUCGAUCGAUAUGCGUACGAUCGAUCGAUCGAUAUGCGUACGAUCGAUCGAUCGAU"

# Create an RNA sequence object
sequence = RNA.fold_compound(rna_sequence)

# Predict the minimum free energy (MFE) secondary structure
mfe_structure, mfe_energy = sequence.mfe()

# Save the secondary structure in dot-bracket notation
with open("rna_structure.dbn", "w") as dbn_file:
    dbn_file.write(mfe_structure)

print("MFE Secondary Structure:", mfe_structure)
print("MFE Energy:", mfe_energy)
