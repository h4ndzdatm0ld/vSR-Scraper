# vSR-Scraper
Tool to scrape configuration file before uploading to vSR SIM Lab.

This tool follows the vSIM Lab Info Document " To Load MLS and/or HUB Config from MTSO:" and completely automates the process.

There are a few variables which will need to be adjusted by locally editing the vSR_Scraper.py file:

FTPuser

FTPpasswd

JumpServer

vsr

# Requirements
This program requires the user to be running a WSL(Windows Subsystem Linux) instance on the machine. This has only been tested on a Ubuntu Instance.

Install GIT, Python3, PIP and Netmiko.

Once these requirements are met, clone the project to your C:/ drive. When the program is run for the first time, it will auto-generate a directory structure that will be utilized throught the life of the tool. 

Things to note: 

This tool will auto-backup the original file placed into the directory before it's processed. It will also backup a copy of the     finished product and organize it by system host name. 

# Instructions on how to get started.

Log into the MLS or HUB Router and capture the output of 'admin display-config' and save it as a .log file.

Drag the .log session into the working directory folder (vsr_scraper) under the C:/ drive.  Note: only qty. (1) .log file can be present in the working directory or the script will fail. 
