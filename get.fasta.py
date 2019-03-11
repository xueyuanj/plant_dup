import glob,re

# idconvert={}

# idf1=open("id_conversion.bdi.csv", "r")



# bradic=idf1.readlines()[1:]
# for stem in bradic:
# 	plaid=stem.split(";")[0][1:-1]
# 	geneinfor=stem.split(";")[1][1:-1]
# 	anotherid=stem.split(";")[2][1:-2].upper()
# 	if geneinfor=="GeneName":
# 		idconvert[anotherid]=plaid


dic={}

path1=glob.glob("cds.*.tfa")

for files in path1:
	with open(files) as f:
		book=f.readlines()
		for page in book:
			if ">" in page:
				geneid=page.strip()
				geneid=re.search("\w+", geneid).group(0)
			else:
				seq=page.strip()
				dic[geneid]=seq



cpassign=glob.glob("singlecopy.plaza.bdi_osa_sbi.ids.txt")
# childids=[]
# parentids=[]
# for files in cpassign:
# 	with open(files) as f:
# 		crest=f.readlines()[1:]
# 		for paste in crest:
# 			id1=paste.split()[0]
# 			id2=paste.split()[1]
# 			parentids.append(id1)
# 			childids.append(id2)

for files in cpassign:
	i=1
	cfile=open(files, "r")
	spenm=files.split(".")[2]
	filedf=cfile.readlines()
	#newfasta=spenm+"."+str(i)+".geneconv.fasta"
	for secrets in filedf:
		pgene=secrets.split()[0]
		cgene=secrets.split()[1]
		agene=secrets.split()[2]
		try:
			pseq=dic[pgene]
			cseq=dic[cgene]
			aseq=dic[agene]
			# newfasta=spenm+"."+str(i)+".fasta"
			# newfile=open(newfasta, "w")
			# newfile.write(">"+ pgene+"\n"+pseq+"\n"+">"+cgene+"\n"+cseq+"\n"+">"+agene+"\n"+aseq)
			treefile=spenm+"."+str(i)+".plaza.single.tree"
			treedf=open(treefile, "w")
			treedf.write("(("+pgene+" ,"+cgene+" ) ,"+agene+" #1);")
			i+=1
		except KeyError:
			continue
		



# path2=glob.glob("duplicates.ids.ageinfor.count.gain_06.4species.*")

# for files in path2:
# 	i=1
# 	j=1
# 	with open(files) as f:
# 		spe=files.split(".")[6]
# 		#anc=files.split(".")[2]
# 		cdrom=f.readlines()[1:]
# 		for scripts in cdrom:
# 			dup1=scripts.split()[1]
# 			dup2=scripts.split()[2]
# 			ancs1=scripts.split()[3]
# 			ancs2=scripts.split()[4]
# 			ancs3=scripts.split()[5]
# 			if dup1 in childids and dup2 in parentids:
# 				thischild=dup1
# 				thisparent=dup2
# 			else:
# 				thischild=dup2
# 				thisparent=dup1
# 			newf1=spe+"."+ str(i)+".branch.4spec.fasta"
# 			f1=open(newf1, "w")
# 			try:
# 				#f1.write("\t"+"1"+"\n")
# 				f1.write(">"+dup1+ "\n" + dic[dup1]+"\n"+">"+dup2+ "\n" + dic[dup2]+"\n"+">"+ancs1+"\n"+dic[ancs1]+"\n"+">"+ancs2+"\n"+dic[ancs2]+"\n" +">"+ancs3+"\n"+dic[ancs3] )
# 				# if spe=="sbi":
# 				# 	f1.write("((("+thisparent+" #1  , "+thischild+" ), ("+ancs1+ ", "+ancs2+ "))," + ancs3+ " );" )
# 				# else:
# 				# 	f1.write("(((("+thisparent+" #1 , "+thischild+" ), " +ancs1+ "), "+ancs2+ "), "+ ancs3+ ");" )
# 				i+=1
# 			except KeyError:
# 				print dup1, newf1
# 			f1.close()
# 			# newf2=spe+"."+ anc+ ".child." + str(j)+".count.fasta"
# 			# f2=open(newf2, "w")
# 			# try:
# 			# 	f2.write(">"+dup2+ "\n" + dic[dup2]+"\n"+">"+ancs+"\n"+dic[ancs])
# 			# 	j+=1
# 			# except KeyError:
# 			# 	print dup2, newf2
# 			# f2.close()
			
