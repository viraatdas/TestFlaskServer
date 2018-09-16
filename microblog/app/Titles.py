from googlesearch import search
import urllib2
from BeautifulSoup import BeautifulSoup
from nltk.tag import pos_tag
from routes import url

def parseNouns(title):
    tagged_sent = pos_tag(title.split())
    nouns = [word for word,pos in tagged_sent if pos == 'NNP']
    return nouns

def method ():
    website_url = url
    soup = BeautifulSoup(urllib2.urlopen(website_url))
    title = soup.title.string
    title = title[:title.find('|')]
    print (title)

    query =  parseNouns(title)
    for i, w in enumerate(query):
        query[i] =  w.replace('u',"")

    query = "".join(query)
    print (query)

    print ("article title is " + title)

    for url in search(query, stop=20):
        print(url)

