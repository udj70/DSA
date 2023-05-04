class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 


class BinarySearchTree:
    def __init__(self): 
        self.root = None
    #create of tree by passing node value  as parameter
    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def calculate_turns(root,data1,data2,t):

    #here if t==-1, i.e current node came from left of parent
    # if t==1, current node came from right of parent
    # if t==0, i.e. current node came from main root
    global turns
    # while returning if child return 0. i.e. data not found in subtree
    # if child return 1 i.e data found in right subtree
    # if child return -1 i.e. data found in left subtree
    if root == None:
        return 0
    if root.info==data1 or root.info==data2:
        return t    

    left=calculate_turns(root.left,data1,data2,-1)
    right=calculate_turns(root.right,data1,data2,1)

    #if left and right return -1 and 1 respectively, i.e current node is LCA , and it will add up 1 to turn, and return 0(i.e we dont require further comparison now)
    if left==-1 and right==1:
        turns+=1
        return 0 
    #if only left return -1 , i.e data present in left subtree, if t==1, i.e we are moving from upward from left to right(turn +1)    
    if left==-1 and t==1:
        turns+=1
        return t
    #if right return 1 and t=-1, i.e we are moving upwards from right to left(turn +1)    
    if right==1 and t==-1:
        turns+=1
        return t


def turns_between_two_nodes(root,data1,data2):
    global turns
    turns=0
    #pass 0 in t as current element is root, so it will not further contribute in turns
    return calculate_turns(root,data1,data2,0)

tree = BinarySearchTree()
t = int(input()) #number of elements in tree

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])    
root=tree.root    
#search turn between 4,10, ans==0(straight line)
turns_between_two_nodes(root,4,10)
#maintain global turns variable
global turns
print(turns)    