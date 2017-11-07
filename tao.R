library(stringr)
library(dplyr)
library(ggplot2)
library(reshape2)

path= setwd("/data/2017_plant_dup/specificities")

exprfiles=list.files("/data/2017_plant_dup/specificities", pattern = "expr")

# Calculate tao based on the formula
# The input of this function is a vecor of expression data
tao=function(genet){
  ntissue=length(genet)
  emax=max(genet)
  sum=0
  for(i in 1:length(genet)){
    before=1-genet[i]/emax
    sum=sum+before
  }
  return(sum/(ntissue-1))
}


# Get the tao, as well as the largest expression value for all the files
for (j in 1:length(exprfiles)){
  temp=exprfiles[j]
  tempdf=read.table(temp, header = TRUE )
  largevec=colnames(tempdf[,-1])[apply(tempdf[,-1], 1, which.max)]
  tempdf["largest"]=largevec
  tempdf["tao"]=NA
  for (m in 1:nrow(tempdf)){
    thisrow=as.numeric(tempdf[m,2:(ncol(tempdf)-2)])
    thistao=tao(thisrow)
    tempdf[m, "tao"]=thistao
  }
  result=paste(temp,"tao",sep = ".")
  write.table(tempdf,file = result, quote = FALSE, sep = "\t", row.names = FALSE)
  
}



# Merge the classification, age, tao, and highest expression tissue information

# First lable the species and ancestral species
mechage=read.table("noclade.strict.age.class.siqr", header = TRUE)
mechage[,"species"]=substr(mechage$age, 0,3)
mechage[,"anspecies"]=substr(mechage$Ancestor, 0, 2)
mechage$anspecies = mechage$anspecies%>%{gsub("OS", "osa", .)}%>%{gsub("BD", "bdi", .)}%>%{gsub("SB", "sbi", .)}

# Remove the NAs
mechage=na.omit(mechage)

# Get all the tao data
taofile=list.files("/data/2017_plant_dup/specificities", pattern = "expr.tao")
taodf=data.frame()
for (l in 1:length(taofile)){
  taot=read.table(taofile[l], header = TRUE, sep = "\t")
  taodf=rbind(taodf, taot)
}




# Append the tao as well as largest expression value to child and parent in mech/age table
mechage[,c("plargest", "ptao", "clargest", "ctao" )]=NA

for (num in 1:nrow(mechage)){
  pid=mechage[num, "Parent"]
  cid=mechage[num, "Child"]
  #mechage[num, "plargest"]=taodf[which(taodf$gene==pid), "largest"]
  #mechage[num, "ptao"]=taodf[which(taodf$gene==pid), "tao"]
  #mechage[num, "clargest"]=taodf[which(taodf$gene==cid), "largest"]
  #mechage[num, "ctao"]=taodf[which(taodf$gene==cid), "tao"]
}


# Save a copy of the file
write.table(mechage,file = "noclade.strict.age.class.siqr.tao", quote = FALSE, sep = "\t", row.names = FALSE)

mechage=read.table("noclade.strict.age.class.siqr.tao",header = TRUE)
# Also get the tao for single copy genes
singletao=matrix(data = NA, nrow = 3, ncol = 2)

singleids=list.files("/data/2017_plant_dup/specificities", pattern = "singles")
for(mk in 1:length(singleids)){
  filename=singleids[mk]
  print(filename)
  singlelist=read.table(filename, header = FALSE, colClasses = "character")
  colnames(singlelist)=c("id1", "id2")
  singlelist[c("tao1", "tao2")]=NA
  for(up in 1:nrow(singlelist)){
    id1=singlelist[up, "id1"]
    id2=singlelist[up, "id2"]
    if(id1 %in% taodf$gene){
      singlelist[up, "tao1"]=taodf[which(taodf$gene==id1), "tao"]
    }
    else{next}
    if(id2 %in% taodf$gene){
      singlelist[up, "tao2"]=taodf[which(taodf$gene==id2), "tao"]
    }
    else{next}
    
  }
  alltao1=singlelist$tao1
  alltao2=singlelist$tao2
  alltao1[!is.finite(alltao1)]=NA
  alltao2[!is.finite(alltao2)]=NA
  print(length(na.omit(alltao1))); print(length(na.omit(alltao2)))
  print(median(na.omit(alltao1)));print(median(na.omit(alltao2)))
  singletao[mk, 1]=median(na.omit(alltao1))
  singletao[mk, 2]=median(na.omit(alltao2))
}

rownames(singletao)=c("Brachypodium.Oryza", "Brachypodium.Sorghum", "Oryza.Sorghum")
colnames(singletao)=c("f_c", "s_c") # first, secod

