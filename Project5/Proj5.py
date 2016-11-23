#Author: Milan Patel

def fibb (x, y, z, k):
	if x>3:
		z, y=fibb(x-1,y, z, k)
	return (k*y+z, z)

n=int(input("Input # iterations: "))
m=int(input("Input reproduction rate: "))

print(fibb(n,1,1,m)[0])