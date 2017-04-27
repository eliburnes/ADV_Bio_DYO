import sys
print(sys.path)
sys.path.append("/Users/Eli/biopython-1.68")
sys.path.append("/Users/Eli/miniconda2/lib/python2.7/site-packages")
sys.path.append("/opt/local/var/macports/sources/rsync.macports.org/release/tarballs/ports/graphics")
from Bio import Phylo


tree = Phylo.read('HBA_both_parsimony_tree.xml', 'phyloxml')

Phylo.write(tree,'HBA_both_parsimony_tree.nwk','newick')