# Now plot the tao

# First subset the data based on species and ancestral species

threespe=c("bdi", "osa", "sbi")
spe=rep(threespe, 3)
anc=rep(threespe, each=3)

# Pass the ones where both species are the same

head(mechage)
mechage$Classification=as.factor(mechage$Classification)

sink("largest_expression_in_tissue.txt")

for (i in 1:length(spe)){
    thisspe=spe[i]
    anspe=anc[i]
    if (thisspe==anspe){
      next
    }
    else{
      namevec=sort(c(thisspe, anspe))
      print(thisspe);print(anspe)
      #whichrow=paste(namevec[1], namevec[2], sep = ".")
      dfsubset=mechage[which(mechage$species==thisspe&mechage$anspecies==anspe), ]
      print(dim(dfsubset))
      #neochildones=dfsubset[which(dfsubset$Classification=="Neofunctionalization(Child)"), ]
      #print(dfsubset[which.max(neochildones$E_C.A) ,c("Child", "Parent") ])
      #print(table(dfsubset[,c("Classification", "plargest")]))
      #print(table(dfsubset[,c("Classification", "clargest")]))
      # filename1 = paste(thisspe, anspe, "parent", "png", sep = ".")
      # filename2 = paste(thisspe, anspe, "child", "png", sep = ".")
      # pplot=ggplot(dfsubset, aes(x=Classification, y=ptao))+
      #   geom_boxplot(outlier.shape = NA, notch = TRUE)+
      #   ggtitle(paste(thisspe, anspe, "parent", sep = "."))
      #   
      # cplot=ggplot(dfsubset, aes(x=Classification, y=ctao))+
      #   geom_boxplot(outlier.shape = NA, notch = TRUE)+
      #   ggtitle(paste(thisspe, anspe, "child", sep = "."))
      #  
      # if(thisspe==namevec[1]){
      #   thisspe="f_c"
      #   anspe="s_c"
      # }
      # else{
      #   thisspe="s_c"
      #   anspe="f_c"
      # }
      # pplot=pplot+geom_hline(aes(yintercept=singletao[whichrow,thisspe]), linetype="dashed")
      # cplot=cplot+geom_hline(aes(yintercept=singletao[whichrow,thisspe]), linetype="dashed")
      # ggsave(pplot, filename=filename1)
      # ggsave(cplot, filename=filename2)
    }
   
}


sink()


cdromresult=list.files("/data/2017_plant_dup/specificities", pattern = "p1c2a3.result1.txt")

par(mfrow=c(2,3))
for (i in 1:length(cdromresult)){
  thisfile=cdromresult[i]
  thisdata=read.table(thisfile, header = TRUE )
  thisdata=na.omit(thisdata)
  thisdata[, c("ptao", "ctao")]=NA
  for(up in 1:nrow(thisdata)){
    id1=thisdata[up, "Parent"]
    id2=thisdata[up, "Child"]
    if(id1 %in% taodf$gene){
      thisdata[up, "ptao"]=taodf[which(taodf$gene==id1), "tao"]
    }
    else{next}
    if(id2 %in% taodf$gene){
      thisdata[up, "ctao"]=taodf[which(taodf$gene==id2), "tao"]
    }
    else{next}
  }
  namelist=unlist(strsplit(thisfile, "[.]"))
  thisspe=namelist[1]
  decide=namelist[3]
  anspe=gsub("Ancestral$", "", decide)
  filename1 = paste(thisspe, anspe, "parent", "png", sep = ".")
  filename2 = paste(thisspe, anspe, "child", "png", sep = ".")
  #print(thisspe); print(anspe)
  # pplot=ggplot(thisdata, aes(x=Classification, y=ptao))+
  #     geom_boxplot(outlier.shape = NA, notch = TRUE)+
  #     ggtitle(paste(thisspe, anspe, "parent", sep = "."))
  # 
  # cplot=ggplot(thisdata, aes(x=Classification, y=ctao))+
  #     geom_boxplot(outlier.shape = NA, notch = TRUE)+
  #     ggtitle(paste(thisspe, anspe, "child", sep = "."))
  # namevec=sort(c(thisspe, anspe))
  # whichrow=paste(namevec[1], namevec[2], sep = ".")
  # if(thisspe==namevec[1]){
  #   thisspe="f_c"
  #   anspe="s_c"
  # }
  # else{
  #   thisspe="s_c"
  #   anspe="f_c" }
  # pplot=pplot+geom_hline(aes(yintercept=singletao[whichrow,thisspe]), linetype="dashed")
  # cplot=cplot+geom_hline(aes(yintercept=singletao[whichrow,thisspe]), linetype="dashed")
  # 
  # ggsave(pplot, filename=filename1)
  # ggsave(cplot, filename=filename2)
}

 



