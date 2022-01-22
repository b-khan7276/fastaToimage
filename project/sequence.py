from Bio import SeqIO
import pandas as pd
from pandas import Series,DataFrame
import csv




# parse sequence fasta file

Description = [(seq_record.description) for seq_record in SeqIO.parse("fastafile.fasta",
                                                             "fasta")]
                                                             
# converting lists to pandas Series

s3 = Series(Description, name='description')

# Gathering Series into a pandas DataFrame and rename index as ID column
Qfasta = DataFrame(dict(Description=s3)).set_index([Description])
demo = Qfasta.to_csv("sequence.csv")