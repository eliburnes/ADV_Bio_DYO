import sys
print(sys.path)
sys.path.append("/Users/Eli/biopython-1.68")
sys.path.append("/Users/Eli/miniconda2/lib/python2.7/site-packages")
sys.path.append("/opt/local/var/macports/sources/rsync.macports.org/release/tarballs/ports/graphics")
import pylab
import networkx as nx
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout

from Bio import AlignIO
from Bio import SeqIO
from Bio import Seq

from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
import os

from Bio import Phylo


tree = Phylo.read('HBA_both_parsimony_tree.xml', 'phyloxml')
#tree2 = Phylo.read('HBA_both_distance_tree.xml', 'phyloxml')
#tree.ladderize()   # Flip branches so deeper clades are displayed at top
#tree2.ladderize()

Phylo.draw(tree)
