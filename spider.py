#!/usr/bin/python

import requests

response = requests.get('Tesla_06292010_10092014/ProQuestDocuments-2014-10-11.html')

print response.text

