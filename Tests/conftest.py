from http.server import executable
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from WebConfig.web_config import TestData
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--start-maximized')
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options, desired_capabilities=caps)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(100)
    yield 
    web_driver.close()


    