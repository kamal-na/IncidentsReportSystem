import requests
import time
import json


def main():
    f = open('conf.json', )
    conf = json.load(f)
    start = 0
    while True:
        response = requests.get(conf['url']).json()
        start = response['position']

        if response:
            for res in response:
                requests.post("http://127.0.0.1:8000/incidents", data=res)

        time.sleep(conf['wait_time'])


if __name__ == '__main__':
    main()