class AVL_tree():

    class Node():
        def __init__(self, key=None, height=1):
            self.right = None
            self.left = None
            self.p = None
            self.key = key
            self.height = height

    def __init__(self):
        self.NIL = self.Node(key=None, height=0)
        self.root = self.NIL
        self.size = 0
        self.ordered = []
        pass

    def left_rotate(self, x):
        y = x.right
        # setting x right child as y left child
        x.right = y.left
        if(y.left != self.NIL):
            y.left.p = x

        # setting the parent of y as parent of x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        # setting the left child of y
        y.left = x
        x.p = y
        x.height = max(x.left.height, x.right.height)+1
        y.height = max(y.left.height, y.right.height)+1

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if(y.right != self.NIL):
            y.right.p = x

        y.p = x.p
        if(x.p == self.NIL):
            self.root = self.NIL
        elif(x.p.left == x):
            x.p.left = y

        else:
            x.p.right = y

        y.right = x
        x.p = y
        x.height = max(x.left.height, x.right.height)+1
        y.height = max(y.left.height, y.right.height)+1

    def insert(self, x):

        new_node = self.Node(key=x)
        new_node.left = self.NIL
        new_node.right = self.NIL
        root = self.root
        self.avl_insert(root, new_node)
        self.size += 1

    def avl_insert(self, root, x):

        if(self.root == self.NIL):
            self.root = x
            x.p = self.NIL
            return
        elif(x.key < root.key):
            if(root.left == self.NIL):
                root.left = x
                x.p = root
                root.height = max(root.left.height, root.right.height) + 1
            else:
                self.avl_insert(root.left, x)
        else:
            if(root.right == self.NIL):
                root.right = x
                x.p = root
                root.height = max(root.left.height, root.right.height) + 1
            else:
                self.avl_insert(root.right, x)

        if(root.left.height-root.right.height > 1):
            if(root.left.left.height < root.left.right.height):
                self.left_rotate(root.left)
            self.right_rotate(root)

        elif(root.right.height-root.left.height > 1):
            if(root.right.right.height < root.right.left.height):
                self.right_rotate(root.right)
            self.left_rotate(root)

    def inorder(self):
        x = self.root
        if(self.size == 0):
            print("the tree is Empty!")
            return

        self._inorder(x)
        for i in range(len(self.ordered)):
            print(self.ordered[i], end=' ')
        self.ordered = []

    def _inorder(self, x):
        if x != self.NIL and x.key != None:
            self._inorder(x.left)
            self.ordered.append(x.key)
            self._inorder(x.right)

    def remove(self, x):
        node = self.key_search(x)
        if node == None:
            print("there is no node with key {0}".format(x))
            return
        else:
            self._remove(node)

    def _remove(self, x):
        y = x.right

        if(x.left == self.NIL and x.right == self.NIL):
            if(x == self.root):
                self.root = self.NIL

            elif(x.p.left == x):
                x.p.left = self.NIL
            else:
                x.p.right = self.NIL
        if(x.left == self.NIL):
            if(x.p.left == x):
                x.p.left = x.right

            else:
                x.p.right = x.right

            x.right.p = x.p

        elif(x.right == self.NIL):
            if(x.p.left == x):
                x.p.left = x.left
            else:
                x.p.right = x.left

            x.left.p = x.p

        else:
            y = self._tree_minimum(x.right)
            z = y.right
            x.key = y.key
            if(y == x.right):
                if(z != self.NIL):
                    z.p = x
                x.right = z

            else:
                x = y.p
                if(z != self.NIL):

                    z.p = y.p
                if(y.p.left == y):
                    y.p.left = z
                else:
                    y.p.right = z

            self.delete_fixup(x)

    def delete_fixup(self, root):
        if root == self.NIL:
            return
        if(root.left.height-root.right.height > 1):
            if(root.left.left.height < root.left.right.height):
                self.left_rotate(root.left)
            self.right_rotate(root)

        elif(root.right.height-root.left.height > 1):
            if(root.right.right.height < root.right.left.height):
                self.right_rotate(root.right)
            self.left_rotate(root)
        root = root.p
        self.delete_fixup(root)

    def key_search(self, x):
        root = self.root
        if(root == self.NIL):
            print("the tree is empty!")
            return None
        else:
            if(x < root.key):

                return self._key_search(root.left, x)
            else:
                return self._key_search(root.right, x)

    def _key_search(self, root, x):
        if(x == root.key):
            return root
        elif(x < root.key):
            return self._key_search(root.left, x)
        elif(x > root.key):
            return self._key_search(root.right, x)
        else:
            return None

    def tree_minimum(self):
        x = self.root
        if(x == self.NIL):
            return
        else:
            if(x.left == self.NIL):
                print(x.key)

            else:
                y = self._tree_minimum(x.left)
                print(y.key)

    def _tree_minimum(self, x):
        y = self.root
        while(x != self.NIL and x.key != None):
            y = x
            x = x.left

        return y


avl = AVL_tree()

avl.insert(1)
avl.insert(2)

avl.inorder()
print()

avl.insert(5)
avl.insert(3)
avl.inorder()

print()

avl.insert(9)
avl.insert(4)
avl.inorder()
print()

avl.remove(5)
avl.inorder()
