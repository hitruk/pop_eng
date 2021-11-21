
from bs4 import BeautifulSoup
import requests
from page_obj.parent_page import HttpQuery
from page_obj.parent_page import ElementPage
import os



def http_query(url):
    """ requests a page """

    query = HttpQuery(url)
    html  = query.get_html_page()
    return html

def save_html(html):
    """ Save html file """

    with open('parent_page.html', 'w') as file:
        file.write(html)

def open_html():
    """ Open and return html file """

    with open('parent_page.html', 'r') as file:
        html = file.read()
    return html

def get_page_element(html):
    """ Get page elements and text  """

    elements = ElementPage(html)
    result = elements.parent_page_element()
    #print(result)
    return result

def save_data(result):
    """pass"""
    
    wow = []
    for rows in result:
        words = rows.split() 
        for row in words:
            wow.append(row)
    print(wow)

    
if __name__ == '__main__':

    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'  
    
    if os.path.exists('../pop_eng/parent_page.html'):
        pass
    else:
        html = http_query(url)
        save_html(html)

    html = open_html()
    result = get_page_element(html)
    save_data(result)

