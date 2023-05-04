# here we will implement Trie with functionality count word which start with certain prefix, 
# remove word, count words equal to

#refer strivers lecture
class Node:
    def __init__(self):
        self.children=[None]*26
        self.count_prefix=0
        self.ends_with=0
class Trie:
    def __init__(self,Node):
        self.root=Node
    def insert(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is None:
                root.children[ord(ch)-ord('a')]=Node()
            root=root.children[ord(ch)-ord('a')]
            root.count_prefix+=1
        root.ends_with+=1
    
    def count_starts_with(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is not None:
                root=root.children[ord(ch)-ord('a')]
            else:
                return 0
        return root.count_prefix
    def erase(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is not None:
                root=root.children[ord(ch)-ord('a')]
                root.count_prefix-=1
            else:
                return
        root.ends_with-=1
    def count_equal_to(self,word):
        root=self.root
        for ch in word:
            if root.children[ord(ch)-ord('a')] is not None:
                root=root.children[ord(ch)-ord('a')]
            else:
                return 0
        return root.ends_with
t=Trie(Node())
t.insert('apple')
t.insert('apple')
t.insert('apps')
t.insert('app')
t.insert('apples')
print(t.count_equal_to('apple'))
print(t.count_starts_with('app'))
t.erase('ap')
#print(t.count_starts_with('app'))
print(t.count_equal_to('app'))