"""
path2=glob.glob("table.*.bdi_osa_common_*")

for files in path2:
	i=1
	j=1
	with open(files) as f:
		spe=files.split(".")[3]
		cdrom=f.readlines()[1:]
		for scripts in cdrom:
			thisparent=scripts.split()[0]
			thischild=scripts.split()[1]
			ancs1=scripts.split()[2]
			newf1=spe+"."+ str(i)+".parent.fasta"
			f1=open(newf1, "w")
			try:
				f1.write(">"+thisparent+ "\n" + dic[thisparent]+"\n"+">"+ancs1+"\n"+dic[ancs1])
				i+=1
			except KeyError:
				print dup1, newf1
			f1.close()
			newf2=spe+"."+ str(j)+".child.fasta"
			f2=open(newf2, "w")
			try:
				f2.write(">"+thischild+ "\n" + dic[thischild]+"\n"+">"+ancs1+"\n"+dic[ancs1])
				j+=1
			except KeyError:
				print dup2, newf2
			f2.close()
			
"""
# path3=glob.glob("singles.Orthos.*.txt")

# for files in path3:
# 	i=1
# 	with open(files) as f:
# 		flower=files.split(".")[2]
# 		spe=flower.split("_")[0]
# 		anc=flower.split("_")[1]
# 		cdrom=f.readlines()
# 		for scripts in cdrom:
# 			dup1=scripts.split()[0]
# 			dup2=scripts.split()[1]
# 			#ancs=scripts.split()[2]
# 			newf1=spe+"."+ anc+ ".singles." + str(i)+".count.fasta"
# 			f1=open(newf1, "w")
# 			try:
# 				f1.write(">"+dup1+ "\n" + dic[dup1]+"\n"+">"+dup2+"\n"+dic[dup2])
# 				i+=1
# 			except KeyError:
# 				print dup1, newf1
# 			f1.close()
			


# f=open("singles.Orthos.BOS.table.txt", "r")

# i=1
# cdrom=f.readlines()
# for scripts in cdrom:
# 	dup1=scripts.split()[0]
# 	dup2=scripts.split()[1]
# 	sbi=scripts.split()[2]
# 	newf1="singles.orthomcl."+str(i)+".tree"
# 	f1=open(newf1, "w")
# 	try:
# 		trial1=dic[dup1]
# 		trial2=dic[dup2]
# 		trial3=dic[sbi]
# 		f1.write("\t"+"1"+"\n")
# 		#bdi=idconvert[dup1]
# 		#f1.write(">"+dup1+ "\n" + dic[dup1]+"\n"+">"+ dup2+"\n"+dic[dup2]+"\n"+ ">"+ sbi+"\n"+dic[sbi])
# 		f1.write("(("+dup1+"  , "+dup2+" ), " +sbi+ " #1  );" )
# 		i+=1
# 	except KeyError:
# 		print dup1, newf1
			
			

# path2=glob.glob("*.p1c2a3")
# cpassign=glob.glob("*.siqr.result1.txt")
# childids=[]
# parentids=[]
# for files in cpassign:
# 	with open(files) as f:
# 		crest=f.readlines()[1:]
# 		for paste in crest:
# 			id1=paste.split()[0]
# 			id2=paste.split()[1]
# 			parentids.append(id1)
# 			childids.append(id2)


#geneidfile=open("singles.geneids.bdi_osa_sbi_mac_ath.noclade.txt", "r")

