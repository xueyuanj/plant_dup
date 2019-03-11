import glob

path=glob.glob("./plaza.single.1to1to1.aligned/*_NT.fasta")


for files in path:
	print files
	with open(files) as f:
		ring=f.read()
		ring=ring.replace("!", "-")
		with open(files,"w") as f1:
			f1.write(ring)
			

 
