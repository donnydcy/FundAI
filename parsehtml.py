#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom,re,StringIO

from bs4 import BeautifulSoup


soup = BeautifulSoup(open("Tesla_06292010_10092014/100.html"))

tag = soup.body

a = tag.find_all(href=re.compile("rft.date"))[0]




