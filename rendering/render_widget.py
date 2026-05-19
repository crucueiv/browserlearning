from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter

class RenderWidget(QWidget):
    def __init__(self, layout_root):
        super().__init__()
        self.layout_root = layout_root
    
    def paintEvent(self, event):
        painter = QPainter(self)
        self.draw_box(painter, self.layout_root)
    
    def draw_box(self, painter, box):
        if box.node.node_type == 'text':
            painter.drawText(box.x, box.y, box.node.text)
        
        for child in box.children:
            self.draw_box(painter, child)