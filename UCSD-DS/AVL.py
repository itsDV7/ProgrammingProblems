class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.height = 1

class AVL:
            
    def insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node 
        
        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))
        
        balance = self.getbalance(node)
        
        # LL Rotation
        if balance > 1 and key < node.left.key:
            return self.rightrotate(node)
        
        # RR Rotation
        if balance < -1 and key > node.right.key:
            return self.leftrotate(node)
        
        # LR Rotation
        if balance > 1 and key > node.left.key:
            node.left = self.leftrotate(node.left)
            return self.rightrotate(node)
        
        # RL Rotation
        if balance < -1 and key < node.right.key:
            node.right = self.rightrotate(node.right)
            return self.leftrotate(node)
            
        return node
    
    def delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        elif key == node.key:
            if node.right is not None and node.left is not None:
                iosuccessor = self._inordersuccessor(node)
                node = self.delete(node, iosuccessor.key)
                node.key = iosuccessor.key
            elif node.right is None and node.left is None:
                node = None
                return node
            elif node.right is None:
                node = node.left
                return node
            elif node.left is None:
                node = node.right
                return node
        
        if node is None:
            return node
        
        node.height = 1 + max(self.getheight(node.left), self.getheight(node.right))
        
        balance = self.getbalance(node)
        
        # LL Rotation
        if balance > 1 and key < node.left.key:
            return self.rightrotate(node)
        
        # RR Rotation
        if balance < -1 and key > node.right.key:
            return self.leftrotate(node)
        
        # LR Rotation
        if balance > 1 and key > node.left.key:
            node.left = self.leftrotate(node.left)
            return self.rightrotate(node)
        
        # RL Rotation
        if balance < -1 and key < node.right.key:
            node.right = self.rightrotate(node.right)
            return self.leftrotate(node)
            
        return node
            
    
    def search(self, node, key):
        if node is not None:
            if key == node.key:
                return True
            elif key < node.key:
                self.search(node.left, key)
            elif key > node.key:
                self.search(node.right, key)
        
        return False
        
    
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
        N.height = 1 + max(self.getheight(N.left), self.getheight(N.right))
        
        return NL
    
    def getheight(self, node):
        if node is None:
            return 0
        
        return node.height
    
    def getbalance(self, node):
        if node is None:
            return 0
        
        return self.getheight(node.left) - self.getheight(node.right)
    
    def _inordersuccessor(self, node):
        if node is None:
            return node
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
#             print(f"{root.left.key if root.left is not None else None} {root.key} {root.right.key if root.right is not None else None}\n")
            print(str(root.key), end=" -> ")
#             print("{0} ".format(root.key), end="")
#             self.inorder(root.left)
            self.inorder(root.right)
            
avl = AVL()
root = avl.insert(None, 10)
root = avl.insert(root, 20)
root = avl.insert(root, 30)
root = avl.insert(root, 40)
root = avl.insert(root, 50)
root = avl.insert(root, 25)
avl.inorder(root)

10 -> 20 -> 25 -> 30 -> 40 -> 50 -> 
