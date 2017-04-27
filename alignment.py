import sys
print(sys.path)
import numpy
sys.path.append("/Users/Eli/biopython-1.68")
from Bio import AlignIO
from Bio import SeqIO
from Bio import Seq
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
import os

calculator = DistanceCalculator('blosum62') #note blosum cannot take padding with "." characters
constructor=DistanceTreeConstructor(calculator, 'nj')

numpy.set_printoptions(threshold=numpy.nan)

input_file = 'HBB_BOTH_padded.fasta'
alignment = AlignIO.read(input_file, "fasta")

dm = calculator.get_distance(alignment)


print dm

"""
print dm

mine=[]

for element in dm:
    mine.append(numpy.array(element))

averages=[]
total=0
total_length=0
total_array=[]
numpy.array(total_array)


for x in range (len(mine)):
    print mine[x]
    sum = numpy.sum(mine[x])
    total=total+sum
    length = len(mine[x])-1
    total_length=total_length+length
    averages.append(sum/length)
    for element in mine[x]:
        if element!=0:
            total_array.append(element)

print numpy.average(averages)
print total/total_length
print averages
print "*****************************"
print numpy.average(total_array)
print numpy.std(total_array)
print total_array


"""

leppa=dm[0]
latch=dm[1]

numpy.array(leppa)
numpy.array(latch)

leppa=leppa[2:]
latch=latch[2:]

print leppa
print latch


lungfish_avg=numpy.average(leppa)
coelecanth_avg=numpy.average(latch)

lungfish_std=numpy.std(leppa)
coelecanth_std=numpy.std(latch)

print lungfish_avg
print coelecanth_avg

print lungfish_std
print coelecanth_std



