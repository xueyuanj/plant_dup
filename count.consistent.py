import glob


# def summary(files):
# 	with open(files) as f:
# 		present=[]
# 		i=0
# 		j=0
# 		paste=f.readlines()
# 		for tooth in paste:
# 			rawc=tooth.split()[0]
# 			if rawc=="3":
# 				j+=1
# 			dup1=tooth.split()[1]
# 			if dup1 in present:
# 				present.remove(dup1)
# 			else:
# 				i+=1
# 				present.append(dup1)
# 		print files, i, j

# path=glob.glob("*.count")

# for data in path:
# 	summary(data)


def summary(files):
	with open(files) as f:
		present={}
		paste=f.readlines()
		for tooth in paste:
			dup1=tooth.split()[0]
			dup2=tooth.split()[1]
			anc=tooth.split()[2]
			dup1=dup1+"_"+dup2+"_"+anc
			assign=tooth.split()[3]
			source=tooth.split()[4]
			if dup1 not in present:
				present[dup1] = [assign, source]
			else:
				there=present[dup1]
				pre_assign=there[0]
				if pre_assign== assign:
					there.append(source)
					present[dup1]=there
				else:
					note="*.not."+source
					there.append(note)
					present[dup1]=there
	return present


path=glob.glob("*.bdi_osa_common_osa.temp")

f1=open("consistent.table.bdi_osa_common_osa.count_gain06", "w")

for data in path:
	allinfor=summary(data)
	print allinfor
	for genes in allinfor:
		dup1=genes.split("_")[0]
		dup2=genes.split("_")[1]
		ances=genes.split("_")[2]
		f1.write(dup1+"\t"+dup2+"\t"+ ances+"\t")
		i=0
		assignments=allinfor[genes]
		for stuff in assignments:
			if "*.not" in stuff:
				i+=1
		if i==2:
			assigned=assignments[0]
			if dup1==assigned:
				major=dup2
			else:
				major=dup1
			# When ORTHO is the only one that doesn't agree with the two, add *.not. to ORTHO
			f1.write(major+"\t"+ "*.not.anchor_point"+"\t"+"ORTHO"+"\t"+"TROG"+"\n")
		else:
			major=assignments[0]
			f1.write(major+"\t")
			for j in range(1,len(assignments)):
				f1.write(assignments[j]+"\t")
			f1.write("\n")

f1.close()
