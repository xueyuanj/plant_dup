
def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]

expdic={}

newf=open("Sorghum.TPM.log2trans.highexp.txt,clean", "w")

with open("Sorghum.TPM.log2trans.highexp.txt") as f:
	soft=f.readlines()
	for cream in soft:
		gid=cream.split()[0]
		infor=cream.split()[1:]
		#print infor
		if gid in expdic:
			print gid
			entries_to_remove(gid, infor)
		else:
			expdic[gid]=infor

for cool in expdic:
	newf.write(cool+"\t")
	expinfor=expdic[cool]
	for nivea in expinfor:
		newf.write(nivea+"\t")
	newf.write("\n")

newf.close()