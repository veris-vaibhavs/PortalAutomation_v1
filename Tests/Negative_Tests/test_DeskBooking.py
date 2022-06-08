from time import sleep
import logging

from selenium.webdriver.common.keys import Keys
from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest
from selenium.webdriver.common.by import By

from mail_conf import send_email

import traceback


'''Logger'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Test_Booking(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(
            TestData.USER_NAME, TestData.PASSWORD)

    @pytest.mark.xfail(reason="The test is expected to fail")
    def test_datetime_change_booking(self):
        bookinpage = deskBookingsPage(self.driver)
        # bookinpage = Test_Booking.test_login()
        sleep(3)
        bookinpage.driver_get_url(TestData.RESOURCE_PAGE_URL)
        sleep(3)
        bookinpage.start_selection()

        # Clicking on available desk
        print("Clicking on available desk")
        bookinpage.select_available_resource()

        # Selecting datetime
        bookinpage.date_selection_chain(deskBookingsPage.DATE_INPUT, TestData.PAST_BOOKING_DATE, 2)

        # Get date input value
        input_value = bookinpage.get_element(deskBookingsPage.DATE_INPUT)
        title = input_value.get_attribute('title')

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.MODAL_CLOSE)
        sleep(2)
        assert title == TestData.PAST_BOOKING_DATE