"""
gffile=open("table.p1c2a3.count_gain06.txt", "r")

cdrom=gffile.readlines()
#cdrom=cdrom[1:]
i=1
for scripts in cdrom:
	spe=scripts.split()[17]
	#dup1=scripts.split()[18]
	dup1=scripts.split()[18]
	dup2=scripts.split()[19]
	anc1=scripts.split()[20]
	anc2=scripts.split()[21]
	#mac=scripts.split()[22]
	ath=scripts.split()[22]
	newf2="dup.phyml."+spe+"." + str(i)+".tree"
	#newf1="dup.phyml."+spe+"." + str(i)+".fasta"
	#newf2="single." + str(i)+".tree"
	if dup1 in childids and dup2 in parentids:
		thischild=dup1
		thisparent=dup2
	else:
		thischild=dup2
		thisparent=dup1
	f2=open(newf2, "w")
	f2.write("\t"+"1"+"\n")
	if spe=="sbi":
		#(((sbi1, sbi2),(bdi, osa)), ath);
		#f2.write("(((("+thisparent+", "+thischild+" ), ("+anc1+ ", "+anc2+ ")),"+mac+"), "+ath+");" )
		f2.write("((("+thisparent+" #1  , "+thischild+"), ("+anc1+ ", "+anc2+ ")), "+ath+");" )
		#f2.write("((("+thisparent+", "+thischild+" ), ("+anc1+ ", "+anc2+ ")), "+ath+");" ) ### change this line if the tree differs for parent and child
	else:
		#((( (dup1, dup2), ory/bdi),sbi), ath);
		#f2.write("((((("+thisparent+", "+thischild+" ), " +anc1+ "), "+anc2+")," +mac+"), "+ath+");" )
		f2.write("(((("+thisparent+" #1  , "+thischild+"), " +anc1+ "), "+anc2+"), " +ath+");" )  ### change this line if the tree differs for parent and child
		#f2.write("(((("+thisparent+", "+thischild+" ), " +anc1+ "), "+anc2+"), " +ath+");" )
	i+=1
	#print newf1
	# f1=open(newf1, "w")
	# try:
	# 	f1.write(">"+dup1+ "\n" + dic[dup1]+"\n"+ ">"+dup2+ "\n" + dic[dup2]+"\n"+ ">"+anc1+"\n"+dic[anc1]+"\n" +">"+anc2+"\n"+dic[anc2]+"\n" +">"+ath+"\n"+dic[ath] +"\n" )
	# 	#f2.write("(((("+bdi+", "+osa+" ), "+sbi+ "), "+mac+"), "+ath+");" )
	# 	i+=1
	# except KeyError:
	# 	print dup1
	# f1.close()

"""



"""
	newf1=spe+"."+ anc+ ".branch." + str(i)+".fasta"
	newf2=spe+"."+ anc+ ".branch." + str(i)+".tree"



for files in path2:
	i=1
	j=1
	with open(files) as f:
		spe=files.split(".")[0]
		anc=files.split(".")[2]
		cdrom=f.readlines()
		for scripts in cdrom:
			dup1=scripts.split()[0]
			dup2=scripts.split()[1]
			ancs=scripts.split()[2]
			newf1=spe+"."+ anc+ ".branch." + str(i)+".fasta"
			newf2=spe+"."+ anc+ ".branch." + str(i)+".tree"
			#f1=open(newf1, "w")
			#f2=open(newf2, "w")
			try:
				#f1.write(">"+dup1+ "\n" + dic[dup1]+"\n"+ ">"+dup2+ "\n" + dic[dup2]+"\n"+ ">"+ancs+"\n"+dic[ancs])
				#f2.write("\t"+"1"+"\n"+"(("+dup1+"  #1,"+dup2+" ) ,"+ancs+");")
				i+=1
			except KeyError:
				print dup1, newf1
			#f1.close()
			f2.close()
			#print "(("+dup1+" #1,"+dup2+" #2),"+ancs+")"


"""			
