import os
import threading
from time import sleep

def func1():
    os.system("pytest -v -s --html=report_l7.html -m prs Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
    # os.system("pytest -v -s Tests/test_send_email.py")
    sleep(3)
    os.system("pytest -v -s --html=report_l8.html -m prsc Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")
    # os.system("pytest -v -s Tests/test_send_email.py")
    sleep(3)
    os.system("pytest -v -s --html=report_l9.html -m pcnclb Tests/Positive_Tests/Test_Resource_Booking/test_RoomBooking.py --self-contained-html --capture=sys -rP -rF")

if __name__ == "__main__":
    t1 = threading.Thread(target=func1)

    t1.start()

    # t1.join()