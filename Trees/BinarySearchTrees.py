class _Node:
    __slots__ = "_element", "_left", "_right"

    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, t_root, e):
        temp = None
        while t_root:
            temp = t_root
            if t_root._element == e:
                return
            elif t_root._element < e:
                t_root = t_root._right
            elif t_root._element > e:
                t_root = t_root._left
        new_node = _Node(e, None, None)
        if self._root == None:
            self._root = new_node
        else:
            if temp._element > e:
                temp._left = new_node
            elif temp._element < e:
                temp._right = new_node

    def inorder_traversal(self, t_root):
        if t_root:
            self.inorder_traversal(t_root._left)
            print(t_root._element, end=" ")
            self.inorder_traversal(t_root._right)


b = BinarySearchTree()
b.insert(b._root, 100)
b.insert(b._root, 30)
b.insert(b._root, 40)
b.insert(b._root, 50)
b.insert(b._root, 20)
b.insert(b._root, 60)
b.insert(b._root, 200)
b.insert(b._root, 300)
b.insert(b._root, 30)
b.insert(b._root, 40)
b.insert(b._root, 50)
b.insert(b._root, 400)
b.insert(b._root, 500)
b.insert(b._root, 600)

b.inorder_traversal(b._root)

