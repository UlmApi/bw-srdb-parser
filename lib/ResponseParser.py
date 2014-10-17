from bs4 import BeautifulSoup as BS

class ResponseParser(object):

    def __init__(self):
        print('nothing')

    def generic_parse(self, html_code):
        soup = BS(html_code)
        tables = soup.find_all('table')
        table_names = []
        for table in tables:
            table_names.append(table.get('summary'))
            # TODO find captions outside tbody
            lines = table.find('tbody').find_all('tr')
            for line in lines:
                th = line.find('th') 
                print(th.contents[0].strip())
                tds = line.find_all('td')
                for td in tds:
                    print(td.contents[0].strip())
            if(len(table_names) == 1):
                print(table_names[0]) 
            

        #print(table[0].get('summary'))

    def parse_average_age(self, html_code):
        self.generic_parse(html_code)
