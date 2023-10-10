import RNA

# Your RNA sequence
rna_sequence = "AUGCGUACGAUCGAUCGAUCGAU"

# Create an RNA sequence object
sequence = RNA.fold_compound(rna_sequence)

# Predict the secondary structure and its energy
mfe_structure, mfe_energy = sequence.mfe()

print("MFE Structure:", mfe_structure)
print("MFE Energy:", mfe_energy)
