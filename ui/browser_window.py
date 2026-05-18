from PySide6.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QPushButton,
    QTextEdit
)

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from rendering.text_renderer import render_url


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Abrir archivo .ui
        ui_file = QFile("ui/QtDesigner/MainUI.ui")

        if not ui_file.open(QFile.ReadOnly):
            print("No se pudo abrir el archivo UI")
            return

        # Crear loader
        loader = QUiLoader()

        # Cargar interfaz
        self.ui = loader.load(ui_file)

        # Cerrar archivo
        ui_file.close()

        # Establecer la UI cargada como contenido central
        self.setCentralWidget(self.ui)

        # Obtener widgets desde Qt Designer
        self.url_bar = self.findChild(QLineEdit, "urlEntering")
        self.go_button = self.findChild(QPushButton, "goButton")
        self.content_area = self.findChild(QTextEdit, "content_area")

        # Texto inicial
        self.content_area.setText("Bienvenido a mi navegador cursed")

        # Conectar botón
        self.go_button.clicked.connect(self.load_page)
        
        self.resize(1200,800)
        self.setWindowTitle("Navegador de estudios")

    def load_page(self):
        url = self.url_bar.text()

        print(f"Cargando: {url}")

        self.content_area.setPlainText(render_url(url))