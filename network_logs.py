import json

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