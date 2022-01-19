""" import sys, csv, pysam 
fasta_file = pysam.FastaFile(sys.argv[1]) 
with open(sys.argv[2], 'wb') as csvfile: 
    fasta_writer = csv.writer(csvfile, delimiter=',') 
    fasta_writer.writerow(['Ref','Length','Seq']) 
    for ref in fasta_file.references: 
    	fasta_writer.writerow([ref, fasta_file.get_reference_length(ref), fasta_file.fetch(ref)])  """

from Bio import SeqIO
import pandas as pd
from pandas import Series,DataFrame
import csv
# import mysql.connector
# from mysql.connector import Error



# parse sequence fasta file
identifiers = [seq_record.id for seq_record in SeqIO.parse("fastafile.fasta",
                                                           "fasta")]
lengths = [len(seq_record.seq) for seq_record in SeqIO.parse("fastafile.fasta",
                                                             "fasta")]
# converting lists to pandas Series
s1 = Series(identifiers, name='ID')
s2 = Series(lengths, name='length')
# Gathering Series into a pandas DataFrame and rename index as ID column
Qfasta = DataFrame(dict(ID=s1, length=s2)).set_index(['ID'])
demo = Qfasta.to_csv("demo.csv")

""" 
pip install seqio
pip install biopython
 """