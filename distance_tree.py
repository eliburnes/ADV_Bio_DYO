import sys
print(sys.path)
sys.path.append("/Users/Eli/biopython-1.68")
from Bio import AlignIO
from Bio import SeqIO
from Bio import Seq
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
import os

calculator = DistanceCalculator('identity')
constructor=DistanceTreeConstructor(calculator, 'nj')

input_file = 'HBA_BOTH_padded.fasta'
alignment = AlignIO.read(input_file, "fasta")
tree=constructor.build_tree(alignment)

Phylo.write(tree, "HBA_both_distance_tree.xml","phyloxml")
print tree

"""records = SeqIO.parse(input_file, 'fasta')
records = list(records) # make a copy, otherwise our generator
                        # is exhausted after calculating maxlen
maxlen = max(len(record.seq) for record in records)

# pad sequences so that they all have the same length
for record in records:
    if len(record.seq) != maxlen:
        sequence = str(record.seq).ljust(maxlen, '.')
        record.seq = Seq.Seq(sequence)
assert all(len(record.seq) == maxlen for record in records)

# write to temporary file and do alignment
output_file = '{}_padded.fasta'.format(os.path.splitext(input_file)[0])
with open(output_file, 'w') as f:
"""