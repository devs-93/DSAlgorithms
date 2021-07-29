class _Node:
    __slots__ = "_element", "_left", "_right"

    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)

    def preorder_traversal(self, t_root):
        if t_root:
            print(t_root._element, end=" ")
            self.preorder_traversal(t_root._left)
            self.preorder_traversal(t_root._right)

    def postorder_traversal(self, t_root):
        if t_root:
            self.preorder_traversal(t_root._left)
            self.preorder_traversal(t_root._right)
            print(t_root._element, end=" ")

    def inorder_traversal(self, t_root):
        if t_root:
            self.preorder_traversal(t_root._left)
            print(t_root._element, end=" ")
            self.preorder_traversal(t_root._right)


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
x.make_tree(20, a, a)
y.make_tree(30, a, a)
z.make_tree(10, x, y)

print("preorder_traversal")
x.preorder_traversal(z._root)
print()
print("postorder_traversal")
x.postorder_traversal(z._root)
print()
print("inorder_traversal")
x.inorder_traversal(z._root)
