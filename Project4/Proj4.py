#Author: Milan Patel

with open('rosalind_hamm.txt', 'r') as myfile:
		data=myfile.readlines()

referenceDNA=str(data[0])
comparisonDNA=str(data[1])
hammDistance=0

for i, x in enumerate(referenceDNA):
	if x!=comparisonDNA[i]:
		hammDistance+=1
	else:
		continue

print(hammDistance)