from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()  #opening chrome browser

with open('profiles.txt') as f:
    urls = [line.strip() for line in f if line.strip()]

data = []

for url in urls:
    driver.get(url)
    time.sleep(3)  # adding this so that I can give the time to load the profile
    try:
        name = driver.find_element(By.TAG_NAME, 'h1').text
    except:
        name = ''
    try:
        title = driver.find_element(By.CLASS_NAME, 'text-body-medium').text
    except:
        title = ''
    data.append({'url': url, 'name': name, 'title': title})

driver.quit()

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['url', 'name', 'title'])
    writer.writeheader()
    writer.writerows(data)

print("Done! Scraped data saved to output.csv")
