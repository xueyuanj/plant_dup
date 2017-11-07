f1=open("table.parent1.child2.noclade.twooutg.txt", "w")

with open("consistent.table.all.noclade.twooutg") as f:
	cough=f.readlines()
	for syrup in cough:
		infor=syrup.split()
		dup1=infor[0]
		dup2=infor[1]
		assign=infor[2]
		# The only situation worth considering is when 2 conflicting sources are available
		# ORTHO > anchor_point > TROG
		if "*.not." in syrup and len(infor)==5 :
			#print syrup
			source1=infor[3]
			source2=infor[4]
			if source1=="ORTHO":
				parent=assign
				if dup1==parent:
					child=dup2
				else:
					child=dup1
			else:
				child=assign
				if dup1==child:
					parent=dup2
				else:
					parent=dup1
		else:
			parent=assign
			if dup1==parent:
				child=dup2
			else:
				child=dup1
		f1.write(parent+"\t"+ child+"\n")

f1.close()