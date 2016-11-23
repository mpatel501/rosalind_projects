#Author: Milan Patel

with open('rosalind_rna.txt', 'r') as myfile:
		data=myfile.read().replace('\n', '')

dnaString=str(data)
rnaString=[]

for x in dnaString:

	if x=='A':
		rnaString.append('A')
		continue
	elif x=='T':
		rnaString.append('U')
		continue
	elif x=='C':
		rnaString.append('C')
		continue
	else:
		rnaString.append('G')
		continue

rnaPrint=''.join(str(x) for x in rnaString)
print(rnaPrint)