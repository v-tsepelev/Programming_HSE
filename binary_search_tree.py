
# coding: utf-8

# In[2]:


class Node:
    
    def __init__(self, key, parent = None, nil = None):
        self.key = key
        self.par = parent
        self.left = nil
        self.right = nil
        
class BTree:
    
    def __init__(self, root = None):
        self.root = root
    
    def add(self, key):
        if (self.root == None):
            self.root = Node(key)
        else:
            self._add(key, self.root)
            
    def _add(self, key, node):
        if (key < node.key):
            if (node.left != None):
                self._add(key, node.left)
            else:
                node.left = Node(key)
        else:
            if (node.right != None):
                self._add(key, node.right)
            else:
                node.right = Node(key)
    
    def find(self, key):
        if (self.root != None):
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, node):
        if (key == node.key):
            return node
        elif (node.left != None and key <= node.key):
            return self._find(key, node.left)
        elif (node.right != None and key > node.key):
            return self._find(key, node.right)
        else:
            return None
    
    def delete(self, key):
        pass
    
    def get_oredered_list(self):
        pass
    
    def get_min(self):
        pass
    
    def get_max(self):
        pass

    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print(str(node.key) + ' ')
            self._printTree(node.right)

tree = BTree()
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(9)
tree.printTree()
print(tree.find(4))
