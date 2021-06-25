'''
Napisz program, który sprawdzi w wykazie podatników VAT informacje o firmie
na podstawie jej numeru NIP.

https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat
'6772305518'
'''

import json
import urllib.request
from jsonpath_ng import jsonpath, parse
from datetime import date



nip_str = input('Podaj NIP firmy w formacie 10 znaków: 0123456789: ')

nip_query_str='https://wl-api.mf.gov.pl/api/search/nip/' + nip_str +'?date=' + str(date.today())
print (nip_query_str)
with urllib.request.urlopen(nip_query_str) as response:
    json_data =json.loads(response.read())

    name  = parse('$.result.subject.name').find(json_data)[0].value
    print(f'Nazwa firmy {name} ')

    workingAddress = parse('$.result.subject.workingAddress').find(json_data)[0].value
    print(f'Adres firmy: {workingAddress}')

    statusVat = parse('$.result.subject.statusVat').find(json_data)[0].value
    print(f'Status VAT: {statusVat} ')

    regon = parse('$.result.subject.regon').find(json_data)[0].value
    print(f'Regon: {regon}')

    nip = parse('$.result.subject.nip').find(json_data)[0].value
    print(f'NIP: {nip} ')


