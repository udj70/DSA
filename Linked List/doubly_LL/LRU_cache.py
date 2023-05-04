# implement LRU cache by doubly LL
# refer striver video for explaination
class Node:
    def __init__(self,key,data):
        self.key=key
        self.data=data
        self.next=None
        self.prev=None
class LRUCache:
    def __init__(self,capacity):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.cap=capacity
        self.hash_map={}

        self.head.next=self.tail
        self.tail.prev=self.head
    
    def add_node(self,node):
        head=self.head

        node.next=head.next
        node.prev=head
        head.next=node
        node.next.prev=node
    
    def delete_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

        node.next=None
        node.prev=None

    
    def get(self,key):
        hash_map=self.hash_map
        if key in hash_map:
            node=hash_map[key]
            val=node.data
            self.delete_node(node)
            self.add_node(node)

            return val
        else:
            return -1
    def put(self,key,val):
        hash_map=self.hash_map
        if key in hash_map:
            node=hash_map[key]
            self.delete_node(node)
            node.data=val
            self.add_node(node)
        else:
            if len(hash_map)==self.cap:
                hash_map.pop(self.tail.prev.key)
                self.delete_node(self.tail.prev)
            new_node=Node(key,val)
            self.add_node(new_node)
            hash_map[key]=new_node
    def get_cache_status(self):
        head=self.head.next
        while(head!=self.tail):
            print([head.key,head.data],end=" ")
            head=head.next
        print()

        
l=LRUCache(3)

l.put(1,2)
l.put(2,4)
l.get_cache_status()
print(l.get(3))
l.put(3,6)
l.get_cache_status()
l.put(5,7)
print(l.get(3))
l.get_cache_status()

                