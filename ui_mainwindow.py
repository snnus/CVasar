# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowOPBfaQ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(940, 868)
        self.gridLayoutWidget_2 = QWidget(Dialog)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 901, 641))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_View = QGraphicsView(self.gridLayoutWidget_2)
        self.image_View.setObjectName(u"image_View")

        self.gridLayout_2.addWidget(self.image_View, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.red_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.red_checkbox.setObjectName(u"red_checkbox")
        self.red_checkbox.setEnabled(True)
        self.red_checkbox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.red_checkbox)

        self.green_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.green_checkbox.setObjectName(u"green_checkbox")
        self.green_checkbox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.green_checkbox)

        self.blue_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.blue_checkbox.setObjectName(u"blue_checkbox")
        self.blue_checkbox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.blue_checkbox)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.image_hist_label = QLabel(self.gridLayoutWidget_2)
        self.image_hist_label.setObjectName(u"image_hist_label")
        self.image_hist_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.image_hist_label, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.window_info_label = QLabel(self.gridLayoutWidget_2)
        self.window_info_label.setObjectName(u"window_info_label")

        self.gridLayout.addWidget(self.window_info_label, 1, 0, 1, 1)

        self.window_view = QGraphicsView(self.gridLayoutWidget_2)
        self.window_view.setObjectName(u"window_view")

        self.gridLayout.addWidget(self.window_view, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fill_brightness_min_spinbox = QSpinBox(self.gridLayoutWidget_2)
        self.fill_brightness_min_spinbox.setObjectName(u"fill_brightness_min_spinbox")
        self.fill_brightness_min_spinbox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.fill_brightness_min_spinbox)

        self.fill_brightness_max_spinbox = QSpinBox(self.gridLayoutWidget_2)
        self.fill_brightness_max_spinbox.setObjectName(u"fill_brightness_max_spinbox")
        self.fill_brightness_max_spinbox.setMinimum(0)
        self.fill_brightness_max_spinbox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.fill_brightness_max_spinbox)

        self.fill_brightness_colorbutton = QPushButton(self.gridLayoutWidget_2)
        self.fill_brightness_colorbutton.setObjectName(u"fill_brightness_colorbutton")

        self.horizontalLayout_3.addWidget(self.fill_brightness_colorbutton)

        self.fill_brightness_apply_button = QPushButton(self.gridLayoutWidget_2)
        self.fill_brightness_apply_button.setObjectName(u"fill_brightness_apply_button")

        self.horizontalLayout_3.addWidget(self.fill_brightness_apply_button)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)

        self.fill_brightness_label = QLabel(self.gridLayoutWidget_2)
        self.fill_brightness_label.setObjectName(u"fill_brightness_label")

        self.gridLayout_3.addWidget(self.fill_brightness_label, 7, 0, 1, 1)

        self.gamma_correction_label = QLabel(self.gridLayoutWidget_2)
        self.gamma_correction_label.setObjectName(u"gamma_correction_label")

        self.gridLayout_3.addWidget(self.gamma_correction_label, 2, 0, 1, 1)

        self.gamma_correction_slider = QSlider(self.gridLayoutWidget_2)
        self.gamma_correction_slider.setObjectName(u"gamma_correction_slider")
        self.gamma_correction_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.gamma_correction_slider, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.log_transform_button = QPushButton(self.gridLayoutWidget_2)
        self.log_transform_button.setObjectName(u"log_transform_button")

        self.gridLayout_3.addWidget(self.log_transform_button, 1, 0, 1, 1)

        self.binary_transform_slider = QSlider(self.gridLayoutWidget_2)
        self.binary_transform_slider.setObjectName(u"binary_transform_slider")
        self.binary_transform_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.binary_transform_slider, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 5, 1, 1, 1)

        self.image_hist_view = QGraphicsView(self.gridLayoutWidget_2)
        self.image_hist_view.setObjectName(u"image_hist_view")

        self.gridLayout_2.addWidget(self.image_hist_view, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.upload_button = QPushButton(self.gridLayoutWidget_2)
        self.upload_button.setObjectName(u"upload_button")

        self.horizontalLayout.addWidget(self.upload_button)

        self.reset_button = QPushButton(self.gridLayoutWidget_2)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout.addWidget(self.reset_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.red_checkbox.setText(QCoreApplication.translate("Dialog", u"Red channel", None))
        self.green_checkbox.setText(QCoreApplication.translate("Dialog", u"Green channel", None))
        self.blue_checkbox.setText(QCoreApplication.translate("Dialog", u"Blue channel", None))
        self.image_hist_label.setText(QCoreApplication.translate("Dialog", u"Brightness histogram", None))
        self.window_info_label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.fill_brightness_colorbutton.setText("")
        self.fill_brightness_apply_button.setText(QCoreApplication.translate("Dialog", u"Apply filling", None))
        self.fill_brightness_label.setText(QCoreApplication.translate("Dialog", u"Filling of brightness range", None))
        self.gamma_correction_label.setText(QCoreApplication.translate("Dialog", u"Gamma correction (gamma)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Binary transformation (threshold)", None))
        self.log_transform_button.setText(QCoreApplication.translate("Dialog", u"Log transformation", None))
        self.upload_button.setText(QCoreApplication.translate("Dialog", u"Upload an image", None))
        self.reset_button.setText(QCoreApplication.translate("Dialog", u"Reset changes", None))
    # retranslateUi

