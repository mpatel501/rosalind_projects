with open('rosalind_dna.txt', 'r') as myfile:
		data=myfile.read().replace('\n', '')

s=str(data.count("A")) + ' ' + str(data.count("C")) + ' ' + str(data.count("G")) + ' ' + str(data.count("T"))
print(s)