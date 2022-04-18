class TreeNode:

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class Tree:

    def __init__(self, root):
        self.root = root

    def display(self):
        root = self.root

        def display_(root, level=0):
            indentation = '  ' * level
            if not root:
                print(' ' * 3 * level, 'None')
                return

            display_(root.right, level + 1)
            print(indentation, root.value)
            display_(root.left, level + 1)

        display_(root)

    def list(self):
        def list_(node):
            if not node:
                return [None]

            return list_(node.left) + [node.value] + list_(node.right)

        return [item for item in list_(self.root) if item]

    def __iter__(self):
        for item in self.list():
            yield item

    def __getitem__(self, item):
        return find_node(self.root, item)

    def toBST(self):
        self.root = convert_to_bst(self)


class BST(Tree):
    def __init__(self, root):
        # super().__init__(self, root)
        self.difference = None
        self.isbalanced = None
        self.root = convert_to_bst(Tree(root))
        self.__height, self.__h_left = None, None
        self.update()

    def update(self):
        self.__height, self.__h_left, self.__h_right = self.height()
        self.difference = self.__h_left - self.__h_right
        self.isbalanced = self.difference in range(-1, 1)

    def insert(self, value):

        def insert_(root, value, prevNode):
            if not root:
                if not prevNode:
                    self.root = TreeNode(value)
                    return
                if not prevNode.left:
                    prevNode.left = TreeNode(value)
                else:
                    prevNode.right = TreeNode(value)
                return

            if root.value > value:
                insert_(root.left, value, root)
            else:
                insert_(root.right, value, root)

        insert_(self.root, value, None)
        self.update()
        if not self.isbalanced:
            self.balance()

    def min_and_max(self):

        root = self.root

        def minimum(root):
            while root.left != None:
                root = root.left

            return root.value

        def maximum(root):
            if root.right != None:
                return maximum(root.right)
            else:
                return root.value

        return minimum(root), maximum(root)

    def height(self):
        root = self.root

        def h(root):
            if not root:
                return 0
            return 1 + max(h(root.left), h(root.right))

        return h(root), h(root.left), h(root.right)

    def balance(self):
        focus = self.root
        gotoLeft = self.difference > 0
        parent_list = []
        cond1 = focus.left and gotoLeft
        cond2 = focus.right and not gotoLeft
        print('cond1', cond1, 'cond2', cond2)
        while (focus.left and gotoLeft) or (focus.right and not gotoLeft):
            parent_list.append(focus)
            focus = (gotoLeft and focus.left) or (not gotoLeft and focus.right)

        while not self.isbalanced:
            print('runs')
            # rearranging focus
            focus = Tree(focus).toBST()
            # getting the parent
            parent = parent_list.pop()
            # knowing where to attach to the parent
            if parent.left:
                parent.right = focus
            else:
                parent.left = focus
            self.display()


def check_node(t, value):
    return value in t


def find_node(node, value):
    if not node:
        return None
    if node.value == value:
        return node

    return find_node(node.left, value) or find_node(node.right, value)


def find_node_bst(node, value):
    if not node:
        return None
    if node.value == value:
        return node

    if node.value > value:
        return find_node_bst(node.left, value)

    else:
        return find_node_bst(node.right, value)


def convert_to_bst(Tree):
    lt = Tree.list()
    lt.sort()

    def convert(lt):
        if not lt:
            return
        mid = len(lt) // 2
        root_value = lt[mid]  # not the index itself
        left_lt = lt[:mid]
        right_lt = lt[mid + 1:]
        root = TreeNode(root_value, convert(left_lt), convert(right_lt))

        return root

    return convert(lt)


def part():
    t_list = TreeNode(1, TreeNode(4, TreeNode(3)), TreeNode(2, TreeNode(8), TreeNode(7)))
    t = BST(t_list)

    t.display()

    things = [10, 2, 7, 100, 50, 70, 90]

    for thing in things:
        print('inserted', thing)
        t.insert(thing)
        t.toBST()

    t.display()


part()
