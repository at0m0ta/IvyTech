'''
Liliana Varela
M13 CH19
'''

# 191 
 
# node structure
class Node:
 
    # creating a new node
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None
#print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
# Print nodes level
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1 :
        printGivenLevel(root.left , level-1)
        printGivenLevel(root.right , level-1)
#height of node
def height(node):
    if node is None:
        return 0
    else :
        #height of each subtree 
        lheight = height(node.left)
        rheight = height(node.right)
 
        #Use the larger one
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is:  ", printLevelOrder(root))
