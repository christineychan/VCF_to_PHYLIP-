#!/usr/bin/python

in_file = "/Users/christinechan/Desktop/VCF_to_PHYLIP project/test/input.txt"

fh = open(in_file, "r")

samples = ''
ref = ''
alt = ''

for line in fh:
    if '##' in line:
        pass
    elif '#' in line:
        samples = line.strip().split()[9:]
    else:
        for line in fh:
            ref = line.strip().split()[3:]
            alt = line.st rip().split()[4:]

print ref
print alt
print samples
        
fh.close()