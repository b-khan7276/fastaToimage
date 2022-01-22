""" 
To taken from 
https://github.com/drewk2021/fastatocsv
 """
""" import fastatocsv
from fastatocsv import converter 
fastatocsv.converter.convert("fastafile.fasta","convert_fastafile_to_csv.csv") """
""" 
import fastatocsv 
#from fastatocsv import convertWithAttributes

converter.convertWithAttributes("fastafile.fasta.fasta","new.csv") """

import sys, os

def convert(input,output):
    """
    Purpose: To convert a .fasta file of >= 1 sequence(s) into a .csv file, with
    two columns, one containing the headline identifier, the other containing the
    sequence.
    Parameters: the input .fasta file path, a string, and the desired .csv output
    path, another string.
    Return: the output path, a string.
    """
    if not os.path.exists(input):
        raise IOError(errno.ENOENT, 'No such file', input)

    # Read in Fasta
    fasta = open(input, 'r')
    fasta_lines = fasta.readlines()
    seq = {}
    seqs = []

    for line in fasta_lines:

        if line[0] == ">": # head line with description
            seqs += [seq] # adding dicitionary to broader list
            seq_local = {}
            seq_head = line.strip(">\n")
            seq_local["seq_type"] = seq_head # identifier
            seq_local["seq"] = "" # actual sequence
            seq = seq_local


        else: # sequence line
            seq["seq"] += line.strip("\n")


    fasta.close()

    # Convert fasta to csv
    seqs.pop(0) # removing first (empty) item in seqs list i.e. fencepost
    csv_lines = ["Properties, Sequence\n"]
    for seq in seqs:
        csv_line = seq["seq_type"] + "," + seq["seq"] + "\n"
        csv_lines += csv_line


    # Output csv file
    csv = open(output, 'w')
    csv.writelines(csv_lines)
    csv.close()
    return output

convert('fastafile.fasta', 'newfastatocsvsecondfile.csv')