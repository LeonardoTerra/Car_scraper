# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:26:12 2023

@author: leeon
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd
import requests


'''
url = 'https://www.webmotors.com.br/carros/estoque?idcmp=s08%3Ac03%3Ad927b2484af44809b0c79e6f4c4a80c3&tipoveiculo=carros&anunciante=Loja%7CConcession%C3%A1ria&gclsrc=aw.ds&gclid=EAIaIQobChMI2P7utpaDgQMVnjjUAR0dLgb8EAAYASAAEgI-OvD_BwE'

def brands():
    car_brand = []
    soup = BeautifulSoup(page_source, 'lxml')
    
    brand = soup.find_all('a', class_='Filters__line Filters__line__result')
    for i in brand:
        brand_car = i.get_text()
        car_brand.append(brand_car)
        
    return car_brand

brands()

choose_car_brand = input('Brand: ').lower()

sleep(10)

index = brands().index(choose_car_brand) + 1
index

element = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div[2]/div[1]/div[4]/div/div[5]/a['+str(index)+']')
href = element.get_attribute('href')
href

next_page = 'https://www.webmotors.com.br/carros/mg-belo-horizonte/toyota

driver.get(next_page)
'''

'''

car =[]
descrip = []
prices = []

for i in range(1,11):
   try:
       car_name = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div[3]/div[2]/div/div[1]/div/div['+str(i)+']/div/div[2]/a[1]/div[1]/h2')
       car.append(car_name.text)
       
       description = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div[3]/div[2]/div/div[1]/div/div['+str(i)+']/div/div[2]/a[1]/div[1]/h3')
       descrip.append(description.text)
       
   except:
       continue

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

price = soup.find_all('strong', class_="sc-cJSrbW fMdCZZ")
price

for p in price:
    for i in range(1,11):
        prices = p.find_all('strong', class_="sc-cJSrbW fMdCZZ")

prices

car
descrip
prices.replace('\xa0', ' ')
prices

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

price = soup.find_all('strong', class_="sc-cJSrbW fMdCZZ")
price
'''
driver = webdriver.Chrome('C:/Users/leeon/.spyder-py3/chromedriver.exe')
driver.get(url)
'''