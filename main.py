from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

GOOGLE_FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSd5fBM0JEqiF4GgZbbZQjOU7rqJnEEhS8bdEv1beej5xW9yJw/viewform?usp=sf_link"

service = Service("/Users/justinfulkerson/Desktop/chromedriver")
driver = webdriver.Chrome(service=service)


header = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.58473433447266%2C%22east%22%3A-122.29496993017578%2C%22south%22%3A37.67495266283211%2C%22north%22%3A37.84350922703257%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D",headers=header)
soup = BeautifulSoup(response.text, "html.parser")

addresses = [address.text for address in soup.find_all(class_="list-card-addr")]
links = [link['href'] for link in soup.find_all('a', href=True, class_='list-card-link list-card-link-top-margin')]
prices = [price.text for price in soup.find_all(class_='list-card-price')]

for n in range(len(links)):
#loop through data and fill in forms
    driver.get(GOOGLE_FORMS_LINK)

    time.sleep(2)

    address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    try:
        address.send_keys(addresses[n])
        price.send_keys(links[n])
        link.send_keys(prices[n])
    except IndexError:
        continue
    submit_button.click()








