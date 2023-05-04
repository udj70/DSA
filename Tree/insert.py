import node #import node class
import create_tree #import Tree class

def insert(d1,d2,d3,d4,d5,d6,d7):
    t=create_tree.Tree()
    t.root=node.Node(d1)
    t.root.left=node.Node(d2)
    t.root.right=node.Node(d3)
    t.root.left.left=node.Node(d4)
    t.root.left.right=node.Node(d5)
    t.root.right.left=node.Node(d6)
    t.root.right.right=node.Node(d7)

    return t.root

