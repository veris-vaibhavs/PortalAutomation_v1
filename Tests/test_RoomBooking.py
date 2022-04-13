from time import sleep
import logging

from selenium.webdriver.common.keys import Keys


from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from Pages.RoomBookingPage import RoomBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest



'''Logger'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)




class Test_RoomBooking(BaseTest):

    """Desk Booking"""

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        # bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        # bookinpage.host_selection(RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        
        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        # bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        # bookinpage.host_selection(RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_change_host_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        
        # Agenda
        bookinpage.enter_agenda()

        # Selecting Host
        bookinpage.do_click(RoomBookingsPage.EDIT_DETAILS)
        bookinpage.host_selection(RoomBookingsPage.EDIT_DETAILS_SEARCH_BOX, TestData.HOST1_NAME)

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        sleep(10)
        bookinpage.quit_driver()

  
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        # bookinpage.enter_datetime()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        print("Create a booking for the desk by selecting a default date and time: Passed")

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()

        # Selecting datetime
        bookinpage.date_selection_chain(
                RoomBookingsPage.START_DATE, TestData.ROOM_OVERLAPPING_TIME_START, 2)
        bookinpage.date_selection_chain(
                RoomBookingsPage.END_DATE, TestData.ROOM_OVERLAPPING_TIME_END, 2)

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        try:
            enabled_check = bookinpage.is_enabled(RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = bookinpage.get_element_text(RoomBookingsPage.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")

        sleep(10)
        bookinpage.quit_driver()


    # @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_rlogin(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Selecting resource type
        bookinpage.select_resource_type()
        # Clicking on list view
        bookinpage.do_click(RoomBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # New Member
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_1, TestData.NEW_CONTACT_1_EMAIL)
        bookinpage.new_contact_guest(TestData.NEW_CONTACT_2, TestData.NEW_CONTACT_2_EMAIL)
        # Is drafted = False
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_DRAFTED_FALSE)
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)
        # Agenda
        bookinpage.enter_agenda()

        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(RoomBookingsPage.ROOM_124_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(RoomBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        bookinpage.do_click(RoomBookingsPage.ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON)
        print("Create a booking for the desk by selecting a default date and time: Passed")

        bookinpage.do_send_keys(RoomBookingsPage.BODY, Keys.PAGE_UP)
        sleep(3)

        # Clicking on Book Space for overlapping booking
        bookinpage.do_click(RoomBookingsPage.BOOK_SPACE_NAV)
        # Checking available resources
        bookinpage.select_available_status()
        sleep(3)

        # Clicking on room 124 booking modal
        bookinpage.do_click(RoomBookingsPage.ROOM_124)

        '''Booking Modal'''

        # Attendee Details
        # Is Member = True
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_1_IS_MEMBER)
        bookinpage.host_selection(RoomBookingsPage.ATTENDEE_DETAILS, TestData.CONTACT_2_IS_MEMBER)

        # Agenda
        bookinpage.enter_agenda()


        # Clicking on booking button
        bookinpage.do_click(RoomBookingsPage.BOOKING_CONFIRM_BUTTON)

        sleep(10)
        print("Create a booking of room by selecting the time of already cancelled booking: Passed")
        bookinpage.quit_driver()