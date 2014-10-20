#!/usr/bin/env python

from lib import ResponseParser
import requests
import logging

### 
average_age_link = "http://www.statistik-bw.de/SRDB/Tabelle.asp?H=1&U=02&T=01035100&E=LA&R=LA"

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    # TODO fetch all links, then get html code from particular   
    rp = ResponseParser.ResponseParser()
    # get html_code 
    av_age = requests.get(average_age_link).text
    rp.parse_average_age(av_age)

if __name__ == "__main__":
    main()
