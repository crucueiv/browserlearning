class LayoutBox:
    def __init__(self, node):
        self.node = node
        self.children = []
        
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        
def build_layout(dom_node):
    box = LayoutBox(dom_node)
    
    for child in dom_node.children:
        if child.node_type == 'element':
            box.children.append(build_layout(child))
        elif child.node_type == 'text':
            box.children.append(LayoutBox(child))
    return box

def layout(box, x=10, y=10):
    box.x = x
    box.y = y
    
    current_y = y
    for child in box.children:
        
        child.x = x
        child.y = current_y
        
        if child.node.node_type == 'text':
            current_y += 20
        else:
            layout(child, x, current_y)
            current_y += 20