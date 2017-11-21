library(stringr)

current=setwd("/data/2017_plant_dup/specificities")

dupfiles=list.files("/data/2017_plant_dup/specificities", pattern = ".result1.txt.tao")



# Plot the combination of x, logx, y, logy
testprep=function(dist, tao){
  list_dist=list(dist, log(dist)); list_tao=list(tao, log(tao))
  testcomb=expand.grid(list_dist, list_tao)
  mapply(corretst, testcomb[,1], testcomb[,2] )
}

# Test wrapper, gives correlation coefficient and p-value
corretst=function(x, y){
  testpearson=cor.test(x,y, method="pearson")
  pearson_coef=testpearson$estimate
  pearson_p=testpearson$p.value
  testspearman=cor.test(x,y, method="spearman")
  spearman_coef=testspearman$estimate
  spearman_p=testspearman$p.value
  plotwithstat=plot(x, y, pch=19,cex.main=1,cex.lab=0.8,xlab="", ylab="t", main=paste("r =", round(pearson_coef, digits=4), "P =", round(pearson_p, digits=4), "\nrho =",round(spearman_coef, digits=4), "P =", round(spearman_p, digits=4) ))
  return (plotwithstat)
}



# Generate a matrix to store the correlation coefficients and p-values
par(mfrow=c(4,4), mar=c(2.5,2.5,2.5,1.5), mgp=c(2,1,0))
# Overall test 

for (i in 1:length(dupfiles)){
  print(dupfiles[i])
  dupdata=read.table(dupfiles[i])
  #namelist=unlist(strsplit(dupfiles[i], "[.]")) 
  colnames(dupdata)=c("p", "c", "a", "pdist", "cdist", "comdist", "mech", "taop", "taoc", "taoa")
  tao_p=dupdata$taop;tao_c=dupdata$taoc;tao_a=dupdata$taoa;e_pa=dupdata$pdist;e_ca=dupdata$cdist;
  testprep(e_pa ,tao_p);testprep(e_pa ,tao_a); testprep(e_ca ,tao_c);testprep(e_ca ,tao_a);
}




# Test for each mechanisms
mechs=c("Conservation", "Neofunctionalization(Child)","Neofunctionalization(Parent)", "Specialization")
for (j in 1:length(mechs)){
print(mechs[j] )
for (i in 1:length(dupfiles)){
  print(dupfiles[i])
  dupdata=read.table(dupfiles[i])
  colnames(dupdata)=c("p", "c", "a", "pdist", "cdist", "comdist", "mech", "taop", "taoc", "taoa")
  dupdata=dupdata[which(dupdata$mech==mechs[j]),]
  if (nrow(dupdata)>1){
  tao_p=dupdata$taop;tao_c=dupdata$taoc;tao_a=dupdata$taoa;e_pa=dupdata$pdist;e_ca=dupdata$cdist;
  testprep(e_pa ,tao_p);testprep(e_pa ,tao_a); testprep(e_ca ,tao_c);testprep(e_ca ,tao_a); 
  }
  else{
    print("Not enough data in this category.")
  } 
 }
}


# Test for single-copy genes
singlef=list.files("/data/2017_plant_dup/specificities", pattern = "singles.noclade.5species.euc.tao")

for (i in 1:length(singlef)){
  singlename=singlef[i]
  singledata=read.table(singlename)
  colnames(singledata)=c("spe2", "spe1", "eucdist", "tao2", "tao1")
  distance=singledata$eucdist; tao1=singledata$tao1; tao2=singledata$tao2;
  testprep(distance, tao1); testprep(distance, tao2);
}


