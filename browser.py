import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from datetime import datetime
from BrainBucket.utils.config_reader import ConfigReader
from json import *


class Browser:
    """
    This class is wrapper around Selenium driver
    """

    def __init__(self, url, browser_name="", wait_time=10):
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path='drivers/geckodriver')
        elif browser_name.lower() == "chrome":
            try:
                self.chrome_path = r"C:\Users\Aleksei ThinkPad\PycharmProjects\chromedriver.exe"
                self.driver = webdriver.Chrome(executable_path=self.chrome_path)
            except WebDriverException:
                print("Webdriver path wrong", self.chrome_path)

            self.driver.get(url)

        elif browser_name.lower() == 'remote':
            config = ConfigReader(r"C:\Users\Aleksei ThinkPad\PycharmProjects\pythonProject\BrainBucket\BDDBehave\Chapter17_1_1\config.ini")
            BROWSERSTACK_URL = config.get_browserstack_url('environment')

            desired_cap_str = config.get_desired_cap('environment')

            desired_cap = json.loads(desired_cap_str)
            print('You set REMOTE!!!', desired_cap )

            self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
            self.driver.get(url)

        self.wait = WebDriverWait(self.driver, wait_time)

        self.driver.maximize_window()
        self.driver.implicitly_wait(wait_time)  # by default 10, but we can add this like a parameter

    def save_screenshot(self):
        now = datetime.now()
        filename = "./screenshots/" + now.strftime("%d%m%Y_%H%M%S.png")
        self.driver.save_screenshot(filename)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
