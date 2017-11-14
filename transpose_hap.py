#! /usr/bin/python
import glob

# #Store all the polymorphism data in the list lis
# with open("dgrp_X_imput.vcf") as f:
#     lis = [x.split() for x in f]

# #Transpose the file
# result = [['foo' for i in range(len(lis))] for j in range (205)]
# for i in range(len(lis)):
# 	for j in range(len(lis[0])):
# 		result[j][i]=lis[i][j]
 
# #Replace diploid symbols with haploid ones. 
# f1= open("dgrp_X.hap",'w') 
# for items in result:
# 	for stuff in items:
# 		if stuff=='0|0':
# 			stuff='0'
# 		else:
# 			stuff='1'
# 		f1.write(str(stuff)+ ' ')
# 	f1.write('\n')


hapfiles=glob.glob("./bdi_poly*_imputed.vcf")

for files in hapfiles:
	with open(files) as f:
		lis = [x.split() for x in f]
	result = [['foo' for i in range(len(lis))] for j in range (53)]
	for i in range(len(lis)):
		for j in range(len(lis[0])):
			result[j][i]=lis[i][j]
	newfile=files.split(".")[0]+".hap"
	f1= open(newfile,'w') 
	for items in result:
		for stuff in items:
			if stuff=='0|0':
				stuff='0'
			else:
				stuff='1'
			f1.write(str(stuff)+ ' ')
		f1.write('\n')
 

