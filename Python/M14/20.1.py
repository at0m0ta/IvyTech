'''
Liliana Varela-Rodriguez
M20 20.1 
'''

# 20.1 Displaying AVL tree graphically

from BinaryTree import BinaryTree

from BinaryTree import TreeNode

class AVLTree(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)

    def createNewNode(self, e):
        return AVLTreeNode(e)

    def insert(self, o):
        successful = BinaryTree.insert(self, o)
        if not successful:
            return False
        else:
            self.balancePath(o)

        return True

    def updateHeight(self, node):
        if node.left == None and node.right == None:
            node.height = 0
        elif node.left == None:
            node.height = 1 + (node.right).height
        elif node.right == None:
            node.height = 1 + (node.left).height
        else:
            node.height = 1 + max((node.right).height, (node.left).height)

    def balancePath(self, o):
        path = BinaryTree.path(self, o);

        for i in range(len(path) -1, -1, -1):
            A = path[i]
            self.updateHeight(A)
            parentOfA = None if (A == self.root) else path[i - 1]

            if self.balanceFactor(A) == -2:
                if self.balanceFactor(A.left) <= 0:
                    self.balanceLL(A, parentOfA)
                else:
                    self.balanceLR(A, parentOfA)
            elif self.balanceFactor(A) == +2:
                if self.balanceFactor(A, parentOfA) >= 0:
                    self.balanceRR(A, parentOfA)
                else:
                    self.balanceRL(A, parentOfA)
    def balanceFactor(self, node):
        if node.right == None:
            return -node.height
        elif node.left ==None:
            return +node.height
        else:
            return (node.right).height - (node.left).height
    def balanceLL(self, A, parentOfA):
        B = A.left

        if A == self.root:
            self.root = B
        else:
            if parentOfA.left == A:
                parentOfA.left = B
            else:
                parentOfA.right = B
                
        A.left = B.right
        B.right = A
        self.updateHeight(A)
        self.updateHeight(B)

    def balanceLR(self, A, parentOfA):
        B = A.left
        C = B.right

        if A == self.root:
            self.root = C
        else:
            if parentOfA.left == A:
                parentOfA.left = C
            else:
                parentOfA.right = C
        A.left = C.right
        B.right = C.left
        C.left = B
        C.right = A

        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)

    def balanceRR(self, A, parentOfA):
        B = A.right

        if A == self.root:
            self.root = B
        else:
            if parentOfA.left == A:
                parentOfA.left = B
            else:
                parentOfA.right = B

        A.right = B.left
        B.left = A
        self.updateHeight(A)
        self.updateHeight(B)

    def balanceRL(self,A,parentOfA):
        B = A.right
        C = B.left

        if A == self.root:
            self.root = C
        else:
            if parentOfA.left == A:
                parentOfA.left = C
            else:
                parentOfA.right = C
        A.right = C.left
        B.left = C.right
        C.left = A
        C.right = B

        self.updateHeight(A)
        self.updateHeight(B)
        self.updateHeight(C)
        
    def delete(self, element):
        if self.root == None:
            return False

        parent = None
        current = self.root
        while current != None:
            if element < current.element:
                parent = current
                current = current.left
            elif element > current.element:
                parent = current
                current = current.right
            else:
                break
        if current == None:
            return False

        if current.left == None:

            if parent == None:
                root = current.right
                else:
                    if element < parent.element:
                        parent.left = current.right
                else:
                    parent.right = current.right

                    self.balancePath(parent.element)
                else:
                    parentOfRightMost = current
                    rightMost = current.left

                    while rightMost.right != None:
                        parentOfRightMost = rightMost
                        rightMost = rightMost.right

                    current.element = rightmost.element

                    if parentOfRightMost.right == rightMost:
                        parentOfRightMost.right = rightMost.left
                    else:
                        parentOfRightMost.left = rightMost.left

                    self.balancePath(parentOfRightMost.element)
                self.size -=1
                return True
        class AVLTreeNode(TreeNode):
            def__init__(self, e):
                self.height = 0
                TreeNode.__init__(self, e)
                
            
        





















            
            
