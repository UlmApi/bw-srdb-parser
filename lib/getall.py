from bs4 import BeautifulSoup as BS
import requests

liste=[]
#Get for each H (topic)
for x in range(1,12):
  liste.append("http://www.statistik-bw.de/SRDB/home.asp?H="+str(x)+"&E=GE")

liste2=[]
for x in liste:
  soup = BS(requests.get(x).text)
  for y in soup.find(attrs={"name":"U"}).children:
    soup2 = BS(requests.get(x + "&U=" + y.get(value)).text)
#    for z in soup.find(attrs={"name":"T"}).children:
#      liste2=(y + "&T=" + z.get(value))
