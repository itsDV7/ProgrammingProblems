class BST:
    
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
    
    def insert(self, node, key):
        if node is None:
            return self.Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        
        return node
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(str(root.key), end=" -> ")
            self.inorder(root.right)
