library(dplyr)

current=setwd("/data/2017_plant_dup")

familydata=read.table("noclade_select.ids.txt", header=TRUE)
#familycounts=familydata[,c(1,4:11)]
#familycounts=familydata[, c("gf_id", "sbi", "osa", "bdi", "mac", "ath")]
familycounts=familydata[, c(1,4:ncol(familydata))]

# Subset the data, choose single-copy gene # = 1, and duplicate gene # = 2
filter_row=function(df,single, dup){
  for(i in 1:length(single)){
    colnm=single[i]
    temp=df[which(df[[colnm]]==1),]
    df=temp
  }
  for(i in 1:length(dup)){
    colnm=dup[i]
    temp=df[which(df[[colnm]]==2),]
    df=temp
  }
  return(df)
}


#allspecies=c("zma", "sbi", "sit", "osa", "osaindica", "bdi", "hvu", "mac")
allspecies=c( "sbi", "osa", "bdi", "mac", "ath")

# For Brachypodium

bin_1=c("bdi")
#bin_2=c("bdi", "hvu")
#bin_3=c("bdi", "hvu", "osa", "osaindica")


applyf=function(dupclade){
  sclade=setdiff(allspecies, dupclade)
  result=filter_row(familycounts, sclade, dupclade)
  if (nrow(result)!=0){
    ageinfor=paste(dupclade, collapse = "_")
    result[,"species"]=ageinfor
  ### change here to decide whether you want to check the data size or
  ### get the table written somewhere
    return(result)
  }
  #return(result)
}

bra_dup=applyf(bin_1)

#bdi3brach=rbind(applyf(bin_1),applyf(bin_2),applyf(bin_3) )
#applyf(bin_1);applyf(bin_2);applyf(bin_3)

# For Oryza

ory_1=c("osa")
#ory_2=c("osa", "osaindica")
#ory_3=c("osa", "osaindica","bdi", "hvu")


#applyf(ory_1);applyf(ory_2);applyf(ory_3)
#ory3brach=rbind(applyf(ory_1),applyf(ory_2),applyf(ory_3) )

ory_dup=applyf(ory_1)

# For Sorghum

sor_1=c("sbi")
# sor_2=c("sbi", "zma")
# sor_3=c("sbi", "zma", "sit")


#applyf(sor_1);applyf(sor_2);applyf(sor_3)
#sor3brach=rbind(applyf(sor_1),applyf(sor_2),applyf(sor_3)  )
sor_dup=applyf(sor_1)

bdi_osa_sbi=rbind(bra_dup, ory_dup, sor_dup)

# Write the table into a file
write.table(bdi_osa_sbi, file = "duplicate.family.mac_ath_outg.bdi_osa_sbi.txt", quote = FALSE, sep = "\t", row.names = FALSE)

#newnames=c("dup1", "dup2", "anc1", "anc2", "species")

bdi_osa_sbi=read.table("duplicate.family.mac_ath_outg.bdi_osa_sbi.txt", sep = "\t",  header=TRUE)

newnames=c("dup1", "dup2", "anc1", "anc2", "anc3", "anc4")

bdi_osa_sbi[newnames]=NA

allfamily=read.table("genefamily_data.hom.csv", sep = ";", header = TRUE)
i=sapply(allfamily, is.factor)
allfamily[i]=lapply(allfamily[i], as.character)
threespecies=c("bdi","osa", "sbi", "ath", "mac")


# Find the duplicates and ancestral single-copy gene IDs of each gene family.
# Write everything in a table.
for(i in 1:nrow(bdi_osa_sbi)){
  gfid=bdi_osa_sbi[i,"gf_id"]
  #spe=unlist(strsplit( bdi_osa_sbi[i,10],"_", head, 1))[1]
  #bdi_osa_sbi[i, "species"]=spe
  spe=bdi_osa_sbi[i, "species"]
  #print(spe);print(gfid)
  dupid=filter(allfamily, gf_id==gfid, species==spe )%>%select(gene_id)%>%unlist
  print(length(dupid))
  bdi_osa_sbi[i, "dup1"]=dupid[1]
  bdi_osa_sbi[i, "dup2"]=dupid[2]
  ancspe=setdiff(threespecies, spe)
  print(spe)
  for(j in (1:length(ancspe))){
    curanc=ancspe[j]
    colname=paste("anc", j, sep = "")
    ancid=filter(allfamily, gf_id==gfid, species==curanc)%>%select(gene_id)%>%unlist
    bdi_osa_sbi[i, colname]=ancid[1]
  }
}

# Save the current file with duplicate/single-copy IDs available
write.table(bdi_osa_sbi, file = "duplicate.family.mac_ath_outg.bdi_osa_sbi.dup_assigned.txt", quote = FALSE, sep = "\t", row.names = FALSE)





