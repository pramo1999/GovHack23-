# import os, sys, path
# from bs4 import BeautifulSoup
# import requests
# import urllib.request
# # urllib.request.urlretrieve(url, "filename.pdf")

# url = 'https://www.actmapi.act.gov.au/hap/1998'
# ext = ''
# # ext = 'pdf'

# base_url = 'https://www.actmapi.act.gov.au'

# # def listFD(url, ext=''):
# #     page = requests.get(url).text
# #     # print(page)
# #     soup = BeautifulSoup(page, 'html.parser')
# #     return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

# # for file in listFD(url, ext):
# #     print(file)

# def listFD(url, ext=''):
#     page = requests.get(url).text
#     # print(page)
#     soup = BeautifulSoup(page, 'html.parser')
#     return [base_url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

# outer_url = 'https://www.actmapi.act.gov.au/hap'

# year_urls = [x for x in listFD(outer_url, '') if 'hap/19' in x]
# # import pdb; pdb.set_trace()
# # folder_per_year_url = [x for x in listFD(year_urls[0], '') if x[-4:] != 'hap/']
# # pdfs_per_folder_url = [x for x in listFD(folder_per_year_url[0], 'pdf')]

# output_path = './Images'
# os.makedirs(outer_url, exist_ok=True)

# years = [x.split('/')[-2] for x in year_urls]

# for i, year in enumerate(years):
#     print(year)
#     year_path = os.path.join(output_path, year)
#     os.makedirs()
#     year_url = year_urls[i]
#     folder_urls = [x for x in listFD(year_url, '') if x[-4:] != 'hap/']
#     folders = [x.split('/')[-2] for x in folder_urls]

#     for i, folder in enumerate(folders):
#         print(folder)
#         folder_url = folder_urls[i]
#         pdf_urls = [x for x in listFD(folder_url, 'pdf')]

#         print(pdf_urls)


# https://stackoverflow.com/questions/23446635/how-to-download-http-directory-with-all-files-and-sub-directories-as-they-appear

# wget -r -np -nH -R index.html https://www.actmapi.act.gov.au/hap/

