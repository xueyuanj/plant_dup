library(stringr)
library(ggplot2)
current=setwd("/data/Progress_Report/2018-7-20")

dupfiles=list.files("/data/Progress_Report/2018-7-20", pattern = "dn.ds.dnds.txt")

options(warn=-1)



# Test wrapper, gives correlation coefficient and p-value
corretst=function(x,y){
  #print(dim(dupdatas))
  colnames(x)=c("cdist", "kac")
  
  testspearman_c=cor.test(x[,"cdist"], x[,"kac"], method="pearson")
  spearman_coef_c=round(testspearman_c$estimate, digits = 4)
  print(spearman_coef_c);print(testspearman_c$p.value)
  pplot=ggplot(x, aes(x=cdist, y=kac))+
    geom_point(size=0.8)+
    theme_classic()+
    theme(plot.title = element_text(size = 25, hjust = 0.5),text = element_text(size = 25,  colour = "black"),panel.border = element_rect(colour = "black", fill=NA, size=0.5),
          axis.text.y = element_text(angle=90, hjust = 0.3),axis.ticks = element_blank())+
    scale_y_continuous(limits = c(-6,0) ,breaks = c( -6, -4, -2, 0),labels = NULL )+
    scale_x_continuous(limits = c(-6,0) ,breaks = c(-4, -3, -2, -1, 0),labels = NULL )+
    ylab("")+xlab("")  +
    geom_smooth(method = "lm", color="red", size=1, se=FALSE)

  pname=paste(y, "duplicates","ka","png", sep = ".")
  ggsave(filename =pname , plot=pplot, path = "/data/Progress_Report/2018-7-20",
         width = 10, height = 10, units = "cm", dpi = 1000, device = "png")  
  
 
}




for (i in 1:length(dupfiles)){
  print(dupfiles[i])
  speciesnow=unlist(strsplit(dupfiles[i], "[.]"))[1]
  dupdata=read.table(dupfiles[i],header = FALSE)
  
  colnames(dupdata)=c("p", "c", "Ediv",  "ka", "ks", "kaks")
  
  dupdata=dupdata[which(dupdata$ks<3),]
 
  E_div=log2(dupdata$Ediv); KaKs=log2(dupdata$ks) # change the statistic here
  # Pearson correlation
  print(cor.test(E_div, KaKs, method="pearson"))
  newdf= cbind(E_div, KaKs)
  newdf = as.data.frame(newdf)
  #print(head(newdf))
  pplot=ggplot(newdf, aes(x=E_div, y=KaKs))+
    geom_point(size=0.8)+
    theme_classic()+
    theme(plot.title = element_text(size = 25, hjust = 0.5),text = element_text(size = 25,  colour = "black"),panel.border = element_rect(colour = "black", fill=NA, size=0.5),
          axis.text.y = element_text(angle=90, hjust = 0.3),axis.ticks = element_blank())+
    scale_y_continuous(limits = c(-2,2) ,breaks = c( -2, -1, 0,1, 2),labels = NULL )+
    scale_x_continuous(limits = c(-6,0) ,breaks = c(-4, -3, -2, -1, 0),labels = NULL )+
    ylab("")+xlab("")  +
    geom_smooth(method = "lm", color="red", size=1, se=FALSE)
  
  pname=paste(speciesnow, "duplicates","ks","png", sep = ".")
  ggsave(filename =pname , plot=pplot, path = "/data/Progress_Report/2018-7-20",
         width = 10, height = 10, units = "cm", dpi = 1000, device = "png")  
}
