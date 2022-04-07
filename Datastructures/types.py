"""
This code contains the guideline and the definition
of node based data structures including Nodes, Graphs, LinkedList, Trees, Search trees and Heaps
"""


class GenericNode:
    def __init__(self, val, attachments):
        self.attachments = attachments


class BinaryNode(GenericNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.list = []
        if type(head) == list:
            self.add(head)
        else:
            self.head = head
        self.listl()

    def __repr__(self):
        the_ls = self.list
        if the_ls:
            ret_val = f"Node({the_ls[0]}, _)"
        else:
            ret_val = "Node()"

        for elem in the_ls[1:]:
            ret_val = ret_val.replace("_", f"Node({elem}, _)")

        return "LinkedList(" + ret_val.replace("_", "next=None") + ")"

    def __str__(self):
        this_l = self.list
        dis_r = ""

        for elem in this_l:
            dis_r += str(elem) + " => "
        else:
            if dis_r:
                dis_r += str(None)
            else:
                dis_r = None

        return dis_r

    def __add__(self, other):
        self.add(other.list)

        self.list += other.list

    def listl(self):
        node = self.head
        rls = []

        while node:
            rls.append(node.val)
            node = node.next

        self.list = rls

    def add(self, ls):
        head = self.head

        if head:
            while head.next:
                head = head.next

        def add_(ls):
            if not ls:
                return None
            return Node(ls[0], add_(ls[1:]))

        res = add_(ls)
        if not self.head:
            self.head = res
        else:
            head.next = res

        self.list += ls

        return self

    def copy(self):
        copy_result = LinkedList()
        copy_result.add(self.list)

        return copy_result.head


class GNode(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        """Assumes src and dest are nodes, weight a number"""
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')' \
               + self.dest.getName()


class Digraph(object):
    # nodes is a list of the nodes in the graph
    # edges is a dict mapping each node to a list of its children
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()

        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' \
                         + dest.getName() + '\n'
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()
    print(l2.add([5, 6, 4]))
    print(l1.add([2, 4, 3]))
    print(l1.__repr__())
