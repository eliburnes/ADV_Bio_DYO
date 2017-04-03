import dendropy

HBA_both=dendropy.ProteinCharacterMatrix.get(file=open("HBA_Tetrapod+fish.fasta"), schema="fasta")
HBA_both_tree=dendropy.Tree(HBA_both)
print HBA_both.description(2)