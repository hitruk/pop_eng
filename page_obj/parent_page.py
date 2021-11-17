
import requests

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
