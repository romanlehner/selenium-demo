from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest

@pytest.fixture
def browser(request):
    driver = webdriver.Remote(
       command_executor='http://selenium-hub:4444/wd/hub', 
       desired_capabilities=DesiredCapabilities.CHROME)
    yield driver
    driver.quit()

def test_browser_interaction(browser):
   browser.get("http://www.python.org")
   element = browser.find_element_by_class_name("donate-button")
   assert element.text == 'Donate'