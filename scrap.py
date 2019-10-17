#importing required libraries
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#giving path to driver for accessing the browser
binary = FirefoxBinary('/usr/lib/firefox/firefox')
driver = webdriver.Firefox(firefox_binary=binary)

#executing driver to access the link
driver.get("https://www.flipkart.com/search?q=mobile+phone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_6&otracker1=AS_Query_OrganicAutoSuggest_1_6&as-pos=1&as-type=RECENT&as-backfill=on")

#creating empty list to store the data
names = []
prices = []
ratings = []

#getting the content of webpage
content = driver.page_source
soup = BeautifulSoup(content,"lxml")

#finding the data with specified tag
for i in soup.find_all('a' , href=True ,attrs={'class':'_31qSD5'}):
    name = i.find('div' , attrs={'class':'_3wU53n'})
    price = i.find('div' , attrs={'class' : '_1vC4OE _2rQ-NK'})
    rating = i.find('div' , attrs = {'class': 'hGSR34'})
    names.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

#Setting up the data frame from scrapped data
df = pd.DataFrame({'Name ':names , 'Price':prices ,'Ratings':ratings})

#creating a csv file to store the scrapped data
df.to_csv('ScrapResult.csv',index=False ,encoding = 'utf-8')
