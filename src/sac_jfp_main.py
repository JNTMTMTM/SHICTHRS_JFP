
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStackedWidget, QWidget , QFileDialog)
from PySide6 import QtGui , QtWidgets

from ui.sac_jfp_ui import Ui_SAC_JFP

import sys
import os

class SAC_JFP(QMainWindow , Ui_SAC_JFP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(310, 126)
        self.show() 

if __name__ == "__main__":
    if __name__ == '__main__':
        app = QApplication(sys.argv)

        # 初始化GUI程序
        app.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd() , 'icon' , 'logo_32x32.ico')))
        app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

        # 实例化GUI程序
        main = SAC_JFP()

        # 主循环
        sys.exit(app.exec())