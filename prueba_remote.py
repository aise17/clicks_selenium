from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://google.es")
busqueda =driver.find_element_by_xpath("//*[@id='lst-ib']")
busqueda.send_keys("retamar")
busqueda.send_keys(Keys.RETURN)


time.sleep(2)
    
driver.close()


