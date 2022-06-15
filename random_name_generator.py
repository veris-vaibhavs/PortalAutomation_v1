import requests
import json

def ran_name():
    for i in range(10):
        response_API = requests.get('https://randomuser.me/api/')
        # print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)
        first_name = parse_json['results'][0]['name']['first']
        print("\n\nFirst name:", first_name)
        last_name = parse_json['results'][0]['name']['last']
        print("Last name:", last_name)
        RANDOM_EMAIL = parse_json['results'][0]['email']
        # print("Email:", email)
        RANDOM_FULL_NAME = f'{first_name} {last_name}'
        check = first_name.isascii()
        check1 = last_name.isascii()
        if check is True and check1 is True:
            return [RANDOM_FULL_NAME, RANDOM_EMAIL, first_name, last_name]
        else:
            pass

def ran_name_2():
    for i in range(10):
        response_API = requests.get('https://randomuser.me/api/')
        # print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)
        first_name = parse_json['results'][0]['name']['first']
        print("\n\nFirst name:", first_name)
        last_name = parse_json['results'][0]['name']['last']
        print("Last name:", last_name)
        RANDOM_EMAIL = parse_json['results'][0]['email']
        # print("Email:", email)
        RANDOM_FULL_NAME = f'{first_name} {last_name}'
        check = first_name.isascii()
        check1 = last_name.isascii()
        if check is True and check1 is True:
            return [RANDOM_FULL_NAME, RANDOM_EMAIL, first_name, last_name]
        else:
            pass

if __name__ == '__main__':
    ran_name()
    ran_name_2()
