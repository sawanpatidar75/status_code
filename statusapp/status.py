import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import os
from requests.exceptions import HTTPError
from requests import exceptions
from . import views

# with open('www.python.org') as file:
# print(json.load('https://www.stackoverflow.com'))

url = 'url_search'
grab = requests.get(Search_)
soup = bs(grab.text, "html.parser")
if os.path.isfile('text.csv'):
    f = open('text.csv', 'w')
    for link in soup.find_all('a'):
        data = link.get('href')
        f.write(data)
        f.write('\n')
    f.close()
else:
    c = open("text.csv","x")
    f = open('text.csv', 'w')
    for link in soup.find_all('a'):
        data = link.get('href')
        f.write(data)
        f.write('\n')
    f.close()


# df = pd.read_csv('text.txt')
with open("text.csv","r") as df:
# with open("text.txt", "r") as a_file:
#   for url in a_file:
#     stripped_line = url.strip()
    # print(stripped_line)
    for url in df:

        if url[0:4] == ('http'):
            url = url.strip('/')
            try:
                response = requests.get(url)
                status = response.status_code
                if status == 200:
                    print(url,"status is",status)
                elif status == 500:
                    print(url,"status is",status)
                else:
                    print(url,"status is",status)
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  # Python 3.6
            except Exception as err:
                print(f'Other error occurred: {err}')  # Python 3.6
            else:
                print('Success!')
        else:
            url = url.strip('/')
            url = ('https://www.allsafe.in/{}'.format(url))
            response = requests.get(url)
            status = response.status_code
            if status == 404:
                print(url, "status is", status)
            elif status == 500:
                print(url, "status is", status)
            else:
                print(url, "status is", status)

