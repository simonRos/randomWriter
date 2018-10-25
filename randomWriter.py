#!/usr/bin/python
from WordWeb import *
import random

#leave False unless debugging
debug = True

#text input is needed to seed/feed/lead the web
with open(input("Type file name: "),'r') as file:
    lines = file.readlines()

coupled_chars = { '(' : ')',
                  ')' : '(',
                  '<' : '>',
                  '>' : '<',
                  '“' : '”',
                  '”' : '“',
                  '"' : '"',
                  "'" : "'" }
ww = WordWeb()
for l in lines:
    #reset last for each line
    last = None
    #remove line endings and split on spaces
    words = l.replace('\n',' ').split(' ')
    for w in words:
        #ignore whitespace
        if w.replace(' ','') != '':
            if w[0] in coupled_chars.keys():
                if w[-1] != coupled_chars[w[0]] and last != None:
                    w = w + coupled_chars[w[0]]
                else:
                    w = w[1:]
            elif w[-1] in coupled_chars.keys():
                if w[0] != coupled_chars[w[-1]] and last != None:
                    w = coupled_chars[w[-1]] + w
                else:
                    w = w[:-1]
            if len(w) > 0:
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


for i in range(0,int(input("How many lines? "))):
    print(ww.getSentence())

