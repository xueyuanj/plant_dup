#!/usr/bin/python

#Search and replace a line in the file. Here we're modifying the
#first line in control file.
from tempfile import mkstemp
from shutil import move
from os import remove, close
from subprocess import *
import glob
import re

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

#Change the range according to the number of files present in the folder.
"""phylip_names=[]
paml_names=[]
for haha in range(1,7996):
    phylip_name=str(haha)+'.phylip'
    paml_name=str(haha)+'.paml'
    phylip_names.append(phylip_name)
    paml_names.append(paml_name)


process=Popen(['codeml'], stdin=PIPE).communicate(input='\n')


for i in range(1,7995):
    old_p=phylip_names[i-1]
    new_p=phylip_names[i]
    old_pa=paml_names[i-1]
    new_pa=paml_names[i]
    replace("codeml.ctl", old_p, new_p)
    replace("codeml.ctl",old_pa, new_pa)
    process=Popen(['codeml'], stdin=PIPE).communicate(input='\n')"""


testlist=[]
allphylip=glob.glob("*.phylip")
for softf in allphylip:
    testlist.append(softf)

#print testlist[0]

process=Popen(['codeml'], stdin=PIPE).communicate(input='\n')

for i in range(1,len(testlist)):
    oldsoft=testlist[i-1]
    newsoft=testlist[i]
    softp=re.search("\S+.\d+", oldsoft).group(0)
    oldp=softp+".paml"
    hardp=re.search("\S+.\d+", newsoft).group(0)
    newp=hardp+".paml"
    replace("codeml.ctl", oldsoft, newsoft)
    replace("codeml.ctl",oldp, newp)
    process=Popen(['codeml'], stdin=PIPE).communicate(input='\n')

