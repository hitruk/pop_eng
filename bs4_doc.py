

from bs4 import BeautifulSoup
import requests
from page_obj.parent_page import HttpQuery
from page_obj.parent_page import ElementPage

def http_query(url):
    """ requests a page """

    query = HttpQuery(url)
    html  = query.get_html_page()
    return html

def get_page_element(html):
    """ Get page elements and text  """

    elements = ElementPage(html)
    result = elements.parent_page_element()
    print(result)
    return result

def save_data(result):
    pass

    
if __name__ == '__main__':

    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'  
    html = http_query(url)
    result = get_page_element(html)
    # save_data(result)

