from bs4 import BeautifulSoup
import requests

url = 'https://www.actmapi.act.gov.au/hap/1998'
ext = ''
# ext = 'pdf'

def listFD(url, ext=''):
    page = requests.get(url).text
    # print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for file in listFD(url, ext):
    print(file)
