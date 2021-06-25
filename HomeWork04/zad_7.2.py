'''
Napisz program odczytujący dane z Twojej nowo utworzonej bazy.

Następnie spróbuj napisać program, który wczytuje dane z bazy i zapisuje je w pliku CSV.

Wykorzystaj napisane już wcześniej klasy/metody do obsługi CSV dla Twoich klas z ogłoszeniami.

'''

import psycopg2
import csv

pi='192.168.1.42'

conn = psycopg2.connect(
    host=pi,
    database='announcements',
    user='u_select',
    password='****'
)

cur = conn.cursor()
cur.execute("select x.*, y.* from annoncement x left join propertyextensions y on y.anoncementID=x.anoncementID where x.sellerID = (select sellerID from Seller where FirstName='Ronald' and Lastname='Regan')")
myresult = cur.fetchall()
for x in myresult:
  print(x)
#print (type(myresult))

with open('regan_announcements.csv', 'w') as f:
    wtr = csv.writer(f, delimiter= ';', lineterminator='\n')
    wtr.writerows(list(myresult))
