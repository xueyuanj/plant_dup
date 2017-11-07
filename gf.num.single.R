library(dplyr)

current=setwd("/data/2017_plant_dup")

familydata=read.table("noclade_select.ids.txt", header=TRUE)

# Subset the data, choose single-copy gene # = 1
filter_row=function(familydf,single){
  for(i in 1:length(single)){
    colnm=single[i]
    temp=familydf[which(familydf[[colnm]]==1),]
    familydf=temp
  }
  
  return(familydf)
}

allspecies=c( "sbi", "osa", "bdi", "mac", "ath")

singlegenes=filter_row(familydata, allspecies)
dim(singlegenes)

write.table(singlegenes, file = "singles.family.bdi_osa_sbi_mac_ath.txt", quote = FALSE, sep = "\t", row.names = FALSE)

bdi_osa_sbi=read.table("singles.family.bdi_osa_sbi_mac_ath.txt", sep = "\t",  header=TRUE, colClasses = "character")

newnames=c("single1", "single2", "single3", "single4", "single5")

bdi_osa_sbi[newnames]=NA

allfamily=read.table("genefamily_data.hom.csv", sep = ";", header = TRUE, colClasses = "character")

for(i in 1:nrow(bdi_osa_sbi)){
  gfid=bdi_osa_sbi[i,"gf_id"]
  #spe=unlist(strsplit( bdi_osa_sbi[i,10],"_", head, 1))[1]
  #bdi_osa_sbi[i, "species"]=spe
  #spe=bdi_osa_sbi[i, "species"]
  #print(spe);print(gfid)
  #dupid=filter(allfamily, gf_id==gfid, species==spe )%>%select(gene_id)%>%unlist
  #print(length(dupid))
  for(j in (1:length(allspecies))){
    curanc=allspecies[j]
    print(curanc)
    colname=paste("single", j, sep = "")
    ancid=filter(allfamily, gf_id==gfid, species==curanc)%>%select(gene_id)%>%unlist
    bdi_osa_sbi[i, colname]=ancid[1]
  }
}

write.table(bdi_osa_sbi, file = "singles.geneids.bdi_osa_sbi_mac_ath.noclade.txt", quote = FALSE, sep = "\t", row.names = FALSE)
