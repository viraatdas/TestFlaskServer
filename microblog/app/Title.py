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
    print (query)
    description = []
    num_page = 3
    search_results = google.search("This is my query", num_page)
    for result in search_results:
        description.append (result.description)
    print (description)
    print (len(description))

    for url in search(query, stop=20):
        print(url)

