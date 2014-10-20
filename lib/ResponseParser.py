import logging
from bs4 import BeautifulSoup as BS

class ResponseParser(object):

    #def __init__(self):
    #    print('nothing')

    """
    Attempt to write a generic parser for the perverted, non-uniformed html tables.
    Works with the following URLs
    @html_code is
    """
    def generic_parse(self, html_code):
        ### TODO write data to backend instead into debug messages
        soup = BS(html_code)
        tables = soup.find_all('table')
        table_names = []
        for table in tables:
            table_name = table.get('summary')
            logging.debug('"Table Name is %s"', table_name)
            # TODO find captions outside tbody
            lines = table.find('tbody').find_all('tr')
            for line in lines:
                th = line.find('th') 
                logging.debug('- TH: %s',th.contents[0].strip())
                tds = line.find_all('td')
                for td in tds:
                    logging.debug(' ** TD: %s', td.contents[0].strip())
            

        #print(table[0].get('summary'))

    def parse_average_age(self, html_code):
        self.generic_parse(html_code)

