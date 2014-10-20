import logging
from bs4 import BeautifulSoup as BS

class ResponseParser(object):

    #def __init__(self):
    #    print('nothing')

    """
    Attempt to write a generic parser for the perverted, non-uniformed html tables.
    Works with the following URLs
    """
    def generic_parse(self, html_code):
        ### TODO write data to backend instead into debug messages
        soup = BS(html_code)
        tables = soup.find_all('table')
        for table in tables:
            table_name = table.get('summary')
            logging.debug('Table Name is ""%s"', table_name)
            # TODO parse thead and tfoot for description 
            trs = table.find('thead').find_all('tr')
            logging.debug('More captions: ')
            for tr in trs:
                ths = tr.find_all('th')
                for th in ths:
                    logging.debug(' ** TH: %s', th.contents[0].strip())

            trs = table.find('tbody').find_all('tr')
            for tr in trs:
                th = tr.find('th') 
                logging.debug('- TH: %s',th.contents[0].strip())
                tds = tr.find_all('td')
                for td in tds:
                    logging.debug(' ** TD: %s', td.contents[0].strip())
            
    def parse_average_age(self, html_code):
        self.generic_parse(html_code)
