# -*- coding: utf-8 -*-

#imports
from lxml import html
import requests
from bs4 import BeautifulSoup
import csv

# define File and write header
file = r"../data/check_24_haftpflicht_data.csv"
ofile  = open(file, "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE, lineterminator = '\n')
writer.writerow(["plz","provider", "tarif", "price","deckungssumme"])
ofile.close()

plzlist = ['59558', '21493','45133','37083','10997','21073', '22089', '20357', '72336','65189','22337','58513','47877']

for plz in plzlist:
    print "########################################################################################"
    print plz
    for p in range(0,13):

        base_url= "https://privathaftpflicht.check24.de/privathaftpflicht/vergleichsergebnis/ajax/?"
        query_data = "coinsured=1&birthdate=1980-06-18&public_service=no&min_insure_sum=5&max_costsharing=0&contract_period_3=no&paymentperiod=year&sortfield=provider&sortorder=asc"
        plz_data = "&zipcode=XXX".replace('XXX', plz)
        page_data = "&page=XXX".replace('XXX', str(p))

        url = base_url+query_data+plz_data+page_data

        #url = "https://privathaftpflicht.check24.de/privathaftpflicht/vergleichsergebnis/ajax/?coinsured=1&birthdate=1980-06-18&public_service=no&zipcode=59558&min_insure_sum=5&max_costsharing=0&contract_period_3=no&paymentperiod=year&sortfield=provider&sortorder=asc&page=9"

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        soup.prettify()

        procuct_data =  soup.find_all(class_="result_box ")

        for product in procuct_data:

            provider = product.find_all(class_="provider_name")[0].get_text().strip().encode('utf-8')
            tarif = product.find_all(class_="tariff_name")[0].get_text().replace('Tarif:','').strip().encode('utf-8')
            price = product.find_all(class_="price_container__amount")[0].get_text().encode('utf-8').replace('€','').strip()
            deckungssumme = product.find_all(class_="c24pv_bullet cp24_bullet_good c24-tooltip-trigger")[0].get_text().split('Mio.')[0].replace('Deckungssumme: ','').strip().encode('utf-8')

            values = (plz, provider, tarif, price, deckungssumme)
            print values

            ofile  = open(file, "a")
            writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
            writer.writerow(values)
            ofile.close()