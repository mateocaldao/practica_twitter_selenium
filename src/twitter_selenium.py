from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get("http://www.twitter.com")

'''login'''
login = browser.find_element_by_class_name("js-login")
login.send_keys(Keys.RETURN)

'''username and password'''
username = browser.find_element_by_class_name("js-signin-email")
password = browser.find_element_by_name("session[password]")

username.send_keys("mateo.cervino@live.u-tad.com")
password.send_keys("practicaSelenium")
submit = browser.find_element_by_class_name("js-submit")
submit.send_keys(Keys.RETURN)

'''posting tweet'''
tweet = browser.find_element_by_id("tweet-box-home-timeline")
tweet.send_keys("Selenium!!")
post_tweet = browser.find_element_by_class_name("js-tweet-btn")
post_tweet.send_keys(Keys.RETURN)

'''close browser'''
browser.close()