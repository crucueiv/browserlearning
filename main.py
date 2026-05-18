
from PySide6.QtWidgets import QMainWindow,QApplication
import sys
from ui.browser_window import BrowserWindow

app = QApplication(sys.argv)

window = BrowserWindow()
window.show()

sys.exit(app.exec())