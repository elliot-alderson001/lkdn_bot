from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class JobApplicationBot:
    
    def __init__(self, config):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=webdriver.ChromeOptions())
    
    def login(self):
        self.driver.get("https://www.linkedin.com/login")

    def run(self):
        self.login()
        html = self.driver.page_source
        sleep(5)
        self.driver.quit()