with open('rosalind_iprb.txt', 'r') as myfile:
		data=myfile.read().split()

homoDom=int(data[0])
het=int(data[1])
homoRec=int(data[2])

totalOrgs=homoRec+het+homoDom
hetHomoRec=0.5
hetHet=0.75

dominantTree = (homoDom/totalOrgs)

heterozygousTree = ((het/totalOrgs)*(homoDom/(totalOrgs-1))+(het/totalOrgs)*((het-1)/(totalOrgs-1))*hetHet+ \
					(het/totalOrgs)*(homoRec/(totalOrgs-1))*hetHomoRec)

recessiveTree = ((homoRec/totalOrgs)*(homoDom/(totalOrgs-1))+(homoRec/totalOrgs)*(het/(totalOrgs-1))*hetHomoRec)


probDominant = dominantTree + heterozygousTree + recessiveTree

print(probDominant)
