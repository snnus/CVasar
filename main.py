from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtWidgets import (QApplication, QDialog, QLabel,
                               QPushButton, QGraphicsScene, 
                               QWidget, QMainWindow, QColorDialog,
                               QTableWidgetItem, QFileDialog)
from ui_mainwindow import Ui_Main_window
import sys
from PIL import Image
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_window()
        self.ui.setupUi(self)
        
        self.original_image = None
        
        self.ui.fill_brightness_color_button.clicked.connect(self.color_selection)
        self.ui.upload_button.clicked.connect(self.upload_image)


    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Only Images (*.png *.jpg *.jpeg *.bmp)")
        
        scene = QGraphicsScene()
        pixmap = QPixmap(file_name)
        scene.addPixmap(pixmap)
        
        self.original_image = np.asarray(Image.open(file_name))

        self.ui.image_View.setScene(scene)
    
    
    def color_selection(self):
        button = self.sender()
        background_color = button.palette().color(QPalette.Button)
        
        dialog = QColorDialog()
        dialog.setCurrentColor(background_color.name())
        
        if dialog.exec_() == QDialog.Accepted:
            color = dialog.selectedColor()
            if color.isValid():
                button.setStyleSheet("QPushButton" + " {background-color : " + color.name() + ";}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
