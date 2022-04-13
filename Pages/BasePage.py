import json
import pprint
import requests
import urllib3

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

"""This is the parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_present_element(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(by_locator))
        return element.text
    
    def host_selection(self, by_locator, elkeys, ex=None):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.send_keys(elkeys)
            sleep(2)
            actions.perform()
            sleep(2)
            select_host = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
            actions.move_to_element(select_host)
            if ex is not None:
                for i in range(0, ex):
                    actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            sleep(2)
        except Exception as e:
            print("host_selection: ", e)

    def date_selection_chain(self, by_locator, dkeys, bstrokes):
        bdate = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(bdate)
        actions.click()
        sleep(2)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
        for i in range(0, bstrokes):
            actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(dkeys)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        sleep(5)
        
    def time_selection(self, bstart, bstart_input):
        start_time = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(bstart))
        actions = ActionChains(self.driver)
        actions.move_to_element(start_time)
        actions.click()
        for i in range(0, 6):
            actions.send_keys(Keys.BACKSPACE)
        actions.send_keys(bstart_input)
        actions.send_keys(Keys.ENTER)
        sleep(2)
        actions.perform()
        sleep(2)

    def action_chain_click(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        print("Element: ", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        sleep(3)
        actions.click(element)
        actions.perform()
        sleep(5)

    def action_chain_key_down(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        print("Element: ", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        sleep(3)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        sleep(5)

    def scroll_to_element(self, by_locator):
        a = None
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element)
            a = 1
            pass
        except:
            print("1st failed")
        if a == None:
            try:
                element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
                self.driver.execute_script("coordinates = arguments[0].getBoundingClientRect();scrollTo(coordinates.x,coordinates.y);", element)
                pass
            except:
                print("2nd failed")

    def quit_driver(self):
        self.driver.quit()

    def print_browser_logs(self):
        request_log = self.driver.get_log("performance")
        # try:
        #     for entry in request_log:
        #         print("in process_browser for loop")
        #         log = json.loads(entry["message"])["message"]
        #         url = "https://ndl.veris.in/api/v4/organization/56/resources/analytics/?date_from=2022-04-07T10:52:20.249Z&date_to=2022-04-07T16:52:20.250Z&resource_id=6871"
        #         if (
        #             url in log["params"]["headers"]["url"]
        #             # or "Network.request" in log["method"]
        #             # or "Network.webSocket" in log["method"]
        #         ):
        #             yield log

        #             content = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]['requestId']})
        #             print("content: ", content)
        #             break
        # except Exception as e:
        #     print("logging error: ", e)
        events = process_browser_logs_for_network_events(request_log)
        with open("log_entries.txt", "wt") as out:
            for event in events:
                pprint.pprint(event, stream=out)



def process_browser_logs_for_network_events(logs):
    print("in process_browser")
    for entry in logs:
        print("in process_browser for loop")
        log = json.loads(entry["message"])["message"]

        url = "https://ndl.veris.in/api/v4/organization/56/resources/analytics/?date_from=2022-04-07T10:52:20.249Z&date_to=2022-04-07T16:52:20.250Z&resource_id=6871"
        if (
            url in log["params"]["headers"]["url"]
            # or "Network.request" in log["method"]
            # or "Network.webSocket" in log["method"]
        ):
            yield log