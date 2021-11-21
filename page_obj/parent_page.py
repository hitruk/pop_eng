
import requests
from bs4 import BeautifulSoup

class HttpQuery:

    def __init__(self, url):
        self.url = url
        self.r = requests.get(self.url)

    def get_html_page(self):
        
        if self.r.status_code == 200:
            print('status code :', self.r.status_code)
            return self.r.text
        else:
            print(r.status_code)

class ElementPage:

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, 'lxml')

    def parent_page_element(self):

        abc = self.soup.find('div', class_='body').find_all('div', class_='section')
        res_text = []
        for row in abc:
            if row != '':
                div_p = row.find_all('p')
                for row in div_p:
                    try:
                        text_p = row.text
                    except:
                        text_p != ''
                    if text_p != '':
                        res_text.append(text_p)
        return res_text
