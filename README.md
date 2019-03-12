# plant_dup
2017-2018 graduate project

##Download the monocot phylogeny from PLAZA 3.0
--> noclade_select.ids.txt
##
##
##Identify lineag-specific single-copy genes and 1:1 single-copy orthologs

$ python 1to1to1.py

--> singlecopy.plaza.bdi_osa.ids.txt
--> singlecopy.plaza.bdi_sbi.ids.txt
--> singlecopy.plaza.osa_sbi.ids.txt

##Identification of duplicates
##Use maximum-likelihood method COUNT (Csuos 2010) to estimate rates of duplications and losses along the tree

$java -Xmx2048M -cp Count.jar ca.umontreal.iro.evolution.genecontent.ML 

$java -Xmx2048M -cp Count.jar ca.umontreal.iro.evolution.genecontent.AsymmetricWagner
##
##
##Assign the ancestral copy, get the table of triplets.Used majority-voting scheme.

$ python direct.ances.py

$ python conut.consistent.py

$ python assign.py

--> table.p1c2a3.count_gain06.txt
##
##
##Obtain and clean the expression file.

$ python filter.exp.plus.idc.py

$ python remove.dup.py

--> Brachypodium.TPM.log2trans.highexp.txt,clean

--> Oryza.TPM.log2trans.highexp.txt,clean

--> Sorghum.TPM.log2trans.highexp.txt,clean
##
##
##Run CDROM to classify the duplicates into different retention mechanisms.

$ cdrom.play.R

--> Brachypodium.dups.Oryza.table.p1c2a3.count_gain06.siqr.result1.txt.merge

--> Oryza.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge

--> Sorghum.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge
##
##
##Align the sequences using MACSE

$ python automator.py
##
##
##Calculate Ka, Ks, Ka/Ks using PAML
##
(1) remove ! in alignment file

$ python remove_ex.py
##
(2) convert to phylip format

$ python phylip_generator.py
##
(3) run PAML

$ python autopaml.py
##
(4) parse the PAML output

$ python getdnds.py
##
##
##Correlation between expression divergence and sequence divergence

$ R plot.kaks.R
##
##
##Determine DNA- and RNA-mediated duplication

$ get.dna.rna.py

--> Brachypodium.dups.Sorghum.table.p1c2a3.count_gain06.siqr.result1.txt.merge.dna_rna

--> Oryza.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge.dna_rna

--> Sorghum.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge.dna_rna
##
##
##Calculate tissue specificity, and get the tissue in which the gene that has the highest expression 

$ tao.R

--> Brachypodium.dups.Oryza.table.p1c2a3.count_gain06.siqr.result1.txt.merge.tao_largest

--> Oryza.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge.tao_largest

--> Sorghum.dups.Brachypodium.table.p1c2a3.count_gain06.siqr.result1.txt.merge.tao_largest
##
##
##Statistical test of tissue over-representation

$ triplebar.merge.Rmd
##
##The age information was obtained along with the duplicates identification
--> duplicates.ids.ageinfor.count.gain_06.all
##
##Test for overrepresentation of particular mechanism in different age groups
$ Age.chisq.Rmd







