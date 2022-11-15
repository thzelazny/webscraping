
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import openpyxl as xl
#from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title
table_row=soup.findAll("tr")
for row in table_row[1:6]:
    td=row.findAll("td")
    rank=td[0].text
    rank=int(rank)
    if int(rank)<6:
        name=td[1].text
        gross=td[5].text.replace(",","")
        gross=gross.replace("$","")
        distributor=td[9].text
        theater_num=td[6].text.replace(",","")
        gross_theater=round((float(gross)/float(theater_num)),2)
        print(f"Rank: {rank}")
        print(f"Movie Name: {name}")
        print(f"Total Gross: ${gross}")
        print(f"Distributor: {distributor}")
        print(f"Average Gross/Theater: $ {gross_theater}")
        print()
        



##
##
##
##

