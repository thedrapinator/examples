#!/usr/bin/python3

import subprocess

#target="google.com"
directory="/home/kali/whois/data"

#bashCommand = "whois "+domain
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd=directory)
#output, error = process.communicate()

def grabfile(domain):
     f = open(domain, "w") # this creates the file
     subprocess.run(['whois', domain], stdout=f) # this runs whois and writes to file f
     print('Grabbing whois record for '+domain+' and writing to file')

#For loop with files
#grabfile(target)

with open('/home/kali/whois/inscope.txt') as f:
    for line in f:
        #print(line.strip())
        grabfile(line.strip())












print('COMPLETED!')
