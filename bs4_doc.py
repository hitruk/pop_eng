
from bs4 import BeautifulSoup
import requests
from page_obj.parent_page import HttpQuery
from page_obj.parent_page import ElementPage
import os
import re 


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
    return result

def save_data(result):
    """pass"""
   
    # двумерный список [[],[]] делаем [] простым списком
    wow = []
    for rows in result:  # [[],[]]
        words = rows.split() # разделение на подстроки
        for row in words:
            # подумать нужны ли такие слова, It's, you’r
            # может быть добавить их в список?
            # найти словасостоящие только из латинских букв
            pattern = r"[^A-Za-z]"
            if re.search(pattern, row):
                pass
            else:
                wow.append(row.lower())  # []
    print(wow)
    
    bob = []  # список уникальных слов   
    fin_result = []
    for a in wow:
        if a not in bob:
            bob.append(a)
  
    for row in bob:
        row_count = wow.count(row) # подсчет кол-ва вхождений слов в списке
        fin_result.append([row, row_count])
    # сортировка двумерного списка, по [[a,b], [a1,b1]] b, по убыванию reverse = True
    finn_result = sorted(fin_result, key=lambda x: x[1], reverse=True)    
    print(finn_result)

    
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

