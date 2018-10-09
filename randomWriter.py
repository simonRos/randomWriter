#!/usr/bin/python
from WordWeb import *
import random

#leave False unless debugging
debug = True

#text input is needed to seed/feed/lead the web
with open(input("Type file name: "),'r') as file:
    lines = file.readlines()

ww = WordWeb()
for l in lines:
    #reset last for each line
    last = None
    #remove line endings and split on spaces
    words = l.replace('\n',' ').split(' ')
    for w in words:
        #ignore whitespace
        if w.replace(' ','') != '':
            ww.add(last, w)
            last = w

if debug == True:
    with open("debug.txt", 'w') as debugFile:
        for k,v in ww.nodes.items():
            debugFile.write(str(k))
            debugFile.write('\t'+str(len(v.followers))+'\n')
            for f in v.followers:
                debugFile.write('\t'+f.word)
                debugFile.write('\n\t\t'+str(v.followers[f])+'\n')

def traverse(node):
    """
    Randomly traverse the WordWeb
    """
    if node.ender == True or len(node.followers) <= 0:
        print(node.word)
        return
    else:
        print(node.word, end =" ")
        traverse(random.choice(list(node.followers)))

for i in range(0,int(input("How many lines? "))):
    first = WordNode(None)
    while first.starter == False:
        first = ww.nodes[random.choice(list(ww.nodes))]
    traverse(first)
