from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from datetime import timedelta
# import pytz

class TestData:
    
    CHROME_EXECUTABLE_PATH = "chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "C:\WebDrivers\geckodriver-v0.30.0-win64\geckodriver"

    BASE_URL = "https://ndl.veris.in/login/NewLogin"
    USER_NAME = "neeraj.dhiman@veris.in"
    PASSWORD = "Passw0rd@123"
    USER_NAME_2 = "shailendra.tiranga@veris.in"
    PASSWORD_2 = "Ttpl@12345"

    LOGIN_PAGE_TITLE = "Veris | Powering Future Workplaces"

    RESOURCE_PAGE_URL = "https://ndl.veris.in/meeting-room/find-resource"

    
    def time_select(m):
        now = datetime.now()
        future_time = now + timedelta(minutes=m)
        current_time = future_time.strftime("%H:%M")
        print("time_select_start_1: ", current_time)
        return current_time

    def booking_date(d):
        now = datetime.now()
        future_time = now + timedelta(days=d)
        bdate = future_time.strftime("%d %b %Y")
        print("booking_date: ", bdate)
        return bdate

    def repeat_till_date(dys):
        now = datetime.now()
        future_time = now + timedelta(days=dys)
        bdate = future_time.strftime("%d %b %Y")
        print("repeat_till_date: ", bdate)
        return bdate

    def room_datetime(d,m):
        now = datetime.now()
        future_time = now + timedelta(days=d, minutes=m)
        rsdate = future_time.strftime("%d %b %Y %H:%M")
        print("rsdate: ", rsdate)
        return rsdate

    def room_start_overlapping_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=20)
        rsodate = future_time.strftime("%d %b %Y %H:%M")
        print("rsdate: ", rsodate)
        return rsodate

    def room_end_overlapping_datetime():
        now = datetime.now()
        future_time = now + timedelta(minutes=40)
        reodate = future_time.strftime("%d %b %Y %H:%M")
        print("redate: ", reodate)
        return reodate

    '''Desk Booking details'''
    DEFAULT_HOSTNAME = "Neeraj Dhiman"
    DEFAULT_HOSTEMAIL = "neeraj.dhiman@veris.in"
    HOST1_NAME = "Shail"
    HOST1_FULLNAME = "Shailendra Tiranga"
    HOST1_EMAIL = "shailendra.tiranga@veris.in"
    HOST2_NAME = "Himans"
    HOST2_FULLNAME = "Himanshi Sharma"
    HOST2_EMAIL = "himanshi.sharma@veris.in"
    BOOKING_DATE = booking_date(5)
    BOOKING_DATE1 = booking_date(5)
    TIME_START = time_select(15)
    TIME_END = time_select(30)
    TIME_END2 = time_select(20)
    TIME_START3 = time_select(25)
    TIME_END3 = time_select(45)
    TIME_OVERLAPPING_START = time_select(25)
    TIME_OVERLAPPING_END = time_select(45)
    TILL_NEXT_DAY_START_TIME = "26 Apr 2022 23:55"
    TILL_NEXT_DAY_START_TIME_1 = "26 Apr 2022 23:55"
    TILL_NEXT_DAY_END_TIME = "27 Apr 2022 01:30"
    REPEAT_TILL_DATE = f"{repeat_till_date(30)} 01:00"
    REPEAT_TILL_DATE2 = f"{repeat_till_date(30)} 23:00"
    REPEAT_TILL_DATE3 = repeat_till_date(6)
    DESK_NO_1 = None
    DESK_W_ISSUE = ['202']

    '''Room booking'''
    ROOM_W_ISSUE = ['Room Booking rule']
    ROOM_AGENDA = "Automation testing"
    NEW_CONTACT_1 = "Rahul1"
    NEW_CONTACT_1_EMAIL = "rahul1@gmail.com"
    NEW_CONTACT_2 = "Rahul2"
    NEW_CONTACT_2_EMAIL = "rahul2@gmail.com"
    ROOM_START_DATE = room_datetime(2,15)
    ROOM_END_DATE = room_datetime(2,35)
    CONTACT_1_IS_DRAFTED_FALSE = "test veris"
    CONTACT_1_IS_MEMBER = "Johnathan Gracer"
    CONTACT_2_IS_MEMBER = "Mark Jacob"
    CONTACT_3_IS_MEMBER = "Shailendra Tiranga"
    ROOM_OVERLAPPING_TIME_START = room_start_overlapping_datetime()
    ROOM_OVERLAPPING_TIME_END = room_end_overlapping_datetime()
    ROOM_OVERLAPPING_TIME_END_2 = "27 Apr 2022 01:10"
    ROOM_OVERLAPPING_TIME_START_1 = "27 Apr 2022 01:15"
    ROOM_OVERLAPPING_TIME_END_1 = "27 Apr 2022 01:30"

    '''Weekly'''
    ROOM_WSTART_DATE = room_datetime(7,15)
    ROOM_WEND_DATE = room_datetime(7,35)
    REPEAT_FREQUENCY = "1"
    WEEKLY_REPEAT_TILL_DATE = repeat_till_date(21)
    WEEKLY_REPEAT_TILL_DATE2 = "24 Apr 2022"

    '''Amenities'''
    AM_1 = "Dual"
    DUAL_MONITOR = "Dual Monitor"
    AM_QUANTITY = "2"


    '''Tag'''
    TAG = "Engineering Deck"
