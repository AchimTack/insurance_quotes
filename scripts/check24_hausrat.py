# -*- coding: utf-8 -*-

#imports
from lxml import html
import requests
from bs4 import BeautifulSoup
import csv

# define File and write header
file = r"../data/check_24_hausrat_data.csv"
ofile  = open(file, "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONE, lineterminator = '\n')
writer.writerow(["plz","provider", "tarif", "price"])
ofile.close()

plzlist = ['59558', '21493','45133','37083','10997','21073', '22089', '20357', '72336','65189','22337','58513','47877']

for plz in plzlist:
    print "########################################################################################"
    print plz

    base_url= "https://hausratversicherungen.check24.de/hausrat/vergleichsergebnis/?"
    query_data = "module_elementary_city=Hamburg&birthdate=01.08.1999&public_service=no&insurancesum=52000&bike_percentage=0&module_glass=no&building_type=&module_elementary=no&module_elementary_street_select=&module_elementary_street=&module_elementary_street_number=&costsharing=0&paymentperiod=year&contractperiod=1&grade_excellent=no&grade_very_good=no&cct_param2=&reference_lead_id=&gross_negligence=&valuables=&storm_hail_damage=&ebikes_pedelecs=&hausrat_kfz=&hausrat_hotelroom=&garden_equipment=&buggy=&washing_machine=&sortfield=provider&sortorder=asc&squaremeter=80"

    plz_data = "&zipcode=XXX".replace('XXX', plz)

    url = base_url+query_data+plz_data

    #print url

    #url = "https://privathaftpflicht.check24.de/privathaftpflicht/vergleichsergebnis/ajax/?coinsured=1&birthdate=1980-06-18&public_service=no&zipcode=59558&min_insure_sum=5&max_costsharing=0&contract_period_3=no&paymentperiod=year&sortfield=provider&sortorder=asc&page=9"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()

    procuct_data =  soup.find_all(class_="result_box ")

    for product in procuct_data:

        provider = product.find_all(class_="provider_name")[0].get_text().strip().encode('utf-8')
        tarif = product.find_all(class_="tariff_name")[0].get_text().replace('Tarif:','').strip().encode('utf-8')
        price = product.find_all(class_="price_container__amount")[0].get_text().encode('utf-8').replace('€','').strip()
        #deckungssumme = product.find_all(class_="c24pv_bullet cp24_bullet_good c24-tooltip-trigger")[0].get_text().split('Mio.')[0].replace('Deckungssumme: ','').strip().encode('utf-8')

        values = (plz, provider, tarif, price)
        print values

        ofile  = open(file, "a")
        writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        writer.writerow(values)
        ofile.close()