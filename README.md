# vSR-Scraper
Tool to scrape configuration file before uploading to vSR SIM Lab.

This tool follows the vSIM Lab Info Document " To Load MLS and/or HUB Config from MTSO:" and completely automates the process.

There are a few variables which will need to be adjusted by locally editing the vSR_Scraper.py file:

* JumpServer
* JS_User
* JS_Pass
* vsr

# Requirements
This program requires the user to be running a WSL(Windows Subsystem Linux) instance on the machine. This has only been tested on a Ubuntu Instance.

A custom ssh config file will need to be manually created. A template for this will is found under the wiki page, along with detailed instructions on how to install the following:

GIT, Python3, PIP and Netmiko.

Once these requirements are met, clone the project to your C:/ drive. When the program is run for the first time, it will auto-generate a directory structure that will be utilized throught the life of the tool. 

Things to note: 

This tool will auto-backup the original file placed into the directory before it's processed. It will also backup a copy of the     finished product and organize it by system host name. 

# Instructions on how to get started.

Go to the "Wiki" tab at the top of this page which will walk you through installation.
Proceed going through the wiki in the following order:

* WSL Installation
* WSL Utilities Setup
* SSH Key Pairs
* SSH Configuration File
* Clone Program Final Steps

Once you are done setting up your environment, you will drag the .log session into the working directory folder (vsr_scraper) under the C:/ drive.  Note: only qty. (1) .log file can be present in the working directory or the script will fail. 


