from bs4 import BeautifulSoup as BS
import requests
import time

urlbase = "http://www.statistik-bw.de/SRDB/Tabelle.asp?H=11&U=04&T=10025156"

#tests whether a given URL exists.
#Will not handle errors from BS (e.g., on unexpected page)
def exists(url):
  time.sleep(1) # delays for 1 second
  soup = BS(requests.get(url).text)
  elem = soup.find('table')
  if not elem:
    print( "Error for: " + url)
  elem = elem.find('tbody')
  if not elem:
    print( "Error for: " + url)
  elem = elem.find('th')
  if not elem:
    print( "Error for: " + url)
  if elem.contents:
    return True
  else:
    return False

debug=True
valid_url_list =[]

#LA = all of BW
if exists(urlbase + "&E=LA&R=LA"):
  valid_url_list.append(urlbase+"&E=LA&R=LA")
#RB => Regierungsbezirk (1 digit ID)
valid_rbs = []
for x in range(0,10):
  testurl = urlbase + "&E=RB&R=RB" + ("%01i"%(x))
  if exists(testurl):
      valid_url_list.append(testurl)
      valid_rbs.append(x)
      #for debugging we only need one valid entry
      if debug:
        print(testurl)
        break
#RV => Regions (2 digit ID, where 1st digit is RB)
#this assumes that regions (RV) are always contained in an RB
valid_rvs = []
for x in valid_rbs:
  for y in range(0,10):
    testurl = urlbase + "&E=RV&R=RV" + ("%02i"%(x*10 + y))
    if exists(testurl):
      valid_url_list.append(testurl)
      valid_rvs.append(x*10 + y)
      #for debugging we only need one valid entry
      if debug:
        print(testurl)
        break
#KR => Stadt/Landskreis (3 digit ID, where first 2 digits is RV)
#this assumes that kreise (KR) are always contained in a region (RV)
valid_krs = []
for x in valid_rvs:
  for y in range(0,10): #if KR is only in RB, rather than RV, change to 0,100
    testurl = urlbase + "&E=KR&R=KR" + ("%03i"%(x*10 + y)) #and here to 100 too
    if exists(testurl):
      valid_url_list.append(testurl)
      valid_krs.append(x*10+y)
      #for debugging we only need one valid entry
      if debug:
        print(testurl)
        break
#GE => Gemeinde (6 digit ID, where first 3 digits are KR)
#this assumes Gemeinde (GE) is always contained in a Kreis (KR)
valid_ges = []
for x in valid_krs:
  for y in range(0,1000):
    testurl = urlbase + "&E=GE&K=" + ("%03i"%(x)) + "&R=GE" + ("%06i"%(x*1000 + y))
    print("trying " + testurl)
    if exists(testurl):
      valid_url_list.append(testurl)
      valid_ges.append(x*1000+y)
      #for debugging we only need one valid entry
      if debug:
        print(testurl)
        break

#LW => Landeswahltag (4 digit IDs, but not associated with KRs or BT)
#lws = ["LW" + str(x) for x in range(1000,5000)]
#BT => Bundeswahltag (3 digit IDs, independent of other parameters)
#lws = ["BT" + str(x) for x in range(1,5)]
