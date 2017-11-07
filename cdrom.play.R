library(CDROM)

current=setwd("/data/2017_plant_dup/CDROM_input")

dupfiles=list.files("/data/2017_plant_dup/CDROM_input/", pattern = ".orthomcl")


for (i in 1:length(dupfiles)){
  namelist=unlist(strsplit(dupfiles[i], "[.]")) 
  decide=namelist[3]
  ancname=gsub("Ancestral$", "", decide)
  duname=namelist[1]
  sorted=sort(c(ancname, duname))
  singlename=paste(sorted[1],"_", sorted[2], ".singles", sep = "")
  exprname1=paste(duname, "expr", sep=".")
  exprname2=paste(ancname, "expr", sep=".")
  out_name=paste(dupfiles[i], "result", sep = ".")
  print(out_name)
  CDROM(dupfiles[i], singlename, exprname1, exprname2, out = out_name, PC=FALSE,  head1 = FALSE, head2 = FALSE, legend = "topright")
}
