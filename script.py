# code  to subtract heasers and sequences of fasta file  
""" import sys
import matplotlib

sequences = {}

with open('fastafile.fasta') as fasta:
    header = None
    data = ''

    for line in fasta:
        if line.startswith('>'):
            if header and data:
                sequences[header] = data
            data = ''
            header = line.rstrip()
        else:
            data += line.rstrip()

    if header and data:
        sequences[header] = data  

for header, data in sequences.items():
    print('{}; {}bp'.format(header, len(data)))



sequences2 = {}

with open('fastafile.fasta') as fasta2:
    header = None
    data = ''

    for line in fasta2:
        if line.startswith('M'):
            if header and data:
                sequences2[header] = data
            data = ''
            header = line.rstrip()
        else:
            data += line.rstrip()

    if header and data:
        sequences2[header] = data  

for header, data in sequences2.items():
    print('{}; {}bp'.format(header, len(data))) """




# code to convert it into csv file 
""" 
from Bio import SeqIO
import pandas as pd
from pandas import Series,DataFrame
import csv




# parse sequence fasta file
identifiers = [seq_record.id for seq_record in SeqIO.parse("fastafile.fasta",
                                                           "fasta")]
lengths = [len(seq_record.seq) for seq_record in SeqIO.parse("fastafile.fasta",
                                                             "fasta")]
Description = [(seq_record.description) for seq_record in SeqIO.parse("fastafile.fasta",
                                                             "fasta")]
# converting lists to pandas Series
s1 = Series(identifiers, name='ID')
s2 = Series(lengths, name='length')
s3 = Series(Description, name='description')
# Gathering Series into a pandas DataFrame and rename index as ID column
#Qfasta = DataFrame(dict(ID=s1, length=s2)).set_index(['ID'])
# demo = Qfasta.to_csv("demo.csv")
#print(s2)
print(s3) """

""" ## learning to parse a fasta file with python [duplicate]
import re 

dna = []
sequences = []

filename = 'fastafile.fasta'
def read_fasta(filename):
    global seq, header, dna, sequences 

#open the file  
    with open(filename) as file:    
        seq = ''        
        #forloop through the lines
        for line in file: 
            header = re.search(r'^>\w+', line)
            #if line contains the header '>' then append it to the dna list 
            if header:
                line = line.rstrip("\n")
                dna.append(line)            
            # in the else statement is where I have problems, what I would like is
            #else: 
                #the proceeding lines before the next '>' is the sequence for each header,
                #concatenate these lines into one string and append to the sequences list 
            else:               
                seq = line.replace('\n', '')  
                sequences.append(seq)      



read_fasta(filename) """


""" # solution to convert a multifasta file to csv
from Bio import SeqIO
for re in SeqIO.parse('fastafile.fasta', 'fasta'):
    print('>{}\t{}'.format(str(re.description).replace('|', '\t'), re.seq)) """

# How does one convert fasta to CSV using python?
#https://qr.ae/pGBvFF
# import sys, csv, pysam 
# fasta_file = pysam.FastaFile(sys.argv[1]) 
# with open(sys.argv[2], 'wb') as csvfile: 
#     fasta_writer = csv.writer(csvfile, delimiter=',') 
#     fasta_writer.writerow(['Ref','Length','Seq']) 
#     for ref in fasta_file.references: 
#     	fasta_writer.writerow([ref, fasta_file.get_reference_length(ref), fasta_file.fetch(ref)]) 