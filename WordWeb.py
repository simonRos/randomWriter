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
        #used to identify and track quotations
        self.open_quote = False
        self.close_quote = False
        #empty/base nodes should be allowed
        if word != None:
            #characters that denote the end of a sentence
            if word[-1] in ['!','?','.']:
                self.ender = True
            #quote detection
            if word[0] in ['"']:
                self.open_quote = True
            #logic phrased this way to handle cases where " comes before punctuation
            elif '"' in word:
                self.close_quote = True
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
        if front == None:
            self.nodes[follow].starter = True

    def getSentence(self, start_node = None):
        """
        Holds metadata for recursive method 
        """
        import random
        #metadata
        sentence = []
        in_quote = False
        #recursive method
        def _getSentence(node):
            """
            Recursively traverses web to produce a sentence
            """
            if node.ender == True or len(node.followers) <= 0:
                sentence.append(node.word)
                return
            elif node.word != None:
                sentence.append(node.word)
            return _getSentence(random.choice(list(node.followers)))

        if start_node == None:
            start_node = self.nodes[None]
        elif isinstance(start_node, WordNode) == False:
            raise TypeError('Argument to .getSentence must be of type WordNode')
        _getSentence(start_node)
        return (' '.join(sentence))
        
        

