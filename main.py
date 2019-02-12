#!/usr/bin/env python3

import requests
import json
import re
from selenium import webdriver
from bs4 import BeautifulSoup

def headlessDownload(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    options = webdriver.ChromeOptions()
    options.binary_location = '/Applications/Chromium.app/Contents/MacOS/Chromium'
    options.add_argument('headless')
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    response = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
    driver.close()
    driver.quit()

    return response

#mobile_de
response = headlessDownload("https://www.mobile.de")
soup = BeautifulSoup(response, "html.parser")
counts = soup.find_all("span", attrs={'id' : 'qssubhc'})
result_size = 0

for count in counts:
    result_size = count.text

result_size = re.sub('[^0-9]','', result_size)
print("Mobile.de: " + result_size)

#sauto
response = requests.get("https://www.sauto.cz/?ajax=1&condition=1&condition=2&condition=4&category=1&nocache=419")
response = response.text
data = json.loads(response)
result_size = data["resultSize"]
result_size = re.sub('[^0-9]','', result_size)
print("Sauto: " + result_size)

#tipcars
response = headlessDownload("https://www.tipcars.com/")
soup = BeautifulSoup(response, "html.parser")
counts = soup.find_all("div", attrs={'class' : 'fs-nejmensi'})
result_size = 0

for count in counts:
    result_size = count.text

result_size = re.sub('[^0-9]','', result_size)
print("Tipcars: " + result_size)

#otomoto_pl
response = requests.get("https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on")
response = response.text
soup = BeautifulSoup(response, "html.parser")
counts = soup.find_all("span", attrs={'class' : 'counter'})
result_size = 0

for count in counts:
    result_size = count.text
    break

result_size = re.sub('[^0-9]','', result_size)
print("Otomoto: " + result_size)

#olx_pl
response = requests.get("https://www.olx.pl/motoryzacja/samochody/")
response = response.text
soup = BeautifulSoup(response, "html.parser")
sections = soup.find_all("section", attrs={'id' : 'body-container'})
result_size = 0

for section in sections:
    data = section['data-facets']
    data = json.loads(data)
    result_size = data['offer_seek']['offer']
    break

print("OLX: " + str(result_size))

#hasznaltauto-hu
response = headlessDownload("https://www.hasznaltauto.hu")
soup = BeautifulSoup(response, "html.parser")
counts = soup.find_all("span", attrs={'class' : 'total-count'})
result_size = 0

for count in counts:
    result_size = count.text

result_size = re.sub('[^0-9]','', result_size)
print("Hasznaltauto: " + result_size)

#bazos
response = requests.get("https://auto.bazos.cz")
response = response.text
data = re.findall("z [0-9]*</td>", response)
result_size = 0

for line in data:
    result_size = line

result_size = re.sub('[^0-9]','', result_size)
print("Bazos.cz: " + result_size)

#auto_bazar_sk
response = requests.get("https://www.autobazar.sk/api/count/v2/?t=57&p[categories][0][]=1&p[order]=23")
response = response.text
data = json.loads(response)
result_size = data['count']

print("Autobazar.sk: " + str(result_size))

#autoscout24
response = headlessDownload("https://www.autoscout24.cz")
data = re.findall('\"initialTotalCount\" : \d+,', response)
result_size = 0

for line in data:
    result_size = line
    break

result_size = re.sub('[^0-9]','', result_size)
print("Autoscout24: " + result_size)

#autorola
response = requests.get("https://www.autorola.cz/dealer/auctions")
response = response.text
soup = BeautifulSoup(response, "html.parser")
results = soup.find_all("span", attrs={"id" : "showResults"})
result_size = 0

for result in results:
    result_size = result.text

result_size = re.sub('[^0-9]','', result_size)
print("Autorola: " + result_size)

#autobazar_eu
response = requests.get("https://www.autobazar.eu/sk/resultselastic.php?countonly=true&version=2&cat=&advanced=&BrandID%5B%5D=0&CarModelID%5B%5D=0%7C0&made_from=&made_to=&price_from=0&price_to=&currency=2&fuel=&drivenkm_from=&drivenkm_to=&type=&power=&importeu=N&doors=&transmissiontype=&newcars=&damaged=&autoporadca=&age=&sortby=&utype=&zip=&kms=15&checkcountry1=on&checkcountry2=on")
response = response.text
result_size = re.sub('[^0-9]','', response)
print("Autobazar.eu: " + result_size)
