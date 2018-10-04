#!/usr/bin/python
import random

debug = False

class WordNode:
    def __init__(self,word):
        self.word = word
        self.followers = []
        self.starter = False
        self.ender = False
        if word != None:
            if word[-1] in ['!','?','.']:
                self.ender = True 
            if word.istitle():
                self.starter = True 
        else:
            self.ender = False
            
    def add(self, f):
        self.followers.append(f)

class WordWeb:
    def __init__(self):
        self.nodes = {None: WordNode(None)}
        
    def add(self, front, follow):
        if follow not in self.nodes.keys():
            self.nodes[follow] = WordNode(follow)
            self.nodes[front].add(self.nodes[follow])     
        else:
            self.nodes[front].add(self.nodes[follow])
        
with open(input("Type file name: "),'r') as file:
    data = file.read().replace('\n',' ').split(' ')

ww = WordWeb()
last = None

for d in data:
    if d.replace(' ','') != '':
        ww.add(last,d)
        last = d

if debug == True:
    for k,v in ww.nodes.items():
        print(k)
        print(len(v.followers))
        for f in v.followers:
            print('\t'+f.word)

def traverse(node):
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
