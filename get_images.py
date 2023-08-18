from bs4 import BeautifulSoup
import requests

url = 'https://www.actmapi.act.gov.au/hap/1998'
ext = ''
# ext = 'pdf'

base_url = 'https://www.actmapi.act.gov.au'

# def listFD(url, ext=''):
#     page = requests.get(url).text
#     # print(page)
#     soup = BeautifulSoup(page, 'html.parser')
#     return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

# for file in listFD(url, ext):
#     print(file)

def listFD(url, ext=''):
    page = requests.get(url).text
    # print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [base_url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

outer_url = 'https://www.actmapi.act.gov.au/hap'

year_urls = [x for x in listFD(outer_url, '') if 'hap/19' in x]
import pdb; pdb.set_trace()
folder_per_year_url = [x for x in listFD(year_urls[0], '') if x[-4:] != 'hap/']
pdfs_per_folder_url = [x for x in listFD(folder_per_year_url[0], 'pdf')]



