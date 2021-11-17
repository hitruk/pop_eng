

from bs4 import BeautifulSoup
import requests
from page_obj.parent_page import HttpQuery

def http_query(url):
    ''' requests a page '''

    query = HttpQuery(url)
    html  = query.get_html_page()
    print(html)
        
    
if __name__ == '__main__':

    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'  
    http_query(url)
