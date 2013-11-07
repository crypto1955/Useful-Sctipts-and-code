import os
import urllib2, urllib
from urllib2 import urlopen, URLError, HTTPError


def dlfile(path):
    # Open the url
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    mydata=[('long','0'),('pagesize','100'),('page','0')]    #The first is the var name the second is the value
    mydata=urllib.urlencode(mydata)   #the url you want to POST to
    req=urllib2.Request(path, mydata,headers)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    
    try:
        page=urllib2.urlopen(req)
        print "downloading " 

        # Open our local file for writing
        with open(os.path.basename(path), "wb") as local_file:
            local_file.write(page.read())

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, path
    except URLError, e:
        print "URL Error:", e.reason, path


def main():
    # Iterate over image ranges
    #dlfile('http://vx.org.ua/dl/src/')
    f=open('/home/speaker/out','r')
    f1=open('/home/speaker/out1','r')
    f2=open('/home/speaker/out2','r')
    f3=open('/home/speaker/out3','r')
    f= f.read().split('\n')
    f1= f1.read().split('\n')
    f2= f2.read().split('\n')
    f3= f3.read().split('\n')
    for each in f:
        dlfile('http://vx.org.ua/dl/src/'+each)
    for each in f1:
        dlfile('http://vx.org.ua/dl/src/'+each)
    for each in f2:
        dlfile('http://vx.org.ua/dl/src/'+each)
    for each in f3:
        dlfile('http://vx.org.ua/dl/src/'+each)


if __name__ == '__main__':
    main()