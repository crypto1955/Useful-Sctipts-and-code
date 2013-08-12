import urllib
import urllib2
import random
from HTMLParser import HTMLParser

class MyParse(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=="img":
            #print(dict(attrs)["src"])
            var=dict(attrs)["src"]
            var1=var.split("/")
            print var1[-1]
            urllib.urlretrieve(dict(attrs)["src"],var1[-1])


response = urllib2.urlopen('http://www.allmusic.com/')
h=MyParse()
page=response.read()
h.feed(page)