######################################################################

# Now merge duplicates in the same species, take average of the tao in single-copy genes
cdromresult=list.files("/data/2017_plant_dup/specificities", pattern = "p1c2a3.result1.txt")
duptao=data.frame()

for (i in 1:length(cdromresult)){
  thisfile=cdromresult[i]
  print(thisfile)
  thisdata=read.table(thisfile, header = TRUE ,colClasses = "character" )
  thisdata=na.omit(thisdata)
  thisdata[, c("ptao", "ctao")]=NA
  for(up in 1:nrow(thisdata)){
    id1=thisdata[up, "Parent"]
    id2=thisdata[up, "Child"]
    if(id1 %in% taodf$gene){
      thisdata[up, "ptao"]=taodf[which(taodf$gene==id1), "tao"]
    }
    else{next}
    if(id2 %in% taodf$gene){
      thisdata[up, "ctao"]=taodf[which(taodf$gene==id2), "tao"]
    }
    else{next}
  }
  namelist=unlist(strsplit(thisfile, "[.]"))
  thisspe=namelist[1]
  #decide=namelist[3]
  #anspe=gsub("Ancestral$", "", decide)
  #filename1 = paste(thisspe, anspe, "parent", "png", sep = ".")
  #filename2 = paste(thisspe, anspe, "child", "png", sep = ".")
  thisdata["species"]=thisspe
  duptao=rbind(duptao, thisdata)
  #print(thisspe); print(anspe)
  # pplot=ggplot(thisdata, aes(x=Classification, y=ptao))+
  #     geom_boxplot(outlier.shape = NA, notch = TRUE)+
  #     ggtitle(paste(thisspe, anspe, "parent", sep = "."))
  # 
  # cplot=ggplot(thisdata, aes(x=Classification, y=ctao))+
  #     geom_boxplot(outlier.shape = NA, notch = TRUE)+
  #     ggtitle(paste(thisspe, anspe, "child", sep = "."))
  # namevec=sort(c(thisspe, anspe))
  # whichrow=paste(namevec[1], namevec[2], sep = ".")
  # if(thisspe==namevec[1]){
  #   thisspe="f_c"
  #   anspe="s_c"
  # }
  # else{
  #   thisspe="s_c"
  #   anspe="f_c" }
  # pplot=pplot+geom_hline(aes(yintercept=singletao[whichrow,thisspe]), linetype="dashed")
  # cplot=cplot+geom_hline(aes(yintercept=singletao[whichrow,thisspe]), linetype="dashed")
  # 
  # ggsave(pplot, filename=filename1)
  # ggsave(cplot, filename=filename2)
}


######### original data  ###########
duptao=duptao[-which(duptao$Classification=="Subfunctionalization"), ]

duptao$Classification = gsub("Neofunctionalization(Child)", "Neochild", duptao$Classification)

brachydup=duptao[which(duptao$species=="Brachypodium"), ]

bra.pplot=ggplot(brachydup, aes(x=Classification, y=ptao))+
  scale_x_discrete(labels=c("Conservation", "Neochild",  "Neoparent", "Specialization") )+
  geom_boxplot(outlier.shape = NA,lwd=3,width=0.5, notch = TRUE, color=c("slategray1", "palevioletred","thistle", "darkseagreen"))+
  theme_classic()+
  theme(axis.text.x = element_blank(), axis.text.y = element_text(size=18))+
  labs(x="", y=expression(tau))+
  ylim(0.2, 1.2)+
  geom_hline(aes(yintercept=0.67), linetype="dashed", size=1)+
  theme(text = element_text(size = 20),panel.border = element_rect(colour = "black", fill=NA, size=0.5))

bra.pplot

bra.pplot=ggplot(brachydup, aes(x=Classification, y=ptao))+
  geom_boxplot(outlier.shape = NA, notch = TRUE)

bra.cplot=ggplot(brachydup, aes(x=Classification, y=ctao))+
  scale_x_discrete(labels=c("Conservation", "Neochild",  "Neoparent", "Specialization") )+
  geom_boxplot(outlier.shape = NA,lwd=3,width=0.5, notch = TRUE, color=c("slategray1", "palevioletred","thistle", "darkseagreen"))+
  theme_classic()+
  theme(axis.text.x = element_blank(), axis.text.y = element_text(size=18))+
  labs(x="", y=expression(tau))+
  ylim(0.2, 1.2)+
  geom_hline(aes(yintercept=0.67), linetype="dashed", size=1)+
  theme(text = element_text(size = 20),panel.border = element_rect(colour = "black", fill=NA, size=0.5))


