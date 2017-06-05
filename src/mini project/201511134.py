from lxml import etree
import urllib
import re

key=['C','Java','Python','R programming','JavaScript','Arduino','Assembly language','Scala',
       'HTML','Visual Basic','SQL','Labview','Ruby']
lang=[]
d = dict()

for i in range(0,35):
    uResponse = urllib.urlopen("https://www.coursera.org/courses?languages=en&query=programming+languages&start="+str(20*i))
    html=uResponse.read()
    htmlTree = etree.HTML(html)
    nodes = htmlTree.xpath('//*[@id="rendered-content"]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div[1]/div/div[2]/div[1]/h2')

    for node in nodes:
        char = node.text
        for i in range(0,13):
            p=re.compile(key[i])
            words = p.findall(char)
            for word in words:
                lang.append(word)
print lang

for i in lang:
    if i not in d:
        d[i] = 1
    else:
        d[i]=d[i]+1
print d


import matplotlib
import matplotlib.pyplot as plt
plt.bar(range(len(d)),d.values())
plt.xticks(range(len(d)),list(d.keys()))
plt.show()