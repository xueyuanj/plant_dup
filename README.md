# plant_dup
2017-2018 graduate project

##Download the monocot phylogeny from PLAZA 3.0
--> noclade_select.ids.txt

##Identify 1:1 and 1:1:1 single-copy orthologs

##Identify duplicates:
##use maximum-likelihood method COUNT (Csuos 2010) to estimate rates of duplications and losses along the tree

$java -Xmx2048M -cp Count.jar ca.umontreal.iro.evolution.genecontent.ML noclade_select.ids.txt full.tree.spare.txt>          fulltree.ml
  
##Assign the ancestral copy, get the table of triplets.

used majority-voting scheme.

##Obtain and clean the expression file.


##Run CDROM to classify the duplicates into different retention mechanisms.

$ cdrom.play.R

--> Brachypodium.dups.Oryza.table.p1c2a3.count_gain06.siqr.result1.txt.merge

--> Oryza.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge

--> Sorghum.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge

##Align the sequences using MACSE

$ python automator.py

##Calculate Ka, Ks, Ka/Ks using PAML

(1) remove ! in alignment file

$ python remove_ex.py

(2) convert to phylip format

$ python phylip_generator.py

(3) run PAML

$ python autopaml.py

(4) parse the PAML output

$ python getdnds.py


##Correlation between expression divergence and sequence divergence

$ R plot.kaks.R

##Determine DNA- and RNA-mediated duplication

$ get.dna.rna.py

--> Brachypodium.dups.Sorghum.table.p1c2a3.count_gain06.siqr.result1.txt.merge.dna_rna

--> Oryza.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge.dna_rna

--> Sorghum.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge.dna_rna

##Calculate tissue specificity, and get the tissue in which the gene has the highest expression 
