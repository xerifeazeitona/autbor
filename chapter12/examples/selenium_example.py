from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

# Clicking the page
browser.get('https://inventwithpython.com')
link_element = browser.find_element_by_link_text('Read Online for Free')
link_element.click() # follows the "Read Online for Free" link

# Filling out and submitting forms
browser.get('https://login.metafilter.com')
user_element = browser.find_element_by_id('user_name')
user_element.send_keys('not_a_robot')
password_elem = browser.find_element_by_id('user_pass')
password_elem.send_keys('123456')
password_elem.submit()

# Sending special keys
browser.get('https://nostarch.com')
html_element = browser.find_element_by_tag_name('html')
html_element.send_keys(Keys.END)
html_element.send_keys(Keys.HOME)

browser.close()
