# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sac_jfp_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_SAC_JFP(object):
    def setupUi(self, SAC_JFP):
        if not SAC_JFP.objectName():
            SAC_JFP.setObjectName(u"SAC_JFP")
        SAC_JFP.resize(310, 126)
        self.pbtn_read_json = QPushButton(SAC_JFP)
        self.pbtn_read_json.setObjectName(u"pbtn_read_json")
        self.pbtn_read_json.setGeometry(QRect(10, 10, 291, 31))
        self.pbtn_add_jfp = QPushButton(SAC_JFP)
        self.pbtn_add_jfp.setObjectName(u"pbtn_add_jfp")
        self.pbtn_add_jfp.setEnabled(False)
        self.pbtn_add_jfp.setGeometry(QRect(10, 40, 291, 31))
        self.pbtn_update_jfp = QPushButton(SAC_JFP)
        self.pbtn_update_jfp.setObjectName(u"pbtn_update_jfp")
        self.pbtn_update_jfp.setEnabled(False)
        self.pbtn_update_jfp.setGeometry(QRect(10, 70, 291, 31))
        self.lb_stu = QLabel(SAC_JFP)
        self.lb_stu.setObjectName(u"lb_stu")
        self.lb_stu.setGeometry(QRect(10, 100, 291, 21))

        self.retranslateUi(SAC_JFP)

        QMetaObject.connectSlotsByName(SAC_JFP)
    # setupUi

    def retranslateUi(self, SAC_JFP):
        SAC_JFP.setWindowTitle(QCoreApplication.translate("SAC_JFP", u"SAC-JFP\u52a0\u5bc6\u8c03\u8bd5\u5de5\u5177", None))
        self.pbtn_read_json.setText(QCoreApplication.translate("SAC_JFP", u"\u8bfb\u53d6JSON\u6587\u4ef6", None))
        self.pbtn_add_jfp.setText(QCoreApplication.translate("SAC_JFP", u"\u6dfb\u52a0SAC_JFP\u4fdd\u62a4", None))
        self.pbtn_update_jfp.setText(QCoreApplication.translate("SAC_JFP", u"\u66f4\u65b0SAC_JFP\u5bc6\u94a5", None))
        self.lb_stu.setText(QCoreApplication.translate("SAC_JFP", u"\u7b49\u5f85\u8bfb\u53d6\u6587\u4ef6", None))
    # retranslateUi

