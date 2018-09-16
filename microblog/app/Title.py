from nltk.tag import pos_tag
from googlesearch import search
#from google import google
from bs4 import BeautifulSoup
import requests

def function (website_url):
    soup = BeautifulSoup(requests.get(website_url).content, "html.parser")
    title = soup.title.string
    title = title[:title.find('|')]

    tagged_sent = pos_tag(title.split())
    nouns = [word for word, pos in tagged_sent if pos == 'NNP']
    query = nouns
    for i, w in enumerate(query):
        query[i] =  w.replace('u',"")

    query = "".join(query)

    site_prefix = ["site:foxnew.com ", "site: businessinsider.com ", "site: wsj.com ", "sites: nytimes.com ", "site: washingtonpost.com "]

    query_list = []
    i = 0
    while i<5:
        query_list.append(site_prefix[i] + query)
        i+=1
    print (query_list)

    i = 0
    url_list_fox=[]
    url_list_business = []
    url_list_wall = []
    url_list_new = []
    url_list_washington = []
    i = 0
    for url in search(query_list[0], stop=1):
        url_list_fox.append(url)

    for url in search(query_list[1], stop=1):
        url_list_business.append(url)

    for url in search(query_list[2], stop=1):
        url_list_wall.append(url)

    for url in search(query_list[3], stop=1):
        url_list_new.append(url)

    for url in search(query_list[4], stop=1):
        url_list_washington.append(url)

    url_list_fox = url_list_fox[0]
    for text in soup.p.stripped_strings:
        print(text)
    url_list_business = url_list_business[0]
    url_list_wall = url_list_wall[0]
    url_list_new = url_list_new[0]
    url_list_washington = url_list_washington[0]