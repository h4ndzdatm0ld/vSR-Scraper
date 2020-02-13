-----------------------------------------------------------
# Created by Hugo Tinoco :: hugo.tinoco.ext@nokia.com
# Version 0.1 (Beta) - 2/12/2020
#!/usr/bin/python3
-----------------------------------------------------------

import re

# Regex utilized to scrub the configuration files

admin_pw = re.compile('^.*password.*$', re.MULTILINE)
netc = re.compile('^.*netconf.+$', re.MULTILINE)

def main():

 with open ('config.txt', 'r+', encoding='utf-8') as f:
    scrape = []
    for line in f.readlines():
     if re.match(admin_pw, line):
         continue
     if re.match(netc, line):
         continue
     scrape.append(line)

    scrubbed = ("".join(scrape))
    print(scrubbed)

if __name__ == "__main__": main()
