from bs4 import BeautifulSoup as BS
import requests

liste=[]
#Get for each H (topic)
for x in range(1,12):
  liste.append("http://www.statistik-bw.de/SRDB/home.asp?H="+str(x)+"&E=GE")

liste2=[]
found =[]
for x in liste:
  soup = BS(requests.get(x).text)
  for y in soup.find(attrs={"name":"U"}).children:
    if y == u"\n":
      continue
    soup2 = BS(requests.get(x + "&U=" + y.get("value")).text)
    res = soup2.find(attrs={"name":"T"})
    if not res:
        print("Warning, did not find any tables for:" + x + "&U=" + y.get("value"))
        continue
    for z in res.children:
      if z == u"\n" or not z.get("value"):
        continue
      liste2.append(x + "&U=" + y.get("value") + "&T=" + z.get("value"))

print(liste2)
