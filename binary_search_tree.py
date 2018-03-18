class Node:

    def __init__(self, key, parent=None, nil=None):
        self.key = key
        self.par = parent
        self.left = nil
        self.right = nil


class BTree:

    def __init__(self, root=None):
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
                node.left.par = node
        else:
            if (node.right != None):
                self._add(key, node.right)
            else:
                node.right = Node(key)
                node.right.par = node

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
        def _delete(node, key):
            if node.key == key:
                if not (node.left and node.right):
                    return node.left or node.right, True
                else:
                    successor, parent = node.right, node
                    while successor.left:
                        successor, parent = successor.left, successor
                    successor.left = node.left
                    if parent != node:
                        parent.left = successor.right
                        successor.right = node.right
                    return successor, True
            elif key < node.key and node.left:
                node.left, deleted = _delete(node.left, key)
                return node, deleted
            elif key > node.key and node.right:
                node.right, deleted = _delete(node.right, key)
                return node, deleted
            return node, False
        if self.root is None:
            return False
        self.root, deleted = _delete(self.root, key)
        return deleted

    def get_oredered_list(self):
        aNode = self.root

        def makeList(self, aNode):
            if aNode is None:
                return []
            return makeList(self, aNode.left) + [aNode.key] + makeList(self, aNode.right)
        return list(dict.fromkeys(makeList(self, aNode)))

    def get_min(self):
        return self.get_oredered_list()[0]

    def get_max(self):
        return self.get_oredered_list()[len(self.get_oredered_list()) - 1]

    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print(str(node.key) + ' ')
            self._printTree(node.right)
