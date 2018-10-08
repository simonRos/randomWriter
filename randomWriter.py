#!/usr/bin/python
from WordWeb import *
import random

#leave False unless debugging
debug = False

#text input is needed to seed/feed/lead the web
with open(input("Type file name: "),'r') as file:
    #remove line endings and split on spaces
    data = file.read().replace('\n',' ').split(' ')

#create and fill in the WordWeb
ww = WordWeb()
last = None
for d in data:
    #ignore whitespace
    if d.replace(' ','') != '':
        ww.add(last,d)
        #Note that more logic could be added to create a more complex web
        #This web will have only one follower on the base node
        last = d

if debug == True:
    for k,v in ww.nodes.items():
        print(k)
        print(len(v.followers))
        for f in v.followers:
            print('\t'+f.word)

def traverse(node):
    """
    Randomly traverse the WordWeb
    """
    if node.ender == True or len(node.followers) <= 0:
        print(node.word)
        return
    else:
        print(node.word, end =" ")
        traverse(random.choice(node.followers))

for i in range(0,int(input("How many lines? "))):
    first = WordNode(None)
    while first.starter == False:
        first = ww.nodes[random.choice(list(ww.nodes))]
    traverse(first)
