#!/usr/bin/env python

"""
Send Mail using smtplib and email modules.

This module will send mail by connecting to an SMTP server and
sending mail using the From: To: Subject: method.
I can also send attachments by guessing the attachment type.

Usage: mailit.py -f <from> -r <to> -s <Subject> -b <body> -a <attachment>
"""
import smtplib
import email

def main():
  """
  Nothing for now.
  """
  pass

if __name__ == "__main__":
    main()
