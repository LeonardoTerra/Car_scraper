# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:48:04 2023

@author: leeon
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd
import requests

url = 'https://www.webmotors.com.br/carros/mg-belo-horizonte/toyota/corolla?o=5'

response = requests.get(url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
response.request.headers["User-Agent"]

driver = webdriver.Chrome('C:/Users/leeon/.spyder-py3/chromedriver.exe')
driver.get(url)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

cars = []
prices = []
years = []
km = []
description = []

car = soup.find_all('h2', class_="sc-hqyNC eJNFrU")
for c in car:
    cars.append(c.string)

prices = []
price = soup.find_all('strong', class_="sc-cJSrbW fMdCZZ")
for p in price:
    prices.append(p.string)

for i in range(1,25):
    try:
        year = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div[3]/div[2]/div/div[1]/div/div['+str(i)+']/div/div[2]/a[2]/div[2]/div[1]/span').text
        years.append(year)
        
        kms = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div[3]/div[2]/div/div[1]/div/div['+str(i)+']/div/div[2]/a[2]/div[2]/div[2]/span').text
        km.append(kms)
        
        desc = driver.find_element(By.XPATH,'//*[@id="root"]/main/div[1]/div[3]/div[2]/div/div[1]/div/div['+str(i)+']/div/div[2]/a[1]/div/h3').text
        description.append(desc)
        
    except NoSuchElementException:
        continue

