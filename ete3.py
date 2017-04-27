import sys
print(sys.path)
sys.path.append("/Users/Eli/miniconda2/lib/python2.7/site-packages/")
sys.path.append("/Users/Eli/miniconda2/lib/python2.7/site-packages/ete3-3.0.0b36-py3.5.egg/ete3")
sys.path.append("/Users/Eli/miniconda2")

from ete3 import PhyloTree


tree = PhyloTree("HBA_BOTH_tree/clustalo_default-none-none-"
                 "fasttree_full/HBA_BOTH_padded.fasta.final_tree.nw")
tree.link_to_alignment("HBA_BOTH_tree/clustalo_default-none-none-"
                       "fasttree_full/HBA_BOTH_padded.fasta.final_tree.used_alg.fa")
tree.render("%%inline")