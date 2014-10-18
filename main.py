import os,string
import urllib2
from bs4 import BeautifulSoup



content = urllib2.urlopen('http://finance.yahoo.com/q?uhb=uh3_finance_vert&fr=&type=2button&s=TSLA%2C').read();

f = open('test.html','w+');

f.write(content)
f.close()instal

soup = BeautifulSoup(content);


tag = soup.b;
type(tag)

print tag.name