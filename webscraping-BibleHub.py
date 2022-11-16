import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://biblehub.com/asv/john/'
chapter=random.randint(1,21)
webpage+=str(chapter)+".htm"

chapter=str(chapter)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req=Request(webpage, headers=headers)

webpage=urlopen(req).read()

soup=BeautifulSoup(webpage, 'html.parser')

page_verses=soup.findAll("div",class_="chap")
#print(page_verses)
#This removes all of html language and leaves us with all of the text
for verse in page_verses:
    verse_list= verse.text.split(".")



myverse=random.choice(verse_list)

#print(f"Chapter: {chapter}, Verse: {myverse}")

message="Chapter: "+" "+chapter+" "+"Verse: "+" "+myverse

print(message)

from multiprocessing.connection import Client
import keys2
from twilio.rest import Client

client= Client(keys2.accountSID,keys2.authToken)

TwilioNumber= "+13517775160"

myCellPhone="+17078153039"


textmessage=client.messages.create(to=myCellPhone,from_=TwilioNumber,
                            body=message)

print(textmessage.status)
