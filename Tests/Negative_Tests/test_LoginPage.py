from time import sleep
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from Pages.LoginPage import LoginPage

from mail_conf import send_email

class Test_Login(BaseTest):
    
    resource_manager = "resource-manager"

    @pytest.mark.skip(reason="no need of currently testing this")
    # @pytest.mark.custom
    def test_login_page(self):
        self.loginPage = LoginPage(self.driver)
        loginpage = self.loginPage.do_login(
                    TestData.USER_NAME, TestData.PASSWORD)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url
        print("Login done successfully: ", current_url)

    '''invalid username/pwd'''
    @pytest.mark.xfail(reason="The test is expected to fail")
    def test_login_1(self):
        self.loginPage = LoginPage(self.driver)
        loginpage = self.loginPage.do_login(
                    TestData.INCORRECT_USERNAME, TestData.INCORRECT_PASSWORD)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url


    '''valid username but invalid pwd'''
    @pytest.mark.xfail(reason="The test is expected to fail")
    def test_login_2(self):
        self.loginPage = LoginPage(self.driver)
        loginpage = self.loginPage.do_login(
                    TestData.USER_NAME, TestData.INCORRECT_PASSWORD)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url


    '''invalid username but valid pwd'''
    @pytest.mark.xfail(reason="The test is expected to fail")
    def test_login_3(self):
        self.loginPage = LoginPage(self.driver)
        loginpage = self.loginPage.do_login(
                    TestData.INCORRECT_USERNAME, TestData.PASSWORD)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url


    '''blank username/pwd'''
    @pytest.mark.xfail(reason="The test is expected to fail")
    def test_login_4(self):
        self.loginPage = LoginPage(self.driver)
        username = ""
        password = ""
        loginpage = self.loginPage.do_login(
                    username, password)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url


    '''blank username but valid pwd'''
    @pytest.mark.xfail(reason="The test is expected to fail")
    def test_login_5(self):
        self.loginPage = LoginPage(self.driver)
        username = ""
        loginpage = self.loginPage.do_login(
                    username, TestData.INCORRECT_PASSWORD)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url

    '''valid username and blank pwd'''
    @pytest.mark.xfail(strict=True, reason="The test is expected to fail")
    def test_login_6(self):
        self.loginPage = LoginPage(self.driver)
        password = ""
        loginpage = self.loginPage.do_login(
                    TestData.INCORRECT_USERNAME, password)
        sleep(2)
        current_url = loginpage.current_url()
        assert self.resource_manager in current_url



    '''Send report'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_send_email_report(self):
        print("Sending report in mail....")
        # send_email()


sleep(5)