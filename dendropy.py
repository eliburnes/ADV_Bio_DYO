import sys
print(sys.path)
sys.path.append("/usr/local/lib/python2.7/site-packages/dendropy")
import dendropy



# tree_list1 = dendropy.TreeList()
# tree_list1.read_from_path(path='HBA_both_parsimony_tree.nwk', schema="newick", collection_offset=0, tree_offset=100)
#
# tree_list1.print_plot()

t = dendropy.Tree.get_from_string("(A,(B,(C,D)))", "newick")
t.print_plot()

