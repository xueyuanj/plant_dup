f1=open("table.p1c2a3.count_gain06.bdi_osa_common_osa.txt", "w")

with open("consistent.table.bdi_osa_common_osa.count_gain06") as f:
	cough=f.readlines()
	for syrup in cough:
		infor=syrup.split()
		dup1=infor[0]
		dup2=infor[1]
		ancg=infor[2]
		assign=infor[3]
		# The only situation worth considering is when 2 conflicting sources are available
		# ORTHO > anchor_point > TROG
		if "*.not." in syrup and len(infor)==6 :
			print syrup
			#source1=infor[4]
			source2=infor[5]
			if source2=="*.not.ORTHO":
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
		else:
			parent=assign
			if dup1==parent:
				child=dup2
			else:
				child=dup1
		f1.write(parent+"\t"+ child+"\t"+ancg+ "\n")

f1.close()