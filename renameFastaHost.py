from Bio import SeqIO
import sys
from Bio import Entrez
Entrez.email = 'youremail@here' #add your email here


readsList = open(sys.argv[1], 'rU')

outputfile = open(sys.argv[2], 'w')
count = 0
for record in SeqIO.parse(readsList, "fasta"):
    count = count + 1
    accession = record.id
    #print(accession)
    genbank = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", \
                           retmode="text")
    host = ""
    for recordG in SeqIO.parse(genbank, "genbank"):
        for f in recordG.features:
            if (f.qualifiers.get('host') != None):
                host = f.qualifiers.get('host')[0]
    host = host.strip().replace(" ", "_")
    outputfile.write(">" + accession + "_" + host + "\n")
    outputfile.write((str)(record.seq))
    outputfile.write("\n")

    if (count % 100 == 0):
        print (count)
readsList.close()
outputfile.close()

#run
#python3 renameFastaHost.py <sequence.fasta input> <sequence.fasta output>