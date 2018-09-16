from nltk.tag import pos_tag
from googlesearch import search
#from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

def function (website_url):
    soup = BeautifulSoup(requests.get(website_url).content, "html.parser")
    title = soup.title.string
    title = title[:title.find('|')]
    print (title)

    tagged_sent = pos_tag(title.split())
    nouns = [word for word, pos in tagged_sent if pos == 'NNP']
    query = nouns
    print (query)
    for i, w in enumerate(query):
        query[i] =  w.replace('u',"")

    query = "".join(query)

    print (query)

    print ("article title is " + title)

    for url in search(query, stop=20):
        soup
        print(url)
