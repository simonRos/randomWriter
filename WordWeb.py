#!/usr/bin/python

class WordNode:
    """
    Object representing a word and it's followers
    """
    def __init__(self, word):
        """
        Initialize with a string
        """
        self.word = word
        self.followers = {}
        #can be used to begin a sentence
        self.starter = False
        #can be used to end a sentence
        self.ender = False
        #empty/base nodes should be allowed
        if word != None:
            if word.istitle():
                self.starter = True
            #characters that denote the end of a sentence
            if word[-1] in ['!','?','.']:
                self.ender = True  
        else:
            self.ender = False
            
    def add(self, f):
        """
        Add a follower
        """
        if f not in self.followers.keys():
            self.followers[f] = 0
        self.followers[f] += 1

class WordWeb:
    """
    A collection of WordNodes
    """
    def __init__(self):
        """
        Initialize with a base node
        """
        self.nodes = {None: WordNode(None)}
        
    def add(self, front, follow):
        """
        Add a new wordNode
        """
        if follow not in self.nodes.keys():
            #create a new WordNode
            self.nodes[follow] = WordNode(follow)
        #add it to a previously exising WordNode
        self.nodes[front].add(self.nodes[follow])     

