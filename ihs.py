#! /usr/bin/python
import numpy,glob

# with open ("dmel.005.X.nsl.out.100bins.norm") as f:
# 	ihs_out=[x.split() for x in f]

# #Store all the unstandardized ihs in the list ihs_v[]
# ihs_v=[]
# ihs_dic={}
# for item in ihs_out:
# 	ihs_v.append(float(item[6]))
# 	posi=item[1]
# 	score=float(item[6])
# 	ihs_dic[posi]=score
# ihs_mean=numpy.mean(ihs_v)
# ihs_sd=numpy.std(ihs_v)

# #Normalize iHS 
# ihs_stand={}
# for snow in ihs_dic:
# 	flake=ihs_dic[snow]
# 	stand_ihs=(flake-ihs_mean)/ihs_sd
# 	ihs_stand[snow]=stand_ihs

# #Write the ID, position and standardized iHS in a new file
# f1=open("dmel.X.005.norm.standnsl",'w')
# for light in ihs_stand:
# 	bulb=ihs_stand[light]
# 	f1.write(light+'\t'+str(ihs_stand[light])+'\n')
# f1.close()

path1=glob.glob("*.100bins.norm")

for files in path1:
	print files
	with open (files) as f:
		ihs_out=[x.split() for x in f]
	ihs_v=[]
	ihs_dic={}
	for item in ihs_out:
		ihs_v.append(float(item[6]))
		posi=item[1]
		score=float(item[6])
		ihs_dic[posi]=score
	ihs_mean=numpy.mean(ihs_v)
	ihs_sd=numpy.std(ihs_v)
	ihs_stand={}
	for snow in ihs_dic:
		flake=ihs_dic[snow]
		stand_ihs=(flake-ihs_mean)/ihs_sd
		ihs_stand[snow]=stand_ihs
	standf=files+".stand"
	f1=open(standf,'w')
	for light in ihs_stand:
		bulb=ihs_stand[light]
		f1.write(light+'\t'+str(ihs_stand[light])+'\n')
	f1.close()
