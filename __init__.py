
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):

        BUSQUEDA = "retamar"
        XPATH = "//*[@id='rso']/div[1]/div/div/div/div/h3/a"
        LINK = "RETAMAR. International Baccalaureate World School"


        while(True):
            driver = self.driver
            driver.get("http://www.google.com")
            label = driver.find_element_by_id('lst-ib')
            label.send_keys(BUSQUEDA)
            label.send_keys(Keys.RETURN)
            # BUSCADO POR XPATH
            driver.find_element_by_xpath(XPATH).click()
            # BUSCANDO POR TEXTO DE ENLACE (no consigo que funcione)
            #driver.find_element_by_link_text(LINK).click()

            time.sleep(random.randint(1,3))



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()