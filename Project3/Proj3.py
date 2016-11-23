#Author: Milan Patel

with open('rosalind_revc.txt', 'r') as myfile:
		data=myfile.read().replace('\n', '')

dna=str(data)
dnaComplement=[]

for x in dna:

	if x=='A':
		dnaComplement.append('T')
		continue
	elif x=='T':
		dnaComplement.append('A')
		continue
	elif x=='C':
		dnaComplement.append('G')
		continue
	else:
		dnaComplement.append('C')
		continue

dnaReverse=''.join(str(x) for x in dnaComplement)
dnaReverse=dnaReverse[::-1]
print(dnaReverse)