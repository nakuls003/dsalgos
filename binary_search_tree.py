class BinarySearchTree:

    class _Node:
        def __init__(self, data = None, left = None, right = None, parent = None):
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = self._Node(data)
        else:
            curr = self.root
            while curr:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = self._Node(data, parent=curr)
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = self._Node(data, parent=curr)
                        break
                    else:
                        curr = curr.right

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, curr):
        if curr is None:
            return None
        elif data == curr.data:
            return curr
        elif data < curr.data:
            return self._search(data, curr.left)
        else:
            return self._search(data, curr.right)

    def delete(self, data):
        node = self.search(data)
        if node:
            self._delete(node)

    def _delete(self, node):
        par = node.parent
        if not node.left and not node.right:
            if par:
                if par.left == node:
                    par.left = None
                elif par.right == node:
                    par.right = None
            else:
                self.root = None
        elif not node.left:
            if par:
                if par.left == node:
                    par.left = node.right
                elif par.right == node:
                    par.right = node.right
            else:
                self.root = node.right
            node.right.parent = par
        elif not node.right:
            if par:
                if par.left == node:
                    par.left = node.left
                elif par.right == node:
                    par.right = node.left
            else:
                self.root = node.left
            node.left.parent = par
        else:
            temp = self._find_min_right(node.right)
            node.data = temp.data
            self._delete(temp)

    def _find_min_right(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)
