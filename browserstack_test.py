
import time
from BrainBucket.webelements.UIElement import UIElement as Element
from BrainBucket.webelements.browser import Browser
from selenium.webdriver.common.by import By
URL = 'https://techskillacademy.net/brainbucket/index.php?route=account/login'

browser = Browser(URL, 'remote')
login_btn = Element(browser, By.XPATH, '//*[@value="Login"]')
login_btn.click()

time.sleep(1)
browser.shutdown()
