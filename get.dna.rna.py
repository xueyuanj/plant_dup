import re, glob

path1=glob.glob("*.exons.csv")

exonnumdic={}

for files in path1:
	exonf=open(files, "r")
	exondf=exonf.readlines()
	for funnel in exondf:
		geneid=funnel.split(";")[0][1:-1]
		coordi=funnel.split(";")[1]
		exons=coordi.split(",")
		exonnumdic[geneid] =len(exons)
print exonnumdic

path2=glob.glob("*.merge")
for files in path2:
	newfile=files+".dna_rna"
	newdf=open(newfile, "w")
	classi=open(files, "r")
	binder=classi.readlines()
	for paper in binder:
		pid=paper.split()[0]
		cid=paper.split()[1]
		try:
			pexonlen=exonnumdic[pid]
			cexonlen=exonnumdic[cid]
			if pexonlen>1 and cexonlen>1:
				repmech="DNA"
			elif pexonlen>1 and cexonlen==1:
				repmech="RNA"
			else:
				repmech="unknown"
			newdf.write(paper.strip("\n")+"\t"+repmech+"\n" )
		except KeyError:
			print "not found"
	newdf.close()