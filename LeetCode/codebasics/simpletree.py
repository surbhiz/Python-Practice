class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # child is instance of Node class and have parent property and want to set it as self
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces+"|--" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = Node("J")
    f = Node("F")
    f.add_child(Node("A"))
    f.add_child(Node("H"))

    k = Node("K")
    k.add_child(Node("Z"))

    root.add_child(f)
    root.add_child(k)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
