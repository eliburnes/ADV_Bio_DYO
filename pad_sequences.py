import sys
import os
print(sys.path)
sys.path.append("/Users/Eli/biopython-1.68")
from Bio import AlignIO
from Bio import SeqIO
from Bio import Seq
import codecs


input_file = 'HBA_Tetrapod+fish.fasta'
records = SeqIO.parse(input_file, 'fasta')
records = list(records) # make a copy, otherwise our generator
                        # is exhausted after calculating maxlen
maxlen = max(len(record.seq) for record in records)

# pad sequences so that they all have the same length
for record in records:
    if len(record.seq) != maxlen:
        sequence = str(record.seq).ljust(maxlen, '.')
        record.seq = Seq.Seq(sequence)
assert all(len(record.seq) == maxlen for record in records)

SeqIO.write(records, "HBA_BOTH_padded.fasta", "fasta")