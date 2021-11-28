
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
    result_p = elements.parent_page_element()
    return result_p

def modify_list(result_p):
    """ modify the resulting list """
    
    result = []
    for row in result_p:
        new_p = row.split()
        #print(new_p[0])
        #! переделать этот блок с регулярным выражением на более короткий !
        pattern = r"[^A-Za-z]"
        if re.search(pattern, new_p[0]):
            pass
        else:
            #print(new_p[0]) 
            result.append(new_p[0])
    
    data_word = []        
    for row in result:
        row_count = result.count(row)
        #print(row, row_count)
        data = (row, row_count)
        if data not in data_word:
            data_word.append(data)
        
    #print(data_word)
    finn_result = sorted(data_word, key=lambda x: x[1], reverse=True)
    print(finn_result)

def save_data(result_p):
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
    result_p = get_page_element(html)
    modify_list(result_p)
    #save_data(result)

