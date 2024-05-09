# import requests
# from bs4 import BeautifulSoup
# import json
# import csv
# import time

# def find_link_for_scholarship(title):
#     url = f"https://cse.google.com/cse&q={title}"
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.raw, "html.parser")
#     search_results = soup.find_all('div', class_='gsc-results')
#     return response.text

from bs4 import BeautifulSoup
import requests, json, lxml

# https://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers


def search_google(query):
    data = []    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    params = {
    "q": "Apply for "+query,    # query example
    "hl": "en",                         # language
    "gl": "uk",                         # country of the search, UK -> United Kingdom
    "start": 0,                         # number page by default up to 0
    #"num": 100                         # parameter defines the maximum number of results to return.
    }

    page_num = 0
    while True:
        page_num += 1
        html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=10)
        soup = BeautifulSoup(html.text, 'lxml')

        for result in soup.select(".tF2Cxc"):
            title = result.select_one(".DKV0Md").text
            try:
                snippet = result.select_one(".lEBKkf span").text
            except:
                snippet = None
            links = result.select_one(".yuRUbf a")["href"]
            
            data.append({
                "title": title,
                "snippet": snippet,
                "links": links
            })  
        if soup.select_one(".d6cvqb a[id=pnnext]"):
            params["start"] += 10
        else:
            break
    return data[0].get('links')
#print(search_google("EBC scholarship"))
#print(json.dumps(data, indent=2, ensure_ascii=False))