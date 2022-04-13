from time import sleep
import logging


from Pages.LoginPage import LoginPage
from Pages.deskBookingsPage import deskBookingsPage
from WebConfig.web_config import TestData
from Tests.test_base import BaseTest
import pytest



'''Logger'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)




class Test_Booking(BaseTest):

    """Non-Recurring"""

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # COVID_DECLARATION Check
        bookinpage.update_health_status()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking for the desk by selecting a default date and time: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_host_change_booking(self):
        # self.loginPage = LoginPage(self.driver)
        # bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage = deskBookingsPage(self.driver)
        bookinpage = self.loginPage
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        # bookinpage.select_location()
        # bookinpage.select_floor()
        # sleep(10)
        bookinpage.select_available_status()

        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        sleep(5)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(10)

        # Covid-declaration check
        bookinpage.update_health_status()

        # Selecting host
        bookinpage.do_click(deskBookingsPage.HOST_DROPDOWN)
        bookinpage.host_selection(deskBookingsPage.HOST_INPUT, TestData.HOST1_NAME)
        print("Selecting host done")
        sleep(5)

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        # bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking for the desk by changing the default host: Passed")
        

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()

        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(10)

        # Selecting host
        bookinpage.do_click(deskBookingsPage.HOST_DROPDOWN)
        bookinpage.host_selection(deskBookingsPage.HOST_INPUT, TestData.HOST2_NAME)
        print("Selecting host done")
        sleep(5)

        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        # bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking for the desk by changing the default date and time: Passed")
        

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)
        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")


    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()

        # Checking available resources
        bookinpage.select_available_status()

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        # bookinpage.resource_page_booking_check()
        # sleep(3)

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(3)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_available_status()

        # Again booking on cancelled time
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)
        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(3)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks after booking: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks after booking: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Again checking if booking is made or not
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Booking of desk by selecting the time of already cancelled booking: Passed")


    # @pytest.mark.skip(reason="no need of currently testing this")
    def test_till_next_date_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()


        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(10)

        # Multiple days
        bookinpage.do_click(deskBookingsPage.MULTIPLE_DAYS_SINGLE_BOOKING)

        # Selecting datetime
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_START, TestData.TILL_NEXT_DAY_START_TIME) 
        bookinpage.time_selection(deskBookingsPage.MULTIPLE_DAYS_SB_END, TestData.TILL_NEXT_DAY_END_TIME)
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a booking of the desk by selecting a date& time such a way that its overlapping the date : Passed")



    """Recurring"""

    '''Daily'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()

        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(10)


        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Repeating Daily
        bookinpage.daily_repeat()

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_multiple_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking for the desk by changing the default date and time.: Passed")


    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.daily_repeat()

        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_daily_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_available_status()

        # Again booking on cancelled time
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.daily_repeat()

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)

        # Again checking if booking is made or not
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()

        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")



    '''Weekly'''
    @pytest.mark.skip(reason="no need of currently testing this")
    def test_simple_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Network logs
        try:
            bookinpage.print_browser_logs()
        except Exception as e:
            print("network exception: ", e)

        # Get total desks value
        try:
            total_desks = bookinpage.get_element_text(deskBookingsPage.TOTAL_DESKS_2ND_FLOOR)
            print("total_desks: ", total_desks)
            available_desks = bookinpage.get_element_text(deskBookingsPage.AVAILABLE_DESKS_2ND_FLOOR)
            print("available_desks: ", available_desks)
        except Exception as e:
            print("Desk count exception: ", e)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # COVID_DECLARATION Check
        # bookinpage.update_health_status()

        # Repeat Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        # checklist = ['SCHEDULED', f'Name: {TestData.DEFAULT_HOSTNAME}', f'Email: {TestData.DEFAULT_HOSTEMAIL}',  'Cancel Booking']
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking by selecting  default date and time and the end day of booking.: Passed")
        bookinpage.quit_driver()

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_datetime_change_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        bookinpage.select_location()
        bookinpage.select_floor()
        bookinpage.select_available_status()

        # Clicking on list view
        print("Clicking on list view")
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)
        sleep(5)

        # Clicking on desk 201 modal
        print("Clicking on desk 201 modal")
        bookinpage.do_click(deskBookingsPage.DESK_201)
        sleep(10)


        # Selecting datetime
        bookinpage.selecting_date()
        bookinpage.select_time()
        print("Selecting datetime done")
        start_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = bookinpage.get_element_text(deskBookingsPage.TIME_SELECT_END)
        print("startcheck: ", end_check)

        # Repeating Daily
        bookinpage.weekly_repeat()

        # Clicking on booking button
        print("Clicking on booking button")
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        print("Booking should be created successfully: Passed")
        sleep(8)

        # Checking Booking
        # At the find resource page, status of booking should be changed from available to booked
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_multiple_date_select()
        bookinpage.resource_page_booking_check()
        sleep(3)

        # Resource details page
        bookinpage.do_click(deskBookingsPage.Desk_201_AFTER_BOOKING_TITLE)
        sleep(8)
        bookinpage.resource_details_date_select()
        checklist = [TestData.HOST1_FULLNAME, TestData.HOST1_EMAIL, start_check, end_check]
        bookinpage.resource_details_page_check()
        sleep(5)

        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        sleep(5)
        print("Create a Daily recurring booking for the desk by changing the default date and time.: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_overlapping_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Checking Booking
        bookinpage.select_booked_status()
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")
        bookinpage.resource_page_booking_check()
        sleep(3)
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.weekly_repeat()

        # Testing overlapping booking
        bookinpage.overlapping_error_check()
        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")

    @pytest.mark.skip(reason="no need of currently testing this")
    def test_already_cancelled_weekly_recurring_booking(self):
        self.loginPage = LoginPage(self.driver)
        bookinpage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        sleep(10)
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        sleep(5)
        print("Selecting Location")
        bookinpage.select_location()
        print("Selecting Floor")
        bookinpage.select_floor()
        # Checking available resources
        bookinpage.select_available_status()
        # Clicking on list view
        bookinpage.do_click(deskBookingsPage.LIST_VIEW_BUTTON)

        # Clicking on desk 201 modal
        bookinpage.do_click(deskBookingsPage.DESK_201)

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        sleep(5)
        print("Booking should be created successfully: Passed")

        # Cancelling Booking
        # In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        bookinpage.do_click(deskBookingsPage.DESK_201_MEETING_OPTIONS_CANCEL_BUTTON)
        sleep(2)

        # Going to Book Space Nav Panel
        bookinpage.do_click(deskBookingsPage.BOOK_SPACE_NAV)
        sleep(3)

        # Checking available resources
        bookinpage.select_available_status()

        # Again booking on cancelled time
        bookinpage.do_click(deskBookingsPage.DESK_201_RPAGE_CHECK_BOOK_BUTTON)

        # Repeating
        bookinpage.weekly_repeat()

        # Selecting time
        bookinpage.select_time()
        
        # Clicking on booking button
        bookinpage.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)

        # Again checking if booking is made or not
        bookinpage.do_click(deskBookingsPage.BOOKING_NAV)
        bookinpage.check_my_booking()

        sleep(5)
        print("Create a booking of desk by selecting the  date & time such a way that booking time is overlapping to the existing booking: Passed")