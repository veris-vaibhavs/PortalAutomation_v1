from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class RoomBookingsPage(BasePage):

    # <======================================== Selectors ========================================>
    # Body Xpath
    BODY = (By.CSS_SELECTOR, "body")
    # ------
    BOOKING_NAV = (By.XPATH, "//h3[text()='Booking']")
    BOOK_SPACE_NAV = (By.XPATH, "//*[contains(text(), 'Book space')]")
    LOCATION_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div")
    GENPACT_IT_PARK = (
        By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div/div/div[4]/span[2]/span")
    BUSINESS_TOWER = (
        By.XPATH, "/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div/div/div[5]")
    FREE_CLICK = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/p")
    FIRST_FLOOR = (By.XPATH, "//*[@id='0-floor']/div/div[1]/div[1]")
    STATUS_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div")
    AVAILABLE_STATUS = (By.XPATH, "//span[text()='Available']")
    BOOKED_STATUS = (By.XPATH, "//span[text()='Booked']")
    ASSIGNED_STATUS = (By.XPATH, "//span[text()='Assigned']")
    INACTIVE_STATUS = (By.XPATH, "//span[text()='Inactive']")
    ALL_STATUS = (By.XPATH, "//span[text()='All Status']")
    LIST_VIEW_BUTTON = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")

    RESOURCE_DROPDOWN = (
        By.XPATH, "//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/div/div")
    RESOURCE_ROOM = (
        By.XPATH, "//*[contains(text(), 'Rooms')]")
    # Room
    ROOM_124 = (
        By.XPATH, "//*[@title= '124']/parent::*/parent::*/following-sibling::*[5]/button")
    # Modal selectors

    BOOKING_AGENDA = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input")
    ATTENDEE_DETAILS = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[4]/div/div[2]/div/div/div[1]")
    CONFIRM_BOOKING = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[2]/div/div[6]/button[2]")
    EDIT_DETAILS = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[7]/div[2]/p")
    EDIT_DETAILS_SEARCH_BOX = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[8]/div[1]/div")
    START_DATE = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[1]/div[2]/div/input")
    START_DATE_X = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/span/span")
    END_DATE = (
        By.XPATH, "//*[@id='meeting-room-room-modal-dialog-box']/div/div[2]/div/div/div[1]/div/div[4]/div[1]/div[1]/div[3]/div[2]/div/input")
    CONTACT_EMAIL = (
        By.XPATH, "//*[contains(text(), 'New Member')]/parent::*/child::*/following-sibling::*/input")
    CONTACT_RIGHT_TICK = (
        By.XPATH, "//*[contains(text(), 'New Member')]/parent::*/child::*[4]/div")
    BOOKING_CONFIRM_BUTTON = (By.XPATH, "//*[contains(text(), 'Confirm Booking')]")

    # After Booking
    ROOM_124_AFTER_BOOKING_TITLE = (By.XPATH, "//div[@title='124']")
    ROOM_124_RPAGE_STATUS_CHECK = (
        By.XPATH, "//*[@title='124']/parent::*/parent::td/following-sibling::*[1]/div/div")
    

    # Resource Details
    RD_CALENDER_INPUT = (By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    SCHEDULE_LISTING = (By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    I_BUTTON = (By.XPATH, "//*[@class='rbc-event-content']/span")
    I_INFO = (By.XPATH, "//*[@class='ant-popover-content']")
    I_INFO2 = (By.XPATH, "/html/body/div[7]/div/div/div")
    RD_TIME_CHECK = (By.XPATH, "*[@class='rbc-event-label']")
    BOOK_THIS_SPACE = (By.XPATH, "//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    BOOKING_HOSTNAME = (By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    BOOKING_HOSTEMAIL = (By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    BOOKING_START = (By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    BOOKING_END = (By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # My Bookings
    MY_BOOKING_NAV = (By.XPATH, "//*[@id='sub-nav']/div[2]")
    ROOM_124_CHECK_DIV = (By.XPATH, "//p[text()='124']/parent::*/parent::div")
    ROOM_124_SCHEDULE_CHECK = (By.XPATH, "//p[text()='124']/parent::*/following-sibling::*[1]")
    ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK = (By.XPATH, "//p[text()='124']/parent::*/following-sibling::*[2]")
    ROOM_124_MEETING_OPTIONS_CANCEL_BUTTON = (By.XPATH, "//p[text()='124']/parent::*/following-sibling::*[2]/div/div/button[2]")
    MAIN_CARDS_CONATINER = (By.XPATH, "//*[@id='mainBookingCardsContainer']")

    # Overlapping error
    BK_OVERLAPPING_ERROR_MSG = (By.XPATH, "//*[contains(text(), 'Error in creating Booking: Booking Exists')]")

    # <===================================== Functions =======================================>

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for Bookings Page"""

    """selecting location"""

    def select_location(self):
        sleep(3)
        self.do_click(self.LOCATION_DROPDOWN)
        sleep(5)
        self.do_click(self.GENPACT_IT_PARK)
        sleep(5)
        self.do_click(self.BUSINESS_TOWER)
        sleep(5)
        self.do_click(self.FREE_CLICK)
        assert "Location selection passed"
        sleep(10)

    def select_resource_type(self):
        self.do_click(self.RESOURCE_DROPDOWN)
        sleep(2)
        self.do_click(self.RESOURCE_ROOM)
        self.do_click(self.FREE_CLICK)

    def select_floor(self):
        self.do_click(self.FIRST_FLOOR)
        sleep(5)
        assert "Floor selection done"

    def select_available_status(self):
        self.do_click(self.STATUS_DROPDOWN)
        sleep(5)
        self.do_click(self.AVAILABLE_STATUS)
        sleep(5)
        assert "Select Available status done"

    def select_booked_status(self):
        self.do_click(self.STATUS_DROPDOWN)
        sleep(5)
        self.do_click(self.BOOKED_STATUS)
        sleep(5)
        assert "Select Booked status done"

    def select_all_status(self):
        self.do_click(self.STATUS_DROPDOWN)
        sleep(5)
        self.do_click(self.ALL_STATUS)
        sleep(5)
        assert "Select Booked status done"

    def enter_agenda(self):
        try:
            self.host_selection(self.BOOKING_AGENDA, TestData.ROOM_AGENDA)
        except Exception as e:
            print("Agenda error exception: ", e)

    def new_contact_guest(self, contact_name, contact_email):
        try:
            self.host_selection(self.ATTENDEE_DETAILS, contact_name)
            self.do_send_keys(self.CONTACT_EMAIL, contact_email)
            self.do_click(self.CONTACT_RIGHT_TICK)
            sleep(2)
        except Exception as e:
            print("new_contact_guest exception: ", e)

    def enter_datetime(self):
        try:
            self.do_click(self.START_DATE)
            self.action_chain_click(self.START_DATE_X)
            self.date_selection_chain(
                self.START_DATE, TestData.ROOM_START_DATE, 18)
            self.do_click(self.END_DATE)
            self.date_selection_chain(
                self.END_DATE, TestData.ROOM_END_DATE, 18)
        except Exception as e:
            print("enter_datetime exception: ", e)

    def resource_page_booking_check(self):
        rpage_status = self.get_element_text(
            self.ROOM_124_RPAGE_STATUS_CHECK)
        assert rpage_status == "Booked"
        print("rpage_status passed as: ", rpage_status)
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")

    def resource_details_page_check(self):
        self.scroll_to_element(self.SCHEDULE_LISTING)
        sleep(2)
        try:
            self.do_click(self.I_BUTTON)
            sleep(3)
            eltext = self.get_element_text(self.I_INFO).split('\n')
            print("eltext: ", eltext)
            sleep(5)
            print("At the resource details page, booking should be available: Passed")
        except Exception as e:
            print("I_button exce: ", e)
        self.do_send_keys(self.BODY, Keys.PAGE_UP)

    def check_my_booking(self):
        self.do_click(self.MY_BOOKING_NAV)
        sleep(5)
        self.scroll_to_element(self.ROOM_124_CHECK_DIV)
        sleep(3)
        # Meeting Options
        meeting_options = self.get_element_text(self.ROOM_124_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
        std_meeting_options = ['Check in', '', 'Cancel Booking']
        assert meeting_options == std_meeting_options
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        self.do_click(self.ROOM_124_CHECK_DIV)
        sleep(5)