class Node:
    def __init__(self, node_type, tag=None, text=None):
        self.node_type = node_type  # 'tag' o 'text'
        self.tag = tag
        self.text = text
        self.children = []
    def add_child(self, child):
        self.children.append(child)