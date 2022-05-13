from http.server import executable
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options
from WebConfig.web_config import TestData
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.utils import ChromeType


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("enable-automation")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    if request.param == "chrome":
    #    web_driver = webdriver.Chrome(executable_path="chromedriver", options=options, desired_capabilities=caps)
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options, desired_capabilities=caps) 
 
    #    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options, desired_capabilities=caps)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(100)
    yield 
    print("\nteardown")
    web_driver.close()



# #Test arguments
# @pytest.fixture
# def email_pytest_report(request):
#     "pytest fixture for device flag"
#     return request.config.getoption("--email_pytest_report")
 
# #Command line options:
# parser.addoption("--email_pytest_report",
# dest="email_pytest_report",
# help="Email pytest report: Y or N",
# default="N")
 
# def pytest_terminal_summary(terminalreporter, exitstatus):
#     "add additional section in terminal summary reporting."
#     if not hasattr(terminalreporter.config, 'workerinput'):
#         if terminalreporter.config.getoption("--email_pytest_report").lower() == 'y':
#             #Initialize the Email_Pytest_Report object
#             email_obj = Email_Pytest_Report()
#             # Send html formatted email body message with pytest report as an attachment
#             email_obj.send_test_report_email(html_body_flag=True,attachment_flag=True,report_file_path= 'default')