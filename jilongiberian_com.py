import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):


        XPATH_USER =  "//*[@id='login-usuario']"
        XPATH_PASS = "//*[@id='login-passwd']"
        USER = 'admin'
        PASS = 'admin'
        CLOSE_XPATH= "//*[@id='logout']"

        while(True):
            driver = self.driver
            driver.get("http://www.jilongiberian.com")

            user = driver.find_element_by_xpath(XPATH_USER)
            user.send_keys(USER)
            pas = driver.find_element_by_xpath(XPATH_PASS)
            pas.send_keys(PASS)
            user.send_keys(Keys.RETURN)

            time.sleep(random.randint(1,3))

            driver.find_element_by_xpath(CLOSE_XPATH).click()
            


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()