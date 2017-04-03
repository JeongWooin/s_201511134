

import lxml.html
from lxml.cssselect import CSSSelector
import requests
import re
r = requests.get('http://python.org/')
html = r.text

p=re.compile('<h1>(.*?)</h1>')
litags = p.findall(html)
for tag in litags:
    print tag
    print "----------"