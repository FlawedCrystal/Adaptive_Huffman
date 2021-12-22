class Node:
    def __init__(self, parent=None, value=None, count=0, left=None, right=None):
        self.value = value
        self.parent = parent
        self.count = count
        self.left_child = left
        self.right_child = right

    def check_esc(self):
        return self.value == 'esc'

    def check_root(self):
        return self.value == 'root'

    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count

    def __gt__(self, other):
        return self.count > other.count

    def __repr__(self):
        return f'{self.value}, {self.count}'


class AdaptiveHuffmanTree:
    def __init__(self):
        self.root = Node(value='root')
        self.root.right_child = Node(value='esc')
        self.root.right_child.parent = self.root
        self.root.left_child = Node()
        self.root.left_child.parent = self.root
        self.count_symbol = 0

    def add(self, value):
        current_node = self.root
        node = self.search(value)
        if node:
            node.count += 1
            node.parent.count += 1
            self.node_up(node)
        else:
            node = Node(value=value, count=1)
            while current_node.right_child:
                if node > current_node:
                    self.root.left_child = node
                    node.parent = self.root
                    self.root.count = node.count
                    break
                current_node = current_node.right_child
            else:
                self.add_new_node(node=node, current_node=current_node)
            self.count_symbol += 1

    def add_new_node(self, node, current_node):
        new_node = Node()
        temp = current_node.parent
        temp.right_child = new_node
        new_node.parent = temp
        new_node.right_child = current_node
        new_node.left_child = node
        new_node.count = node.count
        node.parent = new_node
        current_node.parent = new_node

    def search(self, value):
        current_node = self.root
        while current_node.right_child:
            if current_node.left_child.value == value:
                return current_node.left_child
            current_node = current_node.right_child
        return None

    def get_path(self, value):
        current_node = self.root
        path = ''
        while current_node.right_child:
            if current_node.left_child.value == value:
                return path + '1'
            path += '0'
            current_node = current_node.right_child
        return None

    def show(self):
        current_node = self.root
        path = ''
        while current_node.right_child:
            print(f'{current_node.left_child.value}, {current_node.count}', path + '1')
            current_node = current_node.right_child
            path += '0'
        print(current_node.value, current_node.count, path)

    def node_up(self, node):
        if node.parent.check_root():
            return
        node_grandparent = node.parent.parent
        node_parent = node.parent
        while node_grandparent:
            if node_parent > node_grandparent:
                temp = node_grandparent.left_child
                node_grandparent.left_child = node
                node.parent = node_grandparent
                node_grandparent.count = node.count
                node_parent.left_child = temp
                temp.parent = node_parent
                node_parent.count = temp.count
                if node.parent.parent:
                    node_grandparent = node.parent.parent
                    node_parent = node.parent
                else:
                    break
            else:
                break

    def search_by_path(self, path):
        tree_path = ''
        current_node = self.root
        while current_node.right_child:
            if tree_path == path[:-1]:
                return current_node.left_child.value
            current_node = current_node.right_child
            tree_path += '0'
        return -1
