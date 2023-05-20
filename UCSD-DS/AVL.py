class AVL:
    
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1
            
    def insert(self, node, key):
        if node is None:
            return self.Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
            
        left_height = self.getheight(node.left)
        right_height = self.getheight(node.right)
        
        node.height = 1 + max(left_height, right_height)
        
        balance = self.getbalance(node)
        
        # LL Rotation
        if balance > 1 and key < node.left.key:
            return self.rightrotate(node)
        # LR Rotation
        if balance > 1 and key > node.left.key:
            node.left = self.leftrotate(node.left)
            return self.rightrotate(node)
        # RR Rotation
        if balance < -1 and key > node.right.key:
            return self.leftrotate(node)
        # RL Rotation
        if balance < -1 and key < node.right.key:
            node.right = self.rightrotate(node.right)
            return self.leftrotate(node)
            
        return node
    
    def leftrotate(self, node):
        N = node
        NR = node.right
        
        N.right = NR.left
        NR.left = N
        
        NR.height = 1 + max(self.getheight(NR.left), self.getheight(NR.right))
        N.height = 1 + max(self.getheight(N.left), self.getheight(N.right))
        
        return NR
    
    def rightrotate(self, node):
        N = node
        NL = node.left
        
        N.left = NL.right
        NL.right = N
        
        NL.height = 1 + max(self.getheight(NL.left), self.getheight(NL.right))
        N.height = 1 + max(self.getheight(NL.left), self.getheight(NL.right))
        
        return NL
    
    def getheight(self, node):
        if node is None:
            return 0
        return node.height
    
    def getbalance(self, node):
        if node is None:
            return 0
        return self.getheight(node.left) - self.getheight(node.right)
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(str(root.key), end=" -> ")
            self.inorder(root.right)
