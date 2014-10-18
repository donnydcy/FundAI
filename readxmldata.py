#!/usr/bin/python

#read in xml files
from xml.dom.minidom import parse
import xml.dom.minidom,numpy

DOMTree = xml.dom.minidom.parse("Tesla_06292010_10092014/Tesla_close.xml")
collection = DOMTree.documentElement
period = collection.getElementsByTagName("dp:SUBTITLE");
n = period[0].childNodes[0].data
P = period[2].childNodes[0].data
print "Read in:\n\t\t\t%s" % n.strip()
print "\t\t\t%s\n" %P.strip()

ROWS = collection.getElementsByTagName("dp:ROW")
TIME = [];
PRICE = [];
for ROW in ROWS[::-1]:

	time =  ROW.childNodes[1].childNodes[1].childNodes[0].data
	price = ROW.childNodes[3].childNodes[1].childNodes[0].data
	time = int(time.strip())
	
	price = float(price.strip())
	TIME.append(time)
	PRICE.append(price)

dPRICE = numpy.diff(PRICE)
TIME.pop(0)
PRICE.pop(0)
MAP = {};

for i in range(0,len(TIME)):
	if (dPRICE[i]>=0):
		idi = "+"
	else:
		idi = "-"
	MAP[TIME[i]] = [PRICE[i],dPRICE[i],idi]
print "There are %d items" %len(MAP)
