
from bs4 import BeautifulSoup
import requests
from page_obj.parent_page import HttpQuery
from page_obj.parent_page import ElementPage
import os
import re 
from db_obj.db import DataBase
from config import config


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
    """ Get page elements and text """

    elements = ElementPage(html)
    result_p = elements.parent_page_element()
    return result_p

def get_id_attribute():
    """ Select id from table resource """

    conn = DataBase()
    id_res = conn.select_id_resource()
    return id_res

  
def modify_list(result_p, id_res):
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
            #print(data)
            data_word.append(data)
        
    #print(data_word)
    finn_result = sorted(data_word, key=lambda x: x[1], reverse=True)
    print(finn_result)

    
    data = []
    for row in finn_result:
        row_one = (id_res, row[0], row[1])
        print(row_one)
        data.append(row_one)
    return data


def save_data(data):
    """ Insert into word(id_resource, word, count_word) """

    conn = DataBase()
    conn.insert_world(data)    


if __name__ == '__main__':

    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/'  
    
    if os.path.exists('parent_page.html'):
        pass
    else:
        html = http_query(url)
        save_html(html)

    html = open_html()
    result_p = get_page_element(html)
    id_res = get_id_attribute()
    data = modify_list(result_p, id_res)
    save_data(data)
