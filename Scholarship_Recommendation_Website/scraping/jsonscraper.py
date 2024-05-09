import json
import time
import random
from datetime import datetime, timedelta
from search import search_google
def random_date():
    month = {
        "Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30,
        "May": 31, "Jun": 30, "Jul": 31, "Aug": 31,
        "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31
    }
    mnth = random.choice(list(month.keys()))
    day = random.randint(1, month[mnth])
    year = 24
    return f"{day}-{mnth}-{year}"
random_funds = ["$3000", "$5000", "Fully Funded", "Partial Funded", "$5000", "$6000", "$7000", "$1000", "$10000", "$1500", "$1800", "$5500", "$3500", "$100000"]
random_degrees = ["Phd", "Bachelor", "Master"]

with open("dataset.json", "r") as file:
    data = json.load(file)
count = 0
for i in range(536, len(data)):
    if count > 20:
        with open('dataset.json', "w") as file:
            json.dump(data, file,ensure_ascii=False, indent=4)
        time.sleep(180)
        count = 0
    data[i]['link'] = search_google(data[i]['title'])
    print("done")
    count += 1
    # if item['degrees'] == "":
    #     item['degrees'] = random.choice(random_degrees)
    #item['link'] = ""
    #item['category'] = ""
with open('dataset.json', "w") as file:
    json.dump(data, file,ensure_ascii=False, indent=4)
