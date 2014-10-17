from bs4 import BeautifulSoup as BS
import requests
import time

urlbase = "http://www.statistik-bw.de/SRDB/Tabelle.asp?H=11&U=04&T=10025156"

def exists(url):
  time.sleep(1) # delays for 1 second
  soup = BS(requests.get(url).text)
  elem = soup.find('table')
  if not elem:
    print( "Error for: " + url)
  elem = elem.find('tbody')
  if not elem:
    print( "Error for: " + url)
  if not elem:
    print( "Error for: " + url)
  elem = elem.find('th')
  if elem.contents:
    return True
  else:
    return False

debug=True
valid_url_list =[]
#time_range = range(0,7)
las = ["LA"]
if exists(urlbase + "&E=LA&R=LA"):
  valid_url_list.append(urlbase+"&E=LA&R=LA")
valid_rbs = []
for x in range(0,10):
  testurl = urlbase + "&E=RB&R=RB" + ("%01i"%(x))
  if exists(testurl):
      valid_url_list.append(testurl)
      valid_rbs.append(x)
      if debug:
        print(testurl)
        break
#this assumes that regions (RV) are always contained in an RB
valid_rvs = []
for x in valid_rbs:
  for y in range(0,10):
    testurl = urlbase + "&E=RV&R=RV" + ("%02i"%(x*10 + y))
    if exists(testurl):
      valid_url_list.append(testurl)
      valid_rvs.append(x*10 + y)
      if debug:
        print(testurl)
        break
#this assumes that kreise (KR) are always contained in a region (RV)
valid_krs = []
for x in valid_rvs:
  for y in range(0,10):
    testurl = urlbase + "&E=KR&R=KR" + ("%03i"%(x*10 + y))
    if exists(testurl):
      valid_url_list.append(testurl)
      valid_krs.append(x*10+y)
      if debug:
        print(testurl)
        break
valid_ges = []
for x in valid_krs:
  for y in range(0,1000):
    testurl = urlbase + "&E=GE&K=" + ("%03i"%(x)) + "&R=GE" + ("%06i"%(x*1000 + y))
    print("trying " + testurl)
    if exists(testurl):
      valid_url_list.append(testurl)
      valid_ges.append(x*1000+y)
      if debug:
        print(testurl)
        break
#lws = ["LW" + str(x) for x in range(1000,5000)]
#lws = ["BT" + str(x) for x in range(1,5)]






#for x in urllist:
#  soup = BS(requests.get(x).text)
#  for y in soup.find(attrs={"name":"E"}).children:
#    if y == u"\n" or y.get("value") == "EV":
#      continue
#    soup2 = BS(requests.get(x + "&E=" + y.get("value")).text)
#    res = soup2.find(attrs={"name":"K"})
#    if not res:
#        print("Warning, did not find any tables for:" + x + "&U=" + y.get("value"))
#        continue
#    for z in res.children:
#      if z == u"\n" or not z.get("value"):
#        continue
#      liste2.append(x + "&E=" + y.get("value") + "&K=" + z.get("value"))
#print(liste2)
