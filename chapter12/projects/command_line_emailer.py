#! /usr/bin/env python3
"""
Command Line Emailer
Write a program that takes an email address and string of text on the
command line and then, using selenium, logs in to your email account and
sends an email of the string to the provided address.
"""

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def send_email(recipient, message):
    """sends an email with the provided message to the provided recipient"""
    browser = webdriver.Firefox()
    browser.get('https://www.guerrillamail.com/compose')
    element = browser.find_element_by_name('to')
    element.send_keys(recipient)
    element = browser.find_element_by_name('subject')
    element.send_keys('thinken of you')
    element = browser.find_element_by_name('body')
    element.send_keys(message)
    element.submit()

if len(sys.argv) >= 3:
    send_email(sys.argv[1], ' '.join(sys.argv[2:]))
    print('Message sent.')
else:
    print('Usage:\npython command_line_emailer.py <recipient email> <message>')
    