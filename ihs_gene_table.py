#! /usr/bin/python
import re, glob

#Check if input value is within a givin interval. 
def check_v(value, inter):
    min_=inter[0]
    max_=inter[1]
    if value >= min_ and value<=max_:
        return True
    else:
        return False

"""
#Get the gene id and coordinates in a dictionary.
f1=open('dmel-all-r5.49.geneids.X', 'r')
vase=f1.readlines()
dmel={}
for waterlily in vase:
	geneid=waterlily.split()[0]
	lowerb=waterlily.split()[2]
	upperb=waterlily.split()[3]
	dmel[geneid]=[int(lowerb), int(upperb)]
f1.close()

#Get the SNP data
f2=open("dmel.X.005.norm.standnsl", 'r')
snp={}
balloon=f2.readlines()
for air in balloon:
	snppos=air.split()[0]
	snpihs=air.split()[1]
	snp[snppos]=float(snpihs)
f2.close()

#Write the SNP id, position on the chromosome and gene into a table.
with open("dmel.005.X.r549.anno.norm.tab", 'w') as f:
	for monitor in snp:
		ihs=snp[monitor]
		monitor=int(monitor)
		for cpu in dmel:
			coordinate=dmel[cpu]
			if check_v(monitor,coordinate):
				f.write(str(monitor)+'\t'+"gene"+'\t'+str(cpu)+'\t'+str(ihs)+'\n')
"""

# path1=glob.glob("bdi.*.nsl.nsl.out.100bins.norm.stand")

# for files in path1:
# 	f1name=files+".genes"
# 	f1=open(f1name, "w")
# 	species=files.split(".")[0]
# 	chrom=files.split(".")[1]
# 	chromnum=re.search("\d+", chrom).group(0)
# 	expectchr="Bd"+chromnum
# 	annofile="anno."+species+".gene.gff"
# 	annoinfor=open(annofile, "r")
# 	annodf=annoinfor.readlines()
# 	annodic={}
# 	for annolines in annodf:
# 		annochr=annolines.split()[0]
# 		annostart=annolines.split()[4]
# 		annoend=annolines.split()[5]
# 		annoidinfor=annolines.split()[9]
# 		annoid=re.search("(?<=ID=)\w+", annoidinfor).group(0)
# 		if annochr==expectchr:
# 			annodic[annoid]=[int(annostart), int(annoend)]
# 	snpfile=open(files, "r")
# 	snpdata=snpfile.readlines()
# 	for xixi in snpdata:
# 		snppos=int(xixi.split()[0])
# 		snpnsl=xixi.split()[1]
# 		for genecoord in annodic:
# 			coor=annodic[genecoord]
# 			if check_v(snppos, coor):
# 				f1.write("gene"+"\t"+str(snppos)+"\t"+genecoord+"\t"+snpnsl+"\n" )
# 	f1.close()
		


path1=glob.glob("sbi.*.nsl.nsl.out.100bins.norm.stand")

for files in path1:
	f1name=files+".genes"
	f1=open(f1name, "w")
	species=files.split(".")[0]
	chrom=files.split(".")[1]
	chromnum=re.search("\d+", chrom).group(0)
	expectchr="chr_"+chromnum
	annofile="anno."+species+".gene.gff"
	annoinfor=open(annofile, "r")
	annodf=annoinfor.readlines()
	annodic={}
	for annolines in annodf:
		annochr=annolines.split()[0]
		annostart=annolines.split()[4]
		annoend=annolines.split()[5]
		annoidinfor=annolines.split()[9]
		annoid=re.search("(?<=ID=)\w+", annoidinfor).group(0)
		if annochr==expectchr:
			annodic[annoid]=[int(annostart), int(annoend)]
	snpfile=open(files, "r")
	snpdata=snpfile.readlines()
	for xixi in snpdata:
		snppos=int(xixi.split()[0])
		snpnsl=xixi.split()[1]
		for genecoord in annodic:
			coor=annodic[genecoord]
			if check_v(snppos, coor):
				f1.write("gene"+"\t"+str(snppos)+"\t"+genecoord+"\t"+snpnsl+"\n" )
	f1.close()
		