bra.cplot
multiplot(bra.pplot, bra.cplot, cols = 2)

orydup=duptao[which(duptao$species=="Oryza"), ]

ory.pplot=ggplot(orydup, aes(x=Classification, y=ptao))+
  scale_x_discrete(labels=c("Conservation", "Neochild",  "Neoparent", "Specialization") )+
  geom_boxplot(outlier.shape = NA,lwd=3,width=0.5, notch = TRUE, color=c("slategray1", "palevioletred","thistle", "darkseagreen"))+
  theme_classic()+
  theme(axis.text.x = element_blank(), axis.text.y = element_text(size=18))+
  labs(x="", y=expression(tau))+
  ylim(0.2, 1.2)+
  geom_hline(aes(yintercept=0.67), linetype="dashed", size=1)+
  theme(text = element_text(size = 20),panel.border = element_rect(colour = "black", fill=NA, size=0.5))
ory.pplot

ory.cplot=ggplot(orydup, aes(x=Classification, y=ctao))+
  scale_x_discrete(labels=c("Conservation", "Neochild",  "Neoparent", "Specialization") )+
  geom_boxplot(outlier.shape = NA,lwd=3,width=0.5, notch = TRUE, color=c("slategray1", "palevioletred","thistle", "darkseagreen"))+
  theme_classic()+
  theme(axis.text.x = element_blank(), axis.text.y = element_text(size=18))+
  labs(x="", y=expression(tau))+
  ylim(0.2, 1.2)+
  geom_hline(aes(yintercept=0.67), linetype="dashed", size=1)+
  theme(text = element_text(size = 20),panel.border = element_rect(colour = "black", fill=NA, size=0.5))

ory.cplot


sordup=duptao[which(duptao$species=="Sorghum"), ]

sor.pplot=ggplot(sordup, aes(x=Classification, y=ptao))+
  scale_x_discrete(labels=c("Conservation", "Neochild",  "Neoparent", "Specialization") )+
  geom_boxplot(outlier.shape = NA,lwd=3,width=0.5, notch = TRUE, color=c("slategray1", "palevioletred","thistle", "darkseagreen"))+
  theme_classic()+
  theme(axis.text.x = element_blank(), axis.text.y = element_text(size=18))+
  labs(x="", y=expression(tau))+
  ylim(0.2, 1.2)+
  geom_hline(aes(yintercept=0.67), linetype="dashed", size=1)+
  theme(text = element_text(size = 20),panel.border = element_rect(colour = "black", fill=NA, size=0.5))

sor.pplot

sor.cplot=ggplot(sordup, aes(x=Classification, y=ctao))+
  scale_x_discrete(labels=c("Conservation", "Neochild",  "Neoparent", "Specialization") )+
  geom_boxplot(outlier.shape = NA,lwd=3,width=0.5, notch = TRUE, color=c("slategray1", "palevioletred","thistle", "darkseagreen"))+
  theme_classic()+
  theme(axis.text.x = element_blank(), axis.text.y = element_text(size=18))+
  labs(x="", y=expression(tau))+
  ylim(0.2, 1.2)+
  geom_hline(aes(yintercept=0.67), linetype="dashed", size=1)+
  theme(text = element_text(size = 20),panel.border = element_rect(colour = "black", fill=NA, size=0.5))

sor.cplot
multiplot <- function(..., plotlist = NULL, file, cols = 1, layout = NULL) {
  require(grid)
  
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  if (is.null(layout)) {
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots == 1) {
    print(plots[[1]])
    
  } else {
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    for (i in 1:numPlots) {
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}
multiplot(bra.pplot, bra.cplot, ory.pplot, ory.cplot, sor.pplot, sor.cplot, cols=2)

wilcoxwrapper=function(dfsub){
  mechs=t(combn(unique(dfsub$Classification), 2))
  result=matrix(nrow = nrow(mechs), ncol = 4, data = NA)
  result[,c(1,2)]=mechs
  for(i in 1:nrow(mechs)){
    ptest=wilcox.test(dfsub[which(dfsub$Classification==mechs[i,1]),"ptao"],dfsub[which(dfsub$Classification==mechs[i,2]), "ptao"] )
    result[i, 3]=ptest$p.value
    ctest=wilcox.test(dfsub[which(dfsub$Classification==mechs[i,1]),"ctao"],dfsub[which(dfsub$Classification==mechs[i,2]), "ctao"] )
    result[i, 4]=ctest$p.value
    }
  return(result)
}

wilcoxwrapper(brachydup);wilcoxwrapper(orydup); wilcoxwrapper(sordup)
