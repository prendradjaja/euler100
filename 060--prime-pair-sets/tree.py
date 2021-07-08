class TreeNode:
    def __init__(self, value, depth=1, parent=None):
        self.value = value
        self.children = []
        self.depth = depth
        self.parent = parent

    def add_child(self, child_value):
        node = TreeNode(child_value, self.depth + 1, self)
        self.children.append(node)
        return node

    def nodes(self):
        yield self
        for child in self.children:
            yield from child.nodes()

    def ancestors(self):
        yield self
        if self.parent:
            yield from self.parent.ancestors()
