#!/usr/bin/python

import subprocess
import glob
import re

path='*NT.fasta'
files=glob.glob(path)
for f in files:
	fname=re.search('\S+.\d+',f).group(0)
	pname=fname+'.phylip'
	print pname
	#subprocess.call(["python", "format_convert.py", f, pname])
