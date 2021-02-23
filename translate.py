from Bio import SeqIO
import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

readsList = open(sys.argv[1], 'rU')
output = open(sys.argv[2], 'w')



for record in SeqIO.parse(readsList, "fasta"):
    protein = record.seq.translate()
    output.write('>' + record.id + '\n')
    output.write(str(protein))
    output.write('\n')


readsList.close()
output.close

#run
#python2 translate.py <sequence.fasta to translate> <output file>