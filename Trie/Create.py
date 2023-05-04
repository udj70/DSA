from string import ascii_lowercase
class trie:
    def __init__(self):
        self.child=[None]*26
        self.leaf=False
def insert(string):
        t=trie()
        n=len(string)
        for i in range(n):
            idx=ascii_lowercase.index(string[i])
            if t.child[idx]==None:
                t.child[idx]=trie()    
            t=t.child[idx]
            
        t.leaf=True
        
insert("hello")




