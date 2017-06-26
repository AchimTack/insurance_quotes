# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Achim
#
# Created:     25.06.2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import shuffle
import time
import csv


# read plz list
plzList = []
plzFile = r'../data/plz_einwohner.csv'
with open(plzFile, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
    for row in spamreader:
        plzList.append(row[0])

del plzList[0]

shuffle(plzList)

# define File and write header
file = r"../data/axa/axa_out.csv"

for plz in plzList:
    try:
        driver = webdriver.Chrome()

        #Open Axa-Page
        url = 'https://entry.axa.de/dvtph/#Start'
        driver.get(url)
        time.sleep(3)

        # Select Single
        driver.find_element_by_xpath('//*[@id="businessCaseSingle"]').click()
        time.sleep(2)

        # Insert PLZ
        text_area = driver.find_element_by_xpath('//*[@id="kundepostleitzahl"]')
        text_area.send_keys(str(plz))
        time.sleep(1)
        text_area.send_keys(Keys.RETURN)
        time.sleep(4)

        # Read Prices
        price_s = driver.find_element_by_xpath('//*[@id="preisS"]').text
        price_m = driver.find_element_by_xpath('//*[@id="preisM"]').text
        price_l = driver.find_element_by_xpath('//*[@id="preisL"]').text

        price_s = price_s.encode('utf-8').replace('€','').strip()
        price_m = price_m.encode('utf-8').replace('€','').strip()
        price_l = price_l.encode('utf-8').replace('€','').strip()

        values = (plz, price_s, price_m, price_l)
        print values

        # write values to file
        ofile  = open(file, "a")
        writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        writer.writerow(values)
        ofile.close()

        driver.close()

    except Exception as r:
        print r