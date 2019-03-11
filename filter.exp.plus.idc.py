import glob, re, math

######################################################
# Get the ID conversion table in a dictionary
idconvert={}

idf1=open("id_conversion.bdi.csv", "r")
idf2=open("RAP-MSU_2017-08-04.txt", "r")
idf3=open("Sorghum.TPM.tsv.temp", "r")

soridc=idf3.readlines()[1:]
for flower in soridc:
	sorid=flower.split()[0]
	sorconverted=sorid.upper()
	idconvert[sorid]=sorconverted

oridc=idf2.readlines()
for petal in oridc:
	id1=petal.split()[0].upper()
	id2=petal.split()[1]
	if id2=="None":
		pass
	else:
		potential=id2.split(",")[0].upper()
		rapid=re.search("OS\w+", potential).group(0)
		idconvert[id1]=rapid
		#print id1, rapid

bradic=idf1.readlines()[1:]
for stem in bradic:
	plaid=stem.split(";")[0][1:-1]
	geneinfor=stem.split(";")[1][1:-1]
	anotherid=stem.split(";")[2][1:-2].upper()
	if geneinfor=="GeneName":
		idconvert[anotherid]=plaid
		


######################################################
# Clean the expression data
path1=glob.glob("*.TPM.tsv.temp")

for files in path1:
	expdf=open(files, "r")
	newfile=files.split(".")[0]+".TPM.log2trans.highexp.txt"
	newdf=open(newfile, "w")
	expdata=expdf.readlines()
	header=expdata[0]
	newdf.write(header)
	realdata=expdata[1:]
	for glide in realdata:
		#print glide.split()[0]
		try:
			workingid = idconvert[glide.split()[0]]
			#print workingid
			j=0
			for i in range(1,10):
				if float(glide.split()[i]) < 1:
					j+=1
			if j==9:
				pass
			else:
				newdf.write(workingid+"\t")
				for k in range(1,10):
					trans=math.log(float(glide.split()[k])+1, 2) # log2(exp+1), in case it's 0.
					newdf.write(str(trans)+"\t")
				newdf.write("\n")
		except KeyError:
			pass
	newdf.close()

