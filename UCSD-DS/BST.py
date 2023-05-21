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
    
    def delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        elif key == node.key:
            if node.right is None and node.left is None:
                node = None
            elif node.right is not None and node.left is not None:
                temp = self._inordersuccessor(node)
                self.delete(node, temp.key)
                node.key = temp.key
                
            elif node.right is not None:
                node = node.right
            elif node.left is not None:
                node = node.left

        return node
    
    def _inordersuccessor(self, node):
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    
    def adjnodes(self, node, key):
        if node is None:
            print("Key not found.")
            return node
        
        if key == node.key:
            if node.left or node.right:
                if node.left:
                    print("Left: ", node.left.key)
                if node.right:
                    print("Right: ", node.right.key)
            else:
                print("Leaf Node")
        elif key < node.key:
            self.adjnodes(node.left, key)
        elif key > node.key:
            self.adjnodes(node.right, key)
    
    def search(self, node, key):
        if node is None:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self.search(node.left, key)
        elif key > node.key:
            return self.search(node.right, key)
    
    def _rsearch(self, node, key, keyset):
        if node is None:
            return node
        
        if key == node.key:
            keyset.add(node.key)
        elif key < node.key:
            keyset.add(node.key)
            self._rsearch(node.left, key, keyset)
        elif key > node.key:
            keyset.add(node.key)
            self._rsearch(node.right, key, keyset)
            
        return keyset
    
    def rangesearch(self, node, key1, key2):
        if self.search(node, key1) and self.search(node, key2):
            keyset = set()
            keyset = self._rsearch(node, key1, keyset)
            keyset = self._rsearch(node, key2, keyset)
            return keyset
        else:
            print("Key not found.")
    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(str(root.key), end=" -> ")
            self.inorder(root.right)

# bst = BST()
# root = bst.insert(None, 8)
# bst.insert(root, 3)
# bst.insert(root, 1)
# bst.insert(root, 6)
# bst.insert(root, 7)
# bst.insert(root, 10)
# bst.insert(root, 14)
# bst.insert(root, 4)
# bst.inorder(root)

# 1 -> 3 -> 4 -> 6 -> 7 -> 8 -> 10 -> 14 -> 

# bst.delete(root, 6)
# bst.delete(root, 13)
# bst.inorder(root)

# 1 -> 3 -> 4 -> 7 -> 8 -> 10 -> 14 -> 

# bst.adjnodes(root, 8)

# Left:  3
# Right:  10
    
# bst.adjnodes(root, 1)

# Leaf Node

# bst.adjnodes(root, 6)

# Key not found.

# bst.rangesearch(root, 10, 4)

# {3, 4, 7, 8, 10}

# bst.rangesearch(root, 10, 6)

# Key not found.
