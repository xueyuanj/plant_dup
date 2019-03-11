#!/usr/bin/python

import subprocess
import glob

path='./*.fasta'
files=glob.glob(path)
for f in files:
	subprocess.check_call(["java", "-jar", "macse_v1.01b.jar", "-prog", "alignSequences", "-seq", f])
