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
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import *

input_file = 'HBA_BOTH_padded.fasta'
aln = AlignIO.read(input_file, "fasta")

starting_tree = Phylo.read("HBA_both_distance_tree.xml", 'phyloxml')
scorer = ParsimonyScorer()
searcher = NNITreeSearcher(scorer)
constructor = ParsimonyTreeConstructor(searcher, starting_tree)
pars_tree = constructor.build_tree(aln)

Phylo.write(pars_tree, "HBA_both_parsimony_tree.xml","phyloxml")
print pars_tree