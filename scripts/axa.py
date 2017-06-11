# scrape insurance quotes by postcode from axa

import requests
import json

url = 'https://entry.axa.de/dvtph/api/v1/tarifierung/quote'

headers = {'Origin': 'https://entry.axa.de',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Content-Type': 'application/json',
           'Accept': 'application/json',
           'Referer': 'https://entry.axa.de/dvtph/?ORGANUMMER=8834002000&AKTIONSCODE=140064',
           'Cookie': 'SCDID_S=3jJL78MqydIT7Tex8gKwuj6rVmA4GiFj8T7LpUIlWNk6otg40-Qaew$$; tc_cj_v2=%5Ecl_%5Dny%5B%5D%5D_mmZZZZZZKNSQKSNOPRPSOZZZ%5D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-567715-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; _ga=GA1.2.1375158739.1497181710; _gid=GA1.2.1446442312.1497181710; optimizelySegments=%7B%223116630505%22%3A%22direct%22%2C%223135560399%22%3A%22false%22%2C%223141240426%22%3A%22none%22%2C%223147560115%22%3A%22gc%22%2C%223379340060%22%3A%22true%22%7D; optimizelyEndUserId=oeu1497181713284r0.09876102621117822; optimizelyBuckets=%7B%7D; _gat=1',
           'Connection': 'keep-alive',
           'DNT': '1'
           }

payload = {"organummer": "8834002000",
           "aktionscode": "14015D",
           "versicherungsBeginn": {"day": 12, "month": 6, "year": 2017},
           "produktPaket": "S",
           "haushalt": "SINGLE_MIT_KIND",
           "postleitzahl": "59558",
           "stadt": "Lippstadt",
           "selbstbeteiligung": "KEINE",
           "paymentCycle": "YEARLY",
           "schaedenLetzte12Monate": "UNKNOWN",
           "bausteine": ["VERSICHERUNGSSUMME"]}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print r
