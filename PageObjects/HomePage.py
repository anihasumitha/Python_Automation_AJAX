from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

from TestData.HomePageData import Data
from TestLocators.HomePageLocators import Locators
class HomePage:

    def __init__(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait=WebDriverWait(self.driver,10)

    def start(self,url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            return True

        except Exception as e:
            print("Error Launching Page", e)

