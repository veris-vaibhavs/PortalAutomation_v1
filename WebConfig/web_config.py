from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestData:
    CHROME_EXECUTABLE_PATH = "E:\lambda test\chromedriver_win32\chromedriver"
    FIREFOX_EXECUTABLE_PATH = "C:\WebDrivers\geckodriver-v0.30.0-win64\geckodriver"

    BASE_URL = "https://ndl.veris.in/login/NewLogin"
    USER_NAME = "neeraj.dhiman@veris.in"
    PASSWORD = "Passw0rd@123"

    LOGIN_PAGE_TITLE = "Veris | Powering Future Workplaces"

    '''Desk Booking details'''
    DEFAULT_HOSTNAME = "Neeraj Dhiman"
    DEFAULT_HOSTEMAIL = "neeraj.dhiman@veris.in"
    HOST1_NAME = "Shail"
    HOST1_FULLNAME = "Shailendra Tiranga"
    HOST1_EMAIL = "shailendra.tiranga@veris.in"
    HOST2_NAME = "Himans"
    HOST2_FULLNAME = "Himanshi Sharma"
    HOST2_EMAIL = "himanshi.sharma@veris.in"
    BOOKING_DATE = "19 Apr 2022"
    BOOKING_DATE1 = "19 Apr 2022"
    TIME_START = "19:30"
    TIME_END = "19:45"
    TIME_END2 = "22:25"
    TIME_START3 = "22:30"
    TIME_END3 = "22:50"
    TIME_OVERLAPPING_START = "19:25"
    TIME_OVERLAPPING_END = "19:40"
    TILL_NEXT_DAY_START_TIME = "26 Apr 2022 23:55"
    TILL_NEXT_DAY_START_TIME_1 = "26 Apr 2022 23:55"
    TILL_NEXT_DAY_END_TIME = "27 Apr 2022 01:30"
    REPEAT_TILL_DATE = "20 May 2022 01:00"
    REPEAT_TILL_DATE2 = "2 May 2022 23:00"
    DESK_NO = 201

    '''Room booking'''
    ROOM_AGENDA = "Automation testing"
    NEW_CONTACT_1 = "Rahul1"
    NEW_CONTACT_1_EMAIL = "rahul1@gmail.com"
    NEW_CONTACT_2 = "Rahul2"
    NEW_CONTACT_2_EMAIL = "rahul2@gmail.com"
    ROOM_START_DATE = "20 Apr 2022 19:51"
    ROOM_END_DATE = "20 Apr 2022 20:06"
    CONTACT_1_IS_DRAFTED_FALSE = "test veris"
    CONTACT_1_IS_MEMBER = "Johnathan Gracer"
    CONTACT_2_IS_MEMBER = "Mark Jacob"
    ROOM_OVERLAPPING_TIME_START = "20 Apr 2022 19:45"
    ROOM_OVERLAPPING_TIME_END = "20 Apr 2022 20:00"
    ROOM_OVERLAPPING_TIME_END_2 = "27 Apr 2022 01:10"
    ROOM_OVERLAPPING_TIME_START_1 = "27 Apr 2022 01:15"
    ROOM_OVERLAPPING_TIME_END_1 = "27 Apr 2022 01:30"
    REPEAT_FREQUENCY = "1"
    WEEKLY_REPEAT_TILL_DATE = "2 May 2022"
    WEEKLY_REPEAT_TILL_DATE2 = "24 Apr 2022"