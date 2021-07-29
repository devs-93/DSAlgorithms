from Queues.QueueLinkedList import QueueLinkedList


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

    def level_order(self, t_root):
        Q = QueueLinkedList()
        t = t_root
        print(t._element, end=" ")
        Q.enqueue(t)
        while not Q.isempty():
            removed_address = Q.dequeue()
            if removed_address._left:
                print(removed_address._left._element, end=" ")
                Q.enqueue(removed_address._left)
            if removed_address._right:
                print(removed_address._right._element, end=" ")
                Q.enqueue(removed_address._right)

    def node_count(self, t_root):
        if t_root:
            x = self.node_count(t_root._left)
            y = self.node_count(t_root._right)
            return (x + y + 1)
        return 0


x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
x.make_tree(20, a, a)
y.make_tree(30, a, a)
z.make_tree(10, x, y)

print("preorder_traversal :")
x.preorder_traversal(z._root)
print()
print("postorder_traversal :")
x.postorder_traversal(z._root)
print()
print("inorder_traversal :")
x.inorder_traversal(z._root)
print()
print("level_order :")
x.level_order(z._root)

print()
print("node count in the tree :")
print(x.node_count(z._root))
