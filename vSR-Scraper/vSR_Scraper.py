#!/usr/bin/python3

#############################################################
# Author: Hugo Tinoco :: hugo.tinoco.ext@nokia.com          #
# Version 0.1 (Beta) - 2/12/2020                            #
#                                                           #
#############################################################
import time
import re

# Regex utilized to scrub the configuration files

ADMIN_PW = re.compile('^.*password.*$', flags=re.MULTILINE)
DISP_CONF = re.compile('^.*admin di.+$', flags=re.MULTILINE)
SOT_LINES = re.compile('^.*Generated\s\w+\s\w+\s+\d+\s\d+.\d+.\d+\s\d+\s\w+', re.DOTALL )
EOT_LINES = re.compile('Finished.*', re.MULTILINE | re.DOTALL)
MGMT_RTZ = re.compile('^.*static\D\w+\D\w+\s\d+.\d+.\d+.\d+\D\d+\s+next-hop\s\d+.\d+.\d+.\d+\s+exit\s+exit', re.MULTILINE)

# Replace the file name with the new configuration file being scrubbed.
file="SPFDILUP91A-P-AL-7750-01.txt"

# The first function runs the regex searches line by line, in order to
# eliminate syntax + empty lines within the configuration file that are
# left beind.

def ALL_Lines():
    with open (file, 'r+', encoding='utf-8') as f:
        scrape = []
        for line in f.readlines():
            if re.match(ADMIN_PW, line):
                print(line)
                continue
            if re.match(DISP_CONF, line):
                print(line)
                continue
            scrape.append(line)
        scrubbed = ("".join(scrape))
        x = open('scrubbed-pre.txt', 'w')
        x.write(scrubbed)
        x.close()
        time.sleep(5) # Some config files are quite large, assert enough time.

# The second function opens the scrubbed file and elimnates the unennsacrry syntax
# at the begining and end of the configuration syntax. This ensures the syntax
# doesn't fail when importing to the vSR.

def SO_Text():
    file = "scrubbed-pre.txt"
    with open (file, 'r+', encoding='utf-8') as f:
        contents = f.read()
        FirstLines = SOT_LINES.finditer(contents)
        for match in FirstLines:
            print(match)
        yz = re.sub(SOT_LINES, '', contents)
        x = open('scrubbed-pre.txt', 'w')
        x.write(yz)
        x.close()
        time.sleep(2) # Some config files are quite large, assert enough time.

def EO_Text():
    file = "scrubbed-pre.txt"
    with open (file, 'r+', encoding='utf-8') as f:
        contents = f.read()
        LastLines = EOT_LINES.finditer(contents)
        for match in LastLines:
            print(match)
        yx = re.sub(EOT_LINES, '', contents)
        x = open('scrubbed-pre.txt', 'w')
        x.write(yx)
        x.close()
        time.sleep(2) # Some config files are quite large, assert enough time.

def MGMT_Routes():
    file = "scrubbed-pre.txt"
    with open (file, 'r+', encoding='utf-8') as f:
        contents = f.read()
        Routes = MGMT_RTZ.finditer(contents)
        for match in Routes:
            print(match)
        yi = re.sub(MGMT_RTZ, '#', contents)
        x = open('scrubbed.txt', 'w')
        x.write(yi)
        x.close()
        time.sleep(1) # Some config files are quite large, assert enough time.

def main():
    ALL_Lines()
    SO_Text()
    EO_Text()
    MGMT_Routes()


if __name__ == "__main__": main()
