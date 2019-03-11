import glob, re




# cpassign=glob.glob("*5species.ath_outg.p1c2a3")
# childids=[]
# parentids=[]
# for files in cpassign:
# 	with open(files) as f:
# 		crest=f.readlines()
# 		for paste in crest:
# 			id1=paste.split()[0]
# 			id2=paste.split()[1]
# 			parentids.append(id1)
# 			childids.append(id2)

# print len(childids), len(parentids)


# path1=glob.glob("5species.noclade.ath_outg.phylip/Sorghum.Oryza.*child.*.paml")


# f1=open("Sorghum.Oryza.ath_outg.paml.child.results", "w")
# print len(path1)
# i=1
# for files in path1:
# 	print i
# 	with open(files) as f:
# 		bloom=f.readlines()
# 		for anchor in bloom:
# 			if "(SB" in anchor:
# 				genids1=re.search("SB\w+", anchor).group(0)
# 				genids2=re.search("OS\w+", anchor).group(0)
# 				print genids1, genids2
# 			if "t=" in anchor:
# 				#print anchor
# 				allinfor=anchor.split("=")
# 				dn=re.search("\d+\.\d+", allinfor[5]).group(0)
# 				ds=re.search("\d+\.\d+", allinfor[6]).group(0)
# 				dnds=re.search("\d+\.\d+", allinfor[4]).group(0)
# 				f1.write(genids1+"\t"+genids2+"\t"+dn+"\t"+ds+"\t"+dnds+"\n")
# 				print dn, ds, dnds
# 				i+=1
# f1.close()

# path1=glob.glob("branch.5.species.paml/parent/osa.*.paml")
# f1=open("osa.parent.branch.5species.results", "w")
# # print len(path1)

# for files in path1:
# 	with open(files) as f:
# 		bloom=f.readlines()
# 		for anchor in bloom:
# 			if "((((OS" in anchor : #and "((" in anchor and "." in anchor:
# 				#print anchor
# 				omegas=re.findall("\d+\.\d+" , anchor)
# 				ids=anchor.split(",")
# 				id1=re.search("\w+\d+\w+", ids[0]).group(0)
# 				id2=re.search("\w+\d+\w+", ids[1]).group(0)
# 				if id1 in childids:
# 					child=id1
# 					parent=id2
# 				else:
# 					child=id2
# 					parent=id1
# 				#print parent, child,omegas[0], omegas[1]
# # 				anc=re.search("\w+\d+\w+", ids[2]).group(0)
#  				f1.write(parent+"\t" +child+"\t"+omegas[0]+"\t"+omegas[1]+"\t" )
#  	f1.write("\n")

# f1.close()


# path2=glob.glob("branch.5.species.paml/child/osa.*.paml")

# f2=open("osa.child.branch.5species.results", "w")

# for files in path2:
# 	i=0
# 	with open(files) as f:
# 		bloom=f.readlines()
# 		for anchor in bloom:
# 			if "((((OS" in anchor : #and "((" in anchor and "." in anchor:
# 				#print anchor
# 				omegas=re.findall("\d+\.\d+" , anchor)
# 				ids=anchor.split(",")
# 				id1=re.search("\w+\d+\w+", ids[0]).group(0)
# 				id2=re.search("\w+\d+\w+", ids[1]).group(0)
# 				if id1 in childids:
# 					child=id1
# 					parent=id2
# 				else:
# 					child=id2
# 					parent=id1
# 				#print parent, child,omegas[0], omegas[1]
# # 				anc=re.search("\w+\d+\w+", ids[2]).group(0)
#  				f2.write(parent+"\t" +child+"\t"+omegas[0]+"\t"+omegas[1]+"\t" )
#  				i+=1
#  	if i!=4:
#  		print files
#  	f2.write("\n")

# f2.close()


# classification=glob.glob("*.p1c2a3.result1.txt")

# for files in classification:
# 	newfile=files+".branch.3species.dnds"
# 	f1=open(newfile, "w")
# 	names=files.split(".")[0]
# 	dndsfile=names+".both.branch.3species.results"
# 	classdata=open(files, "r")
# 	classdf=classdata.readlines()
# 	classdf=classdf[1:]
# 	dndsdata=open(dndsfile, "r")
# 	dndsdf=dndsdata.readlines()
# 	for cream in classdf:
# 		parent=cream.split()[0]
# 		ancestor=cream.split()[2]
# 		for whipped in dndsdf:
# 			pgene=whipped.split()[1]
# 			agene=whipped.split()[3]
# 			cdnds=whipped.split()[4]
# 			pdnds=whipped.split()[9]
# 			if pgene==parent and agene==ancestor:
# 				f1.write(cream.strip()+"\t"+ pdnds+"\t" +cdnds+"\n" ) 
#	f1.close()







# path1=glob.glob("plaza.single.1to1.phylip/bdi_osa.*.paml")
# f1=open("singlecopy.plaza30.bdi_osa.pairwise.results", "w")
# # print len(path1)

# for files in path1:
# 	with open(files) as f:
# 		bloom=f.readlines()
# 		for anchor in bloom:
# 			if "(BD" in anchor:
# 				genids1=re.search("BD\w+", anchor).group(0)
# 				genids2=re.search("OS\w+", anchor).group(0)
# 				print genids1, genids2
# 			if "t=" in anchor:
# 				#print anchor
# 				allinfor=anchor.split("=")
# 				dn=re.search("\d+\.\d+", allinfor[5]).group(0)
# 				ds=re.search("\d+\.\d+", allinfor[6]).group(0)
# 				dnds=re.search("\d+\.\d+", allinfor[4]).group(0)
# 				f1.write(genids1+"\t"+genids2+"\t"+dn+"\t"+ds+"\t"+dnds+ "\n")
# 				print dn, ds, dnds
 	

# f1.close()
			

f1=open("singlecopy.plaza30.osa.branch.results", "w")

path1=glob.glob("plaza.single.1to1to1.phylip/rice/*.paml")

for files in path1:
	print files
	with open(files) as f:
		bloom=f.readlines()
		i=0
		for anchor in bloom:
			if "((BD" in anchor : #and "((" in anchor and "." in anchor:
				i+=1
				print anchor
				omegas=re.findall("\d+\.\d+" , anchor)
				ids=anchor.split(",")
				id1=re.search("\w+\d+\w+", ids[0]).group(0)
				id2=re.search("\w+\d+\w+", ids[1]).group(0)
				id3=re.search("\w+\d+\w+", ids[2]).group(0)
				print omegas
				if i==2:
					f1.write(id1+"\t" +id2+"\t"+id3+"\t"+omegas[1]+"\t")
				if i==3:
					f1.write(omegas[1]+"\t")
				if i==4:
					f1.write(omegas[1]+"\n" )
# 				anc=re.search("\w+\d+\w+", ids[2]).group(0)
 				#f1.write(parent+"\t" +child+"\t"+omegas[0]+"\t"+omegas[1]+"\t" )
 	