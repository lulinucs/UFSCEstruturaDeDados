class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._data)

class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self._root = node
        else:
            self._root = None


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self._root
        while(x):
            parent = x
            if value < x._data:
                x = x._left
            else:
                x = x._right
        if parent is None:
            self._root = Node(value)
        elif value < parent._data:
            parent._left = Node(value)
        else:
            parent._right = Node(value)

    def inorder(self, node=None):
        if node is None:
            node = self._root
        if node._left:
            self.inorder(node._left)
        print(node, end=' ')
        if node._right:
            self.inorder(node._right)

    def preorder(self, node=None):
        if node is None:
            node = self._root
        if node != None:
            print(node, end=' ')
            if node._left:
                self.preorder(node._left)
            if node._right:
                self.preorder(node._right)

    def postorder(self, node=None):
        if node is None:
            node = self._root
        if node != None:
            if node._left:
                self.postorder(node._left)
            if node._right:
                self.postorder(node._right)
            print(node, end=' ')

tree = BinarySearchTree()

qtd = int(input())

for i in range(qtd):
    elem = int(input())
    tree.insert(elem)

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()