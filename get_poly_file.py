#Cut the position and substitution information out from the dgrp2.tgeno file. Name the new file polymorphism.txt. Read the polymorphism file 
f3=open("Sbicolor_313.vcf", 'r')
f4=open("sbi.poly.single.txt", 'w')

poly=f3.readlines()
for poly_1 in poly:
	if "#" in poly_1:
		pass
	else:
		poly_=poly_1.split()
		if len(poly_[3])!=1 or len(poly_[4])!=1:
			pass
		else:
			for stuff in poly_:
				f4.write(stuff.split(":")[0]+"\t")
			f4.write('\n')
f3.close()
f4.close()