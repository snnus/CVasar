# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowmKSOPF.ui'
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

class Ui_Main_window(object):
    def setupUi(self, Main_window):
        if not Main_window.objectName():
            Main_window.setObjectName(u"Main_window")
        Main_window.resize(940, 868)
        Main_window.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayoutWidget_2 = QWidget(Main_window)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 901, 641))
        self.gridLayoutWidget_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_View = QGraphicsView(self.gridLayoutWidget_2)
        self.image_View.setObjectName(u"image_View")
        self.image_View.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.image_View, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.red_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.red_checkbox.setObjectName(u"red_checkbox")
        self.red_checkbox.setEnabled(True)
        self.red_checkbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.red_checkbox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.red_checkbox)

        self.green_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.green_checkbox.setObjectName(u"green_checkbox")
        self.green_checkbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.green_checkbox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.green_checkbox)

        self.blue_checkbox = QCheckBox(self.gridLayoutWidget_2)
        self.blue_checkbox.setObjectName(u"blue_checkbox")
        self.blue_checkbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.blue_checkbox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.blue_checkbox)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.image_hist_label = QLabel(self.gridLayoutWidget_2)
        self.image_hist_label.setObjectName(u"image_hist_label")
        self.image_hist_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
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
        self.window_info_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.window_info_label, 1, 0, 1, 1)

        self.window_view = QGraphicsView(self.gridLayoutWidget_2)
        self.window_view.setObjectName(u"window_view")
        self.window_view.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.window_view, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fill_brightness_min_spinbox = QSpinBox(self.gridLayoutWidget_2)
        self.fill_brightness_min_spinbox.setObjectName(u"fill_brightness_min_spinbox")
        self.fill_brightness_min_spinbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.fill_brightness_min_spinbox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.fill_brightness_min_spinbox)

        self.fill_brightness_max_spinbox = QSpinBox(self.gridLayoutWidget_2)
        self.fill_brightness_max_spinbox.setObjectName(u"fill_brightness_max_spinbox")
        self.fill_brightness_max_spinbox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.fill_brightness_max_spinbox.setMinimum(0)
        self.fill_brightness_max_spinbox.setMaximum(255)

        self.horizontalLayout_3.addWidget(self.fill_brightness_max_spinbox)

        self.fill_brightness_color_button = QPushButton(self.gridLayoutWidget_2)
        self.fill_brightness_color_button.setObjectName(u"fill_brightness_color_button")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(67, 67, 67, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(56, 56, 56, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(22, 22, 22, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(30, 30, 30, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush8)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush8)
#endif
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, brush6)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush6)
        brush9 = QBrush(QColor(22, 22, 22, 127))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush9)
#endif
        brush10 = QBrush(QColor(32, 32, 32, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(6, 6, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, brush10)
#endif
        self.fill_brightness_color_button.setPalette(palette)
        self.fill_brightness_color_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_3.addWidget(self.fill_brightness_color_button)

        self.fill_brightness_apply_button = QPushButton(self.gridLayoutWidget_2)
        self.fill_brightness_apply_button.setObjectName(u"fill_brightness_apply_button")
        self.fill_brightness_apply_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_3.addWidget(self.fill_brightness_apply_button)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)

        self.fill_brightness_label = QLabel(self.gridLayoutWidget_2)
        self.fill_brightness_label.setObjectName(u"fill_brightness_label")
        self.fill_brightness_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.fill_brightness_label, 7, 0, 1, 1)

        self.gamma_correction_label = QLabel(self.gridLayoutWidget_2)
        self.gamma_correction_label.setObjectName(u"gamma_correction_label")
        self.gamma_correction_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.gamma_correction_label, 2, 0, 1, 1)

        self.gamma_correction_slider = QSlider(self.gridLayoutWidget_2)
        self.gamma_correction_slider.setObjectName(u"gamma_correction_slider")
        self.gamma_correction_slider.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.gamma_correction_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.gamma_correction_slider, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.log_transform_button = QPushButton(self.gridLayoutWidget_2)
        self.log_transform_button.setObjectName(u"log_transform_button")
        self.log_transform_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_3.addWidget(self.log_transform_button, 1, 0, 1, 1)

        self.binary_transform_slider = QSlider(self.gridLayoutWidget_2)
        self.binary_transform_slider.setObjectName(u"binary_transform_slider")
        self.binary_transform_slider.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.binary_transform_slider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.binary_transform_slider, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 5, 1, 1, 1)

        self.image_hist_view = QGraphicsView(self.gridLayoutWidget_2)
        self.image_hist_view.setObjectName(u"image_hist_view")
        self.image_hist_view.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.image_hist_view, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.upload_button = QPushButton(self.gridLayoutWidget_2)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.upload_button)

        self.reset_button = QPushButton(self.gridLayoutWidget_2)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout.addWidget(self.reset_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Main_window)

        QMetaObject.connectSlotsByName(Main_window)
    # setupUi

    def retranslateUi(self, Main_window):
        Main_window.setWindowTitle(QCoreApplication.translate("Main_window", u"CVasar App", None))
        self.red_checkbox.setText(QCoreApplication.translate("Main_window", u"Red channel", None))
        self.green_checkbox.setText(QCoreApplication.translate("Main_window", u"Green channel", None))
        self.blue_checkbox.setText(QCoreApplication.translate("Main_window", u"Blue channel", None))
        self.image_hist_label.setText(QCoreApplication.translate("Main_window", u"Brightness histogram", None))
        self.window_info_label.setText(QCoreApplication.translate("Main_window", u"TextLabel", None))
        self.fill_brightness_color_button.setText("")
        self.fill_brightness_apply_button.setText(QCoreApplication.translate("Main_window", u"Apply filling", None))
        self.fill_brightness_label.setText(QCoreApplication.translate("Main_window", u"Filling of brightness range", None))
        self.gamma_correction_label.setText(QCoreApplication.translate("Main_window", u"Gamma correction (gamma)", None))
        self.label_4.setText(QCoreApplication.translate("Main_window", u"Binary transformation (threshold)", None))
        self.log_transform_button.setText(QCoreApplication.translate("Main_window", u"Log transformation", None))
        self.upload_button.setText(QCoreApplication.translate("Main_window", u"Upload an image", None))
        self.reset_button.setText(QCoreApplication.translate("Main_window", u"Reset changes", None))
    # retranslateUi

