#! /usr/bin/python


# f1=open("geneticpos.txt", 'r')
# vase=f1.readlines()
# L_2=[]
# R_2=[]
# L_3=[]
# R_3=[]
# X=[]

# #For each chromosome arm, generate the list that contains the recombination rate 
# #of various positions. The position are separated in 100kb(100,000). The first
# #item is rate of 1, the second is the rate of 100000,ect.
# for flower in vase:
#     re_x=flower.split()[1]
#     chrom=flower.split()[2]
#     if chrom=='2L':
#         L_2.append(re_x)
#     elif chrom=='2R':
#         R_2.append(re_x)
#     elif chrom=='3L':
#         L_3.append(re_x)
#     elif chrom=='3R':
#         R_3.append(re_x)
#     else:
#         X.append(re_x)
# f1.close()

# #Get cumulative map from the the list.
# x_t_2L=0
# x_t_2R=0
# x_t_3L=0
# x_t_3R=0
# x_t_X=0
# L_2_c=[]
# R_2_c=[]
# L_3_c=[]
# R_3_c=[]
# X_c=[]
# for raindrop in L_2:
#     x_t_2L+= float(raindrop)
#     L_2_c.append(x_t_2L)
# for thunderstrom in R_2:
#     x_t_2R+= float(thunderstrom)
#     R_2_c.append(x_t_2R)
# for snow in L_3:
#     x_t_3L+= float(snow)
#     L_3_c.append(x_t_3L)
# for lightening in R_3:
#     x_t_3R+= float(lightening)
#     R_3_c.append(x_t_3R)
# for cloud in X:
#     x_t_X+= float(cloud)
#     X_c.append(x_t_X)


# #Create a map file. Columns are chromosome arm, ID, genetic position, and physical position 
# f2=open("poly_sub.txt", 'r')
# f3=open("dmel_recomb.map", 'w')
# bottle=f2.readlines()
# for orange_juice in bottle:
#     chromos=orange_juice.split()[0]
#     position=orange_juice.split()[1]
#     gene_id=orange_juice.split()[2]
#     posi_infor=int(position)/100000 
# #The posi_infor can be used as an index in the list file.
# #After being divided by 100000, the number correlate with the order of rate in the list.
#     if chromos == '2L':
#         rate = L_2_c[posi_infor]
#         f3.write(chromos+'\t'+gene_id+'\t'+str(rate)+'\t'+position+'\n')
#     elif chromos == '2R':
#         rate = R_2_c[posi_infor]
#         f3.write(chromos+'\t'+gene_id+'\t'+str(rate)+'\t'+position+'\n')
#     elif chromos == '3L':
#         rate = L_3_c[posi_infor]
#         f3.write(chromos+'\t'+gene_id+'\t'+str(rate)+'\t'+position+'\n')
#     elif chromos == '3R':
#         rate= R_3_c[posi_infor]
#         f3.write(chromos+'\t'+gene_id+'\t'+str(rate)+'\t'+position+'\n')
#     elif chromos == '4':
#         rate='0'
#         f3.write(chromos+'\t'+gene_id+'\t'+str(rate)+'\t'+position+'\n')
#     elif chromos == 'X':
#         rate = X_c[posi_infor]
#         f3.write(chromos+'\t'+gene_id+'\t'+str(rate)+'\t'+position+'\n')
#     else:
#         continue
# f2.close()
# f3.close()


import glob,re

path1=glob.glob("*.vcf.vcf")

for files in path1:
    i=float(0)
    j=0
    df1=open(files, "r")
    data=df1.readlines()[10:]
    newfile=files+".map"
    f1=open(newfile, "w")
    for polydf in data:
        chrom=polydf.split()[0]
        physiloc=polydf.split()[1]
        posid=polydf.split()[2]
        if j==10000:
            i+=1
            j=0
        else:
            j+=1
        f1.write(chrom+"\t"+ posid+"\t"+ str(i)+"\t"+ physiloc+"\n")
        