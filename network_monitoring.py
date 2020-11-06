#!/usr/bin/env python3


# Dom Moore
# Midterm Project 401
# Purpose: This script Observes data movement and
#          modifications & sends email notification if and event takes place


# import libraries
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import sys
import ssl
import smtplib
from smtplib import SMTP


# Email enviornment variables

#EmailAddress = os.environ.get('EmailAddr')
#EmailPassword = os.environ.get('EmailPass')



# Email notification trigger

def trigger_email():
    EmailAddress = 'EmailAddr'
    EmailPassword = 'EmailPass'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EmailAddress, EmailPassword)

        subject = 'Network Notification'
        body = 'There has been decection of a file modification in the downloads directory!'

        msg = f'Subject: {subject}\n\n{body}'
        
        smtp.sendmail(EmailAddress, 'EmailAddr' , msg)


# Event Trigger for Email notification

def alert(event):
    trigger_email()
    print('Notification Sent')



# Creating monitoring data and time stamps
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    
    # choosing the path of the directory to observe
    
    path = "/home/ubuntu/Desktop/"
    #path = "C:/Users/IEUser/Desktop"
    
    
    # creating log for the events
    event_handler = LoggingEventHandler()
    event_handler.on_any_event = alert  # Establishing alert for Email Notification
    
    # initiallizing the observer function
   
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    
    # starting the observer function
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()