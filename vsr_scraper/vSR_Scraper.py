#!/usr/bin/python3

##################################################################
# Author: Hugo Tinoco :: hugo.tinoco.ext@nokia.com
# Version 0.1 (Beta) - 2/12/2020  - Created foundation.
# Version 0.2 (Beta) - 2/18/2020  - Re-strucuted. Auto find logs
#  - Error Handling. File/directory handling.
# Ver 0.3 (Beta) - 2/19/2020 - Ran pylint cleaned up code. ###
##################################################################

import time
import re
import os
import shutil
import glob
import sys
# Pending items:
#   - Remove the os module and only use shutil

# Regex patterns utilized to scrub the configuration files
ADMIN_PW = re.compile(r'^.*password.*$', re.MULTILINE)
DISP_CONF = re.compile(r'^.*admin di.+$', re.MULTILINE)
SOT_LINES = re.compile(r'^.*Generated\s\w+\s\w+\s+\d+\s\d+.\d+.\d+\s\d+\s\w+',\
    re.DOTALL)
EOT_LINES = re.compile(r'Finished.*', re.MULTILINE | re.DOTALL)
MGMT_RTZ = re.compile\
    (r'^.*static\D\w+\D\w+\s\d+.\d+.\d+.\d+\D\d+\s+next-hop\s\d+.\d+.\d+.\d+\s+exit\s+exit', \
    re.MULTILINE)
SFM = re.compile(r'^.*sfm\s\d\s+sfm.*\s+\w.*\s+.*', re.MULTILINE)
SYS_NAME = re.compile(r'((?<=system\s........name\s)(.*))')

# Capture the CWD as a variable.
CURRENT_PATH = os.getcwd()

# The log file must be pulled from the SecureCRT session using
# File > Log Session -- If the 'raw log' is used, the text spacing
# will be off and errors will occur.

# Display all .log files in the current working directory.
# If there are more than two .log files, the program will not run.
# Only one log file needs to be present to be scrubbed.
for y in glob.glob("*.log"):
    file = (y)
    print("Found a log file! Using:", file)
    if len(glob.glob("*.log")) > 1:
        sys.exit("Err.. found too many Log files in the CWD - \
Ensure only one is present & try again.")

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' +  directory)

def clean_slate():
# This additional function is used to wipe the latest scrubbed configuration at
# the time of running this program and allow this folder to only keep the active
# file stored within the Scrubbed Configs/Latest directory. Ansible will pull
# this log file and finish FTP it to the Jump Server.
    try:
        os.chdir('Scrubbed Configs')
        shutil.rmtree('Latest')
    except FileNotFoundError:
        print("Latest Folder not present. Is this first boot?")

# These folders will be auto-generated to allow the program to handle all the
# files that will be created, backed up, etc. These do not get overwritten
# after initial creation.
def dir_setup():
    os.chdir(CURRENT_PATH)
    create_folder('Scrubbed Configs')
    create_folder('Scrubbed Configs/Latest')
    create_folder('Temp')
    create_folder('Backup Configs')

    # Create a backup of the original file before doing anything.
    SRC_FILE = file
    DST_FLD = 'Backup Configs'
    shutil.copy2(SRC_FILE, DST_FLD)

# The first function runs the regex searches line by line, in order to
# eliminate syntax + empty lines within the configuration file that are
# left beind.
def line_text():
    with open(file, 'r+', encoding='utf-8') as f_rd:
        scrape = []
        for line in f_rd.readlines():
            if re.match(ADMIN_PW, line):
                continue
            if re.match(DISP_CONF, line):
                continue
            scrape.append(line)
        scrubbed = ("".join(scrape))

        os.chdir("Temp") # Place this file in the temp folder
        x_new = open('scrubbed.log', 'w')
        x_new.write(scrubbed)
        x_new.close()
        time.sleep(5) # Some config files are quite large, assert enough time.

# The second function searches all text, without being bound to reading line by
# line, as opposed to the first function.
def reg_text():
    file = "scrubbed.log"
    with open(file, 'r+', encoding='utf-8') as f_rd:
        contents = f_rd.read()

        # An example loop to print out the items found.

        # FirstLines = SOT_LINES.finditer(contents)
        # for match in FirstLines:
        #     print(match)

        # Extracting the system name out of the config file.
        name = re.finditer(SYS_NAME, contents)

        # Using replace method to pull quotes out of sys name(regex)
        rem_qtz = ['"']
        for match in name:
            try:
                system = (match.group(0))
                # print(system)
            except UnboundLocalError:
                print("Err.. regex failed to find system name")

        for i in rem_qtz:
            try:
                system = system.replace(i, '')
            except UnboundLocalError:
                print("Err.. regex failed to find system name")
                # At this point, the node system name is captured as a variable.
                # named 'system'

        # A dirty way to sub out regex patterns. Can't loop, as some are empty
        # Spaces and some are hashes that replace values.
        a = re.sub(SOT_LINES, '', contents)
        b = re.sub(EOT_LINES, '', a)
        c = re.sub(MGMT_RTZ, '#', b)
        d = re.sub(SFM, '#', c)

        # Remove the temp file
        os.remove("scrubbed.log")

        # Back to home dir + scrubbed config for final product
        os.chdir(CURRENT_PATH +'/Scrubbed Configs')

        # Utilize the createfolder function to create a folder by sys name.
        try:
            create_folder(system)
        except UnboundLocalError:
            print("Err.. regex failed to find system name - error occured earlier.")

        # Drop into the new folder
        try:
            os.chdir(system)
        except UnboundLocalError:
            print("Err.. regex failed to find system name - error occured earlier.")

        try:
            x = open(system +'-Scrubbed.log', 'w')
            x.write(d)
            x.close()
            for y in glob.glob("*.log"):
                file = (y)
                print("Copying the latest generated file to 'Scrubbed Configs/Latest'", file)
            SRC_FILE = file
            DST_FLD = CURRENT_PATH +'/Scrubbed Configs/Latest'
            shutil.copy2(SRC_FILE, DST_FLD)
        except UnboundLocalError:
            print("Err.. regex failed to find system name - error occured earlier.")

        # Captured at the beg of code:
        try:
            print("New Scrubbed Config Directory and File Generated: ", system+"-Scrubbed.log")
            print("The vSR-Scraper directory lives at %s" % CURRENT_PATH)
        except UnboundLocalError:
            print("Err.. regex failed to find system name - error occured earlier.")

def main():
    clean_slate()
    dir_setup()
    line_text()
    reg_text()

if __name__ == "__main__": main()
