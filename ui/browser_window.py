from PySide6.QtWidgets import (
    QMainWindow,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget
)

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from rendering.layout import build_layout, layout
from rendering.render_widget import RenderWidget
from rendering.parser import parse_html
from networking.loader import load_url


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
        self.content_area = self.findChild(QVBoxLayout, "mainLayout")
        initialText = QTextEdit(self)
        initialText.setObjectName("InitialTextUI")
        self.content_area.addWidget(initialText)
        self.initialTextUI = self.findChild(QTextEdit, "InitialTextUI")

        self.initialTextUI.setText("Ingrese una URL y presione 'Go' para cargar la página.")
        self.initialTextUI.setReadOnly(True)

        # Conectar botón
        self.go_button.clicked.connect(self.load_page)
        
        self.resize(1200,800)
        self.setWindowTitle("Navegador de estudios")

    def load_page(self):
        url = self.url_bar.text()

        print(f"Cargando: {url}")
        
        html = load_url(url)
        parsed = parse_html(html)
        layout_root = build_layout(parsed)
        layout(layout_root)
        widget = RenderWidget(layout_root)
        widget.setObjectName("WebRenderWidget")
        
        if self.findChild(QTextEdit, "InitialTextUI"):  # Eliminar el texto inicial
            self.findChild(QTextEdit, "InitialTextUI").deleteLater()
        if self.findChild(QWidget, "WebRenderWidget"):
            self.findChild(QWidget, "WebRenderWidget").deleteLater()  # Verificar si el widget ya existe


        self.content_area.addWidget(widget)