from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtWidgets import (QApplication, QDialog, QLabel,
                               QPushButton, QGraphicsScene, 
                               QWidget, QMainWindow, QColorDialog,
                               QTableWidgetItem)
from ui_mainwindow import Ui_Main_window
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Main_window()
        self.ui.setupUi(self)
        
        self.ui.fill_brightness_color_button.clicked.connect(self.color_selection)

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
