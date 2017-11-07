import re

def split(genome_f):
	gname=re.search("\w+", genome_f).group(0)
	with open(genome_f) as f:
		soft=f.readlines()
		for cream in soft:
			if ">" in cream:
				chrname=re.search("(?<=>)\S+", cream).group(0)
				newname=gname+"."+chrname+".fasta"
				print newname
				newfile=open(newname, 'w')
			else:
				newfile.write(cream)


#split("bdi.con")
split("osa.con")
split("sbi.con")
