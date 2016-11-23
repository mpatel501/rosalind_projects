import numpy as np
from Bio import SeqIO

max_gc = ["null", "-1"]

with open('rosalind_gc.txt', 'rU') as handle:
	records = list(SeqIO.parse(handle, "fasta"))

for i, x in enumerate(records):
	a = x.seq.count('G')
	b = x.seq.count('C')
	c = len(x.seq)
	gc = ((a+b)/c)*100

	if gc >= float(max_gc[1]):
		max_gc[0] = x.id
		max_gc[1] = str(gc)

print(max_gc)