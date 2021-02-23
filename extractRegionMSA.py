from Bio import SeqIO
import sys

readsList = open(sys.argv[1], 'rU')
output = open(sys.argv[2], 'w')
start = int (sys.argv[3])
end = int (sys.argv[4])

size = 1273
#count = 0

for record in SeqIO.parse(readsList, "fasta"):
    seq = str(record.seq)
    seqL = seq.strip()
    output.write('>' + record.id + '\n')
    output.write(seqL[(start-1):end])
    output.write('\n')
    if len(seqL) != size:
        print(record.id)
        print('\n')
        print(len(seqL))
    #if count == 0:
        #print(seqL)
    #count = count + 1


readsList.close()
output.close

#run
#python3 extractRegion.py <multialignment.fasta file> <outputFile.fasta file> <number where start extraction> <number where extraction ends>