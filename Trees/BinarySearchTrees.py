class _Node:
    __slots__ = "_element", "_left", "_right"

    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert_iter(self, t_root, e):
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

    def insert_recur(self, t_root, e):
        if t_root:
            if e < t_root._element:
                t_root._left = self.insert_recur(t_root._left, e)
            elif e > t_root._element:
                t_root._right = self.insert_recur(t_root._right, e)
        else:
            n = _Node(e, None, None)
            t_root = n
        return t_root

    def search_iter(self, key):
        t_root = self._root
        while t_root:
            if t_root._element == key:
                return True
            elif key < t_root._element:
                t_root = t_root._left
            elif key > t_root._element:
                t_root = t_root._right
        return False

    def inorder_traversal(self, t_root):
        if t_root:
            self.inorder_traversal(t_root._left)
            print(t_root._element, end=" ")
            self.inorder_traversal(t_root._right)


##Binary Search Tree using iterative approach
b = BinarySearchTree()
b.insert_iter(b._root, 100)
b.insert_iter(b._root, 30)
b.insert_iter(b._root, 40)
b.insert_iter(b._root, 50)
b.insert_iter(b._root, 20)
b.insert_iter(b._root, 60)
b.inorder_traversal(b._root)
print()

##Binary Search Tree using recursive approach
c = BinarySearchTree()
c._root = c.insert_recur(c._root, 100)
c.insert_recur(c._root, 2)
c.insert_recur(c._root, 3)
c.insert_recur(c._root, 4)
c.insert_recur(c._root, 5)
c.insert_recur(c._root, 6)
c.insert_recur(c._root, 7)
c.insert_recur(c._root, 8)
c.inorder_traversal(c._root)
print("Done")

##Searching Element in Tree
print(c.search_iter(2))
print(c.search_iter(3))
print(c.search_iter(1000))
