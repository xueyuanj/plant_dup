bra_ory_dic={}
with open("integrative_orthology_anchor_point.csv.bra_ory.all") as f:
	ever=f.readlines()
	blacklist=[]
	for make in ever:
		id1=make.split()[0]
		id2=make.split()[1]
		bra_ory_dic[id2]=id1
		bra_ory_dic[id1]=id2

bra_sor_dic={}
with open("integrative_orthology_anchor_point.csv.bra_sor.all") as f:
	ever=f.readlines()
	blacklist=[]
	for make in ever:
		id1=make.split()[0]
		id2=make.split()[1]
		bra_sor_dic[id1]=id2
		bra_sor_dic[id2]=id1


ory_sor_dic={}
with open("integrative_orthology_anchor_point.csv.ory_sor.all") as f:
	ever=f.readlines()
	blacklist=[]
	for make in ever:
		id1=make.split()[0]
		id2=make.split()[1]
		ory_sor_dic[id1]=id2
		ory_sor_dic[id2]=id1


i=0
with open("Oryza.dups.SorghumAncestral.noclade.twooutg.ids") as f:
	f1=open("ory.sor.noclade.twooutg.anchor_point", 'w')
	pen=f.readlines()
	for ink in pen:
		dup1=ink.split()[0]
		dup2=ink.split()[1]
		anc=ink.split()[2]
		try:
			anchor_point=ory_sor_dic[anc]
			f1.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
			i+=1
		except KeyError:
			pass

print i, len(pen)

j=0
with open("Sorghum.dups.OryzaAncestral.noclade.twooutg.ids") as f:
	f2=open("sor.ory.noclade.twooutg.anchor_point", 'w')
	pen=f.readlines()
	for ink in pen:
		dup1=ink.split()[0]
		dup2=ink.split()[1]
		anc=ink.split()[2]
		try:
			anchor_point=ory_sor_dic[anc]
			f2.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
			j+=1
		except KeyError:
			pass

print j, len(pen)



i=0
with open("Brachypodium.dups.SorghumAncestral.noclade.twooutg.ids") as f:
	f3=open("bra.sor.noclade.twooutg.anchor_point", 'w')
	pen=f.readlines()
	for ink in pen:
		dup1=ink.split()[0]
		dup2=ink.split()[1]
		anc=ink.split()[2]
		try:
			anchor_point=bra_sor_dic[anc]
			f3.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
			i+=1
		except KeyError:
			pass

print i, len(pen)

j=0
with open("Sorghum.dups.BrachypodiumAncestral.noclade.twooutg.ids") as f:
	f4=open("sor.bra.noclade.twooutg.anchor_point", 'w')
	pen=f.readlines()
	for ink in pen:
		dup1=ink.split()[0]
		dup2=ink.split()[1]
		anc=ink.split()[2]
		try:
			anchor_point=bra_sor_dic[anc]
			f4.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
			j+=1
		except KeyError:
			pass

print j, len(pen)


i=0
with open("Brachypodium.dups.OryzaAncestral.noclade.twooutg.ids") as f:
	f5=open("bra.ory.noclade.twooutg.anchor_point", 'w')
	pen=f.readlines()
	for ink in pen:
		dup1=ink.split()[0]
		dup2=ink.split()[1]
		anc=ink.split()[2]
		try:
			anchor_point=bra_ory_dic[anc]
			f5.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
			i+=1
		except KeyError:
			pass

print i, len(pen)

j=0
with open("Oryza.dups.BrachypodiumAncestral.noclade.twooutg.ids") as f:
	f6=open("ory.bra.noclade.twooutg.anchor_point", 'w')
	pen=f.readlines()
	for ink in pen:
		dup1=ink.split()[0]
		dup2=ink.split()[1]
		anc=ink.split()[2]
		try:
			anchor_point=bra_ory_dic[anc]
			f6.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
			j+=1
		except KeyError:
			pass

print j, len(pen)



# i=0
# with open("Brachypodium_Oryza.dups.usingBrachyDups") as f:
# 	f7=open("bra_ory.bra.noclade.twooutg.anchor_point", 'w')
# 	pen=f.readlines()
# 	for ink in pen:
# 		dup1=ink.split()[0]
# 		dup2=ink.split()[1]
# 		anc=ink.split()[2]
# 		try:
# 			anchor_point=bra_sor_dic[anc]
# 			f7.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
# 			i+=1
# 		except KeyError:
# 			pass

# print i, len(pen)


# i=0
# with open("Brachypodium_Oryza.dups.usingOryzaDups") as f:
# 	f8=open("bra_ory.ory.noclade.twooutg.anchor_point", 'w')
# 	pen=f.readlines()
# 	for ink in pen:
# 		dup1=ink.split()[0]
# 		dup2=ink.split()[1]
# 		anc=ink.split()[2]
# 		try:
# 			anchor_point=ory_sor_dic[anc]
# 			f8.write(dup1+"\t"+dup2+"\t"+anchor_point+"\t"+"anchor_point"+"\n")
# 			i+=1
# 		except KeyError:
# 			pass

# print i, len(pen)