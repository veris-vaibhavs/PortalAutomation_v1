from Pages.BasePage import BasePage
from WebConfig.web_config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class deskBookingsPage(BasePage):

    '''By XPATH'''
    # Body Xpath
    BODY = (By.CSS_SELECTOR, "body")
    # 
    DESK_NO = 201
    # ------
    BOOKING_NAV = (By.XPATH, f"//h3[text()='Booking']")
    BOOK_SPACE_NAV = (By.XPATH, f"//*[@id='sub-nav']/div[1]")
    LOCATION_DROPDOWN = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[1]/div/div")
    GENPACT_IT_PARK = (By.XPATH, f"/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div/div/div[4]/span[2]/span")
    BUSINESS_TOWER = (By.XPATH, f"/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div/div/div[5]")
    FREE_CLICK = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[1]/p")
    SECOND_FLOOR = (By.XPATH, f"//*[@id='1-floor']/div/div[1]/div[1]")
    STATUS_DROPDOWN = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[3]/div[1]/div/div")
    AVAILABLE_STATUS = (By.XPATH, f"//*[text()='Available']")
    BOOKED_STATUS = (By.XPATH, f"//span[text()='Booked']")
    ASSIGNED_STATUS = (By.XPATH, f"//span[text()='Assigned']")
    INACTIVE_STATUS = (By.XPATH, f"//span[text()='Inactive']")
    ALL_STATUS = (By.XPATH, f"//span[text()='All Status']")
    LIST_VIEW_BUTTON = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/div/div[2]")
    # DESK_201 = (By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr[1]/td[6]/button")
    DESK_AVAIL = (By.XPATH, f"//*[text()='Available']/parent::*/parent::*/following-sibling::*[4]/button")
    DESK_201 = (By.XPATH, f"//*[text()='{DESK_NO}']/parent::*/parent::*/following-sibling::*[5]/button")
    DESK_205 = (By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr[6]/td[6]/button")
    DESK_NUMBER = (By.XPATH, f"//*[@class='desk-title']")

    # 2nd Floor total desks
    TOTAL_DESKS_2ND_FLOOR = (By.XPATH, f"//*[@id='1-floor']/div/div[3]/div[1]/p")
    AVAILABLE_DESKS_2ND_FLOOR = (By.XPATH, f"//*[@id='1-floor']/div/div[3]/div[2]/p")

    # Booking Modal
    BOOKING_CONFIRM_BUTTON = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div/button")
    HOST_DROPDOWN = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[1]/div[1]/div/div[4]/div/div/div[3]/img")
    HOST_INPUT = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[1]/div[1]/div/div[4]/div/div/div")
    HOST_SELECT = (By.XPATH, f"//*[contains(text(), '{TestData.HOST2_FULLNAME}')]")
    
    DATE_DROPDOWN = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div")
    DATE_INPUT = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div")
    DATE_CALENDER_BODY = (By.XPATH, f"/html/body/div[9]/div/div/div/div/div[1]/div[2]")
    DATE_SELECT_2nd = (By.XPATH, f"/html/body/div[6]/div/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td[7]/div")
    TIME_SELECT_START = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div/div")
    TIME_SELECT_END = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div/div")
    MULTIPLE_DAYS_SINGLE_BOOKING = (By.XPATH, f"//*[contains(text(), 'Multiple Days')]")
    MULTIPLE_DAYS_SB_START = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/input")
    MULTIPLE_DAYS_SB_END = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[3]/input")


    # Booking confirmation
    DESK_201_AFTER_BOOKING_DIV = (By.XPATH, f"//*[@id='meeting-room-list']/div/div/div/div/div/div/table/tbody/tr/td[1]/div")
    DESK_201_AFTER_BOOKING_TITLE = (By.XPATH, f"//*[text()='{DESK_NO}']/parent::*/parent::*")

    # Resource Details
    RD_CALENDER_INPUT = (By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div[2]/div/div/input")
    SCHEDULE_LISTING = (By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[3]/div/div/div[2]")
    I_BUTTON = (By.XPATH, f"//*[@class='rbc-event-content']/span")
    I_INFO = (By.XPATH, f"//*[@class='ant-popover-content']")
    I_INFO2 = (By.XPATH, f"/html/body/div[7]/div/div/div")
    RD_TIME_CHECK = (By.XPATH, f"*[@class='rbc-event-label']")
    BOOK_THIS_SPACE = (By.XPATH, f"//*[@id='resource-details-content']/div[1]/div[1]/div/div/div[5]/div/div/div[4]/div/button")
    BOOKING_HOSTNAME = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[1]")
    BOOKING_HOSTEMAIL = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[2]")
    BOOKING_START = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[3]")
    BOOKING_END = (By.XPATH, f"/html/body/div[7]/div/div/div/div[2]/div[2]/div[1]/div[4]")

    # Resource page confirmation
    DATE_CALENDER_RPAGE = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/input")
    BDATE_RPAGE_INPUT = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div/input")
    BDATE_CALENDER_DONE = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/button")
    DESK_201_RPAGE_CHECK_DIV = (By.XPATH, f"//*[@title='{DESK_NO}']/parent::*/parent::div") 
    DESK_201_RPAGE_CHECK_BOOK_BUTTON = (By.XPATH, f"//div[@title='{DESK_NO}']/parent::*/parent::*/following-sibling::*[5]/button") 
    DESK_201_RPAGE_STATUS_CHECK = (By.XPATH, f"//*[@title='{DESK_NO}']/parent::*/parent::td/following-sibling::*[1]/div/div")

    # My Bookings
    MY_BOOKING_NAV = (By.XPATH, f"//*[@id='sub-nav']/div[2]")
    # DESK_201_CHECK_NAME = (By.XPATH, "//p[text()='{}']".format(DESK_NO))
    DESK_201_CHECK_NAME = (By.XPATH, "//*[contains(text(), '{}')]".format(DESK_NO))
    DESK_201_CHECK_DIV = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/parent::div")
    DESK_201_SCHEDULE_CHECK = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*[1]")
    DESK_201_MEETING_OPTIONS_BUTTONS_CHECK = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*[2]")
    DESK_201_MEETING_OPTIONS_CANCEL_BUTTON = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*[2]/div/div/button[2]")
    DESK_201_MEETING_OPTIONS_CANCEL_ALL_DOTS = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/parent::*/preceding-sibling::*/child::*[2]/child::*/child::*/child::*[3]")
    DESK_201_MEETING_OPTIONS_CANCEL_ALL_BUTTON = (By.XPATH, f"//*[text()='Cancel All']")
    MAIN_CARDS_CONATINER = (By.XPATH, f"//*[@id='mainBookingCardsContainer']")


    # Booking Successfull message
    BK_SUCCESS = (By.XPATH, f"/html/body/div[5]/div/div/div/div/div/span[2]")
    BK_OVERLAPPING_ERROR = (By.XPATH, f"/html/body/div[12]/div/div/div/div")
    BK_OVERLAPPING_ERROR_MSG = (By.XPATH, f"//*[contains(text(), 'Error in creating Booking: Booking Exists')]")


    # Health Status
    HEALTH_STATUS_MSG = 'You cannot book the desk since your health status is "Not Filled", Please fill your health status under "My Bookings"'
    HEALTH_STATUS_PROMPT = (By.XPATH, f"//*[contains(text(), 'Update Health Status')]")
    UPDATE_HEALTH_STATUS_BUTTON = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/button")
    FULLY_VACCINATED = (By.XPATH, f"//*[contains(text(), 'Fully Vaccinated')]/preceding-sibling::*/child::*")
    HEALTH_CONDITION_NONE = (By.XPATH, f"//*[contains(text(), 'None')]/preceding-sibling::*/child::*")
    PROVIDING_CARE_NO = (By.XPATH, f"//*[contains(text(), 'If you are providing care to a confirmed /suspect/probable case')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    CONTACT_14DAYS_NO = (By.XPATH, f"//*[contains(text(), 'If you have come in contact with any COVID-19 positive case in the last 14 days')]/parent::*/following-sibling::*/child::div[2]/child::div[2]/child::div/child::div/child::div/child::*")
    OFFICE_TO_VISIT_DROPDOWN = (By.XPATH, f"//*[@id='other_5014']/div")
    OFFICE_TO_VISIT_SELECT = (By.XPATH, f"//*[contains(text(), 'Digicred HQ-New York')]")
    PARKING_DROPDOWN = (By.XPATH, f"//*[@id='other_5015']/div")
    PARKING_SELECT = (By.XPATH, f"//*[contains(text(), '2 Wheeler')]")
    CONFIRM_DECLARATION = (By.XPATH, f"//*[contains(text(), 'Confirm Declaration')]")

    

    # Recurring booking
    DESK_201_CHECK_RDIV = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]")
    DESK_201_RDIV_CANCEL_BUTTON = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*/div[2]/div/p/span[contains(text(),'every day')]/parent::*/parent::*/parent::*/parent::*/following-sibling::*/div/div/button[2]")
    REPEAT_DIV = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[1]/div/div/div[1]")
    REPEAT_DAILY = (By.XPATH, f"//*[contains(text(), 'Daily')]")
    REPEAT_WEEKLY = (By.XPATH, f"//*[contains(text(), 'Weekly')]")
    REPEAT_WEEKLY_DEFAULT_DAY = (By.XPATH, f"//*[contains(text(), 'Wed')]")
    REPEAT_WEEKLY_DAY = (By.XPATH, f"//*[contains(text(), 'Wed')]")
    # REPEAT_TILL_DATE = (By.XPATH, f"//*[@id='meeting-room-desk-booking-modal']/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div")
    REPEAT_TILL_DATE = (By.XPATH, f"//*[contains(text(), 'Ending (on Date)')]/following-sibling::*/child::*/child::*/input")
    MULTIPLE_DAYS = (By.XPATH, f"//*[contains(text(), 'Daily')]")
    MULTIPLE_DAYS_START_DATE = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/input")
    MULTIPLE_DAYS_END_DATE = (By.XPATH, f"//*[@id='meeting-room']/div[2]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/input")
    
    
    # Extend Booking
    PRE_EXTEND_TIME = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*[1]/div/div")
    CHECKIN_BOOKING = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*[2]/div/div/button[1]")
    EXTEND_BOOKING = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/following-sibling::*[2]/div/div/button[2]")
    EXTEND_15_MINS = (By.XPATH, f"//p[text()='15 minutes']")
    EXTEND_30_MINS = (By.XPATH, f"//p[text()='30 minutes']")
    EXTEND_45_MINS = (By.XPATH, f"//p[text()='45 minutes']")
    EXTEND_60_MINS = (By.XPATH, f"//p[text()='60 minutes']")
    EXTEND_BOOKING_TEXT_CONFIRM = (By.XPATH, f"//p[text()='{DESK_NO}']/parent::*/parent::*/following-sibling::div[2]/div")
    
    
    
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

    def select_floor(self):
        self.do_click(self.SECOND_FLOOR)
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

    def get_desk_name(self):
        dval = self.get_element_text(self.DESK_NUMBER)
        # setting desk value
        deskBookingsPage.DESK_NO = dval
        print("DESK_NO: ", self.DESK_NO)
        print("XPATH: ", self.DESK_201_CHECK_NAME)
        return dval
        

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

    def selecting_date(self):
        self.do_click(self.DATE_DROPDOWN)
        sleep(5)
        self.date_selection_chain(self.DATE_INPUT, TestData.BOOKING_DATE, 2)
        dcheck = self.get_element_text(self.DATE_INPUT)
        # assert dcheck == TestData.BOOKING_DATE
        print("dcheck: ", dcheck)
        
    def select_time(self):
        sleep(5)
        self.time_selection(self.TIME_SELECT_START, TestData.TIME_START) 
        self.time_selection(self.TIME_SELECT_END, TestData.TIME_END)

    def check_my_booking(self):
        self.do_click(self.MY_BOOKING_NAV)
        self.scroll_to_element(self.DESK_201_CHECK_DIV)
        sleep(3)
        # Meeting Options
        meeting_options = self.get_element_text(self.DESK_201_MEETING_OPTIONS_BUTTONS_CHECK).split('\n')
        std_meeting_options = ['Check in', '', 'Cancel Booking']
        # assert meeting_options == std_meeting_options
        print("In My booking page, the created booking should be visible with two options i.e Check In and Cancel booking: Passed")
        self.do_click(self.DESK_201_CHECK_DIV)
        sleep(5)

    def resource_page_booking_check(self):
        rpage_status = self.get_element_text(self.DESK_201_RPAGE_STATUS_CHECK)
        assert rpage_status == "Booked"
        print("rpage_status passed as: ", rpage_status)
        print("At the find resource page, status of booking should be changed from available to booked for the booked time frame: Passed")

    def resource_details_date_select(self):
        self.date_selection_chain(self.RD_CALENDER_INPUT, TestData.BOOKING_DATE, 12)
        dcheck = self.get_element_text(self.RD_CALENDER_INPUT)
        print("dcheck: ", dcheck)
        sleep(3)

    def resource_page_date_select(self):
        self.do_click(self.DATE_CALENDER_RPAGE)
        sleep(2)
        self.date_selection_chain(self.BDATE_RPAGE_INPUT, TestData.BOOKING_DATE, 2)
        dcheck = self.get_element_text(self.BDATE_RPAGE_INPUT)
        # assert dcheck == TestData.BOOKING_DATE
        sleep(2)
        self.do_click(self.BDATE_CALENDER_DONE)
        print("dcheck: ", dcheck)
        sleep(5)

    def resource_page_multiple_date_select(self):
        self.do_click(self.DATE_CALENDER_RPAGE)
        sleep(2)
        self.do_click(self.MULTIPLE_DAYS)
        sleep(2)
        self.date_selection_chain(self.MULTIPLE_DAYS_START_DATE, TestData.BOOKING_DATE1, 2)
        dcheck = self.get_element_text(self.MULTIPLE_DAYS_START_DATE)
        sleep(2)
        self.date_selection_chain(self.MULTIPLE_DAYS_END_DATE, TestData.REPEAT_TILL_DATE2, 2)
        dcheck = self.get_element_text(self.MULTIPLE_DAYS_END_DATE)
        # assert dcheck == TestData.BOOKING_DATE
        sleep(2)
        self.do_click(self.BDATE_CALENDER_DONE)
        print("dcheck: ", dcheck)
        sleep(5)

    def overlapping_error_check(self):
        # Selecting time
        self.time_selection(self.TIME_SELECT_START, TestData.TIME_OVERLAPPING_START) 
        self.time_selection(self.TIME_SELECT_END, TestData.TIME_OVERLAPPING_END)
        print("Selecting datetime done")
        start_check = self.get_element_text(self.TIME_SELECT_START)
        print("startcheck: ", start_check)
        end_check = self.get_element_text(self.TIME_SELECT_END)
        print("endcheck: ", end_check)
        sleep(3)
        self.do_click(deskBookingsPage.BOOKING_CONFIRM_BUTTON)
        try:
            enabled_check = self.is_enabled(self.BK_OVERLAPPING_ERROR_MSG)
            print("enabled_check: ", enabled_check)
            if enabled_check == 1:
                error_msg = self.get_element_text(self.BK_OVERLAPPING_ERROR_MSG)
                print("error-msg: ", error_msg)
                print('An error message should be displayed at the portal that " Booking already exist " also show the validity of booking and booking Id.: Passed')
        except Exception as e:
            print("Error 2")


    def daily_repeat(self):
        self.do_click(self.REPEAT_DIV)
        sleep(3)
        self.do_click(self.REPEAT_DAILY)
        sleep(3)
        self.date_selection_chain(self.REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE[:12], 2)

    def weekly_repeat(self):
        self.do_click(self.REPEAT_DIV)
        sleep(3)
        self.do_click(self.REPEAT_WEEKLY)
        sleep(2)
        self.do_click(self.REPEAT_WEEKLY_DEFAULT_DAY)
        sleep(2)
        self.do_click(self.REPEAT_WEEKLY_DAY)
        sleep(3)
        self.date_selection_chain(self.REPEAT_TILL_DATE, TestData.REPEAT_TILL_DATE, 2)

    def extend_booking(self, etime):
        pre_extend_time = self.get_element_text(self.PRE_EXTEND_TIME)
        print("pre_extend_time: ", pre_extend_time)
        self.do_click(self.CHECKIN_BOOKING)
        sleep(12)
        self.do_click(self.EXTEND_BOOKING)
        sleep(5)
        self.do_click(etime)
        sleep(12)
        textend_confirm = self.get_element_text(self.EXTEND_BOOKING_TEXT_CONFIRM)
        print("text: ", textend_confirm)
        assert textend_confirm == "In Use, Booking Extended"
        post_extend_time = self.get_element_text(self.PRE_EXTEND_TIME)
        print("post_extend_time: ", post_extend_time)
        assert pre_extend_time != post_extend_time



    def update_health_status(self):
        val = self.is_enabled(self.HEALTH_STATUS_PROMPT)
        if val == 1:
            self.do_click(self.HEALTH_STATUS_PROMPT)
            sleep(5)
            self.do_click(self.UPDATE_HEALTH_STATUS_BUTTON)
            sleep(2)
            self.do_click(self.FULLY_VACCINATED)
            sleep(2)
            self.do_click(self.HEALTH_CONDITION_NONE)
            sleep(2)
            self.do_click(self.PROVIDING_CARE_NO)
            sleep(2)
            self.do_click(self.CONTACT_14DAYS_NO)
            sleep(2)
            self.do_click(self.OFFICE_TO_VISIT_DROPDOWN)
            sleep(3)
            self.do_click(self.OFFICE_TO_VISIT_SELECT)
            sleep(2)
            self.do_click(self.CONFIRM_DECLARATION)
            sleep(3)
            self.do_click(self.BOOK_SPACE_NAV)
            sleep(3)
            self.do_click(self.DESK_201)
        else:
            pass