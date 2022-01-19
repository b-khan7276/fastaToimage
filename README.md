# Fasta To Image
## converting fasta file into Csv
- I first convert fsata file into csv file using python script
- using modules in main.py file 
```bash
pip install seqio
pip install biopython
```
- I divide fasta file into identifiers and lengths
- I named Identifies as ID
- I named Length as Length
- Than I name the output csv file as demo.csv

## Converting csv file into image/graphs

- In Jupyter notebook 
- I import pandas
- and matplotlib
- than Import demo.csv file

I convert data of the csv file into graphy by 
```python
plt.plot(fasta_data.ID, fasta_data.length)
plt.show()
```
- Than I compare Two IDs with each other
- and show in graph
