"""Utility script to standardize CSV files.

This reads in each CSV file on the command-line and writes it out again using
pandas.  This ensures standard formatting conventions across all files,
including escaping quotes and dealing with line terminators uniformly.
"""

import os
import shutil
import sys

import pandas

if __name__ == '__main__':
    for fn in sys.argv[1:]:
        print "Processing %s" % fn

        shutil.copy2(fn, fn+".bak")
        df = pandas.read_csv(fn, encoding='utf-8')
        df.to_csv(fn, index=False, encoding='utf-8')
        os.remove(fn+".bak")
        
    print "All done"
        
