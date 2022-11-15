from urllib.request import urlopen
from bs4 import BeautifulSoup
from multiprocessing.connection import Client
import keys2
from twilio.rest import Client

client= Client(keys2.accountSID,keys2.authToken)

TwilioNumber= "+13517775160"

myCellPhone="+17078153039"






webpage = 'https://www.cryptocurrencychart.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

#title=soup.title

table_rows=soup.findAll("tr")
title=soup.title
for row in table_rows[1:6]:
    td=row.findAll("td")
    ranking=int(td[0].text)

    name=td[1].text.rstrip("\n")
    price=td[2].text.replace("$","")
    price=price.replace(",","")
    price=float(price)
    percent=td[4].text
    change=float(percent.replace("%",""))
    change=change/100

    price_difference=round((1-change)*price,2)
    if ranking==1:
        if price<40000:
            message="Bitcoin price has fallen below $40,000!"
            textmessage=client.messages.create(to=myCellPhone,from_=TwilioNumber,
                            body=message)
            print(textmessage.status)
    
    if ranking==2:
        if price<3000:
            message="Ethereum price has fallen below $3,000!"
            textmessage=client.messages.create(to=myCellPhone,from_=TwilioNumber,
                            body=message)
            print(textmessage.status)
    

    print()
    print(f"Ranking: {ranking}")
    print()
    print(f"Name: {name}")
    print(f"Price: ${price}")
    print(f"Percentage change: {percent}")
    print(f"Original Price: ${price_difference}")
    print()





