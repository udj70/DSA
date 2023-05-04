# task- given set of words, find longest word with all its prefixs present in word List
#approach 1 - make hash map, and check
# approach 2- make Trie, insert all words in it, then check for each word if its all prefic present, fetch longest such word

from textblob import WordList


class Node:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
class Trie:
    def __init__(self,Node):
        self.root=Node
        self.ans=''
    def insert(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is None:
                root.children[ord(ch)-ord('a')]=Node()
            root=root.children[ord(ch)-ord('a')]
        root.isEnd=True
    def longest_word_with_all_prefix(self,wordList):
        
        for word in wordList:
            flag=True
            root=self.root
            for ch in word:
                if root.children[ord(ch)-ord('a')] is not None:
                    root=root.children[ord(ch)-ord('a')]
                    if not root.isEnd:
                        flag=False
            if flag:
                if len(word)>len(self.ans):
                    self.ans=word
            

t=Trie(Node())
wordList=['n','ni','nin','ninj','ninja','ninga']
for word in wordList:
    t.insert(word)
t.longest_word_with_all_prefix(wordList)
print(t.ans)
            