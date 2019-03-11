# plant_dup
2017-2018 graduate project

# download the monocot phylogeny from PLAZA 3.0
--> noclade_select.ids.txt

# identify 1:1 and 1:1:1 single-copy orthologs
# identify duplicates:
# use maximum-likelihood method COUNT (Csuos 2010) to estimate rates of duplications and losses along the tree
  $java -Xmx2048M -cp Count.jar ca.umontreal.iro.evolution.genecontent.ML noclade_select.ids.txt full.tree.spare.txt>          fulltree.ml
  
# assign the ancestral copy, get the table of triplets.
# used majority-voting scheme.

# obtain and clean the expression file.


# run CDROM to classify the duplicates into different retention mechanisms.
$ cdrom.play.R
--> Brachypodium.dups.Oryza.table.p1c2a3.count_gain06.siqr.result1.txt.merge
--> Oryza.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge
--> Sorghum.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge

# align the sequences using MACSE
# calculate Ka, Ks, Ka/Ks using PAML

# correlation between expression divergence and sequence divergence

# determine DNA- and RNA-mediated duplication

# 
