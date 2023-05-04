# task- given a BT and start node, find all node at distance K from start node
# approach- create parent array in first traversal, now perform BF from start node
# refer striver
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    
def nodes_at_distance_k(root,k,start_node):
    parent={}
    queue=[root]
    while(queue):
        node=queue.pop(0)
        if node.left:
            parent[node.left]=node
            queue.append(node.left)
        if node.right:
            parent[node.right]=node
            queue.append(node.right)
    
    # now we got parent map
    # perform bfs now from start_node

    queue=[start_node]
    dis=0
    ans=[]
    vis=[start_node]
    while(queue and dis<k):
        ans=[]
        size=len(queue)
        for i in range(size):
            node=queue.pop(0)

            if node.left and node.left not in vis:
                vis.append(node.left)
                ans.append(node.left.data)
                queue.append(node.left)
            if node.right and node.right not in vis:
                vis.append(node.right)
                ans.append(node.right.data)
                queue.append(node.right)
            if node in parent and parent[node] not in vis:
                vis.append(parent[node])
                ans.append(parent[node].data)
                queue.append(parent[node])
            
        dis+=1
        #print(ans)
        #print(dis)
    return ans
root=Node(3)
root.left=Node(5)
root.right=Node(1)
root.left.left=Node(6)
root.left.left.left=Node(9)
root.left.right=Node(2)
root.right.left=Node(0)
root.right.right=Node(8)

print(nodes_at_distance_k(root,2,root.left))
