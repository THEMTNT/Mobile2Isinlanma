# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Marley(object):
    def setupUi(self, Marley):
        Marley.setObjectName("Marley")
        Marley.resize(365, 393)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Marley.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Marley)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelx = QtWidgets.QLabel(self.layoutWidget)
        self.labelx.setObjectName("labelx")
        self.gridLayout.addWidget(self.labelx, 0, 0, 1, 1)
        self.labely = QtWidgets.QLabel(self.layoutWidget)
        self.labely.setObjectName("labely")
        self.gridLayout.addWidget(self.labely, 0, 1, 1, 1)
        self.labelz = QtWidgets.QLabel(self.layoutWidget)
        self.labelz.setObjectName("labelz")
        self.gridLayout.addWidget(self.labelz, 0, 2, 1, 1)
        self.listWidgetkoordinat = QtWidgets.QListWidget(Marley)
        self.listWidgetkoordinat.setGeometry(QtCore.QRect(20, 160, 201, 211))
        self.listWidgetkoordinat.setObjectName("listWidgetkoordinat")
        self.layoutWidget1 = QtWidgets.QWidget(Marley)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 100, 311, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButtonxarttir = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonxarttir.setObjectName("pushButtonxarttir")
        self.gridLayout_4.addWidget(self.pushButtonxarttir, 0, 0, 1, 1)
        self.pushButtonyarttir = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonyarttir.setObjectName("pushButtonyarttir")
        self.gridLayout_4.addWidget(self.pushButtonyarttir, 0, 1, 1, 1)
        self.pushButtonzarttir = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonzarttir.setObjectName("pushButtonzarttir")
        self.gridLayout_4.addWidget(self.pushButtonzarttir, 0, 2, 1, 1)
        self.pushButtonxazalt = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonxazalt.setObjectName("pushButtonxazalt")
        self.gridLayout_4.addWidget(self.pushButtonxazalt, 1, 0, 1, 1)
        self.pushButtonyazalt = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonyazalt.setObjectName("pushButtonyazalt")
        self.gridLayout_4.addWidget(self.pushButtonyazalt, 1, 1, 1, 1)
        self.pushButtonzazalt = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonzazalt.setObjectName("pushButtonzazalt")
        self.gridLayout_4.addWidget(self.pushButtonzazalt, 1, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Marley)
        self.layoutWidget2.setGeometry(QtCore.QRect(21, 70, 311, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditx = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditx.setObjectName("lineEditx")
        self.gridLayout_2.addWidget(self.lineEditx, 0, 0, 1, 1)
        self.lineEdity = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdity.setObjectName("lineEdity")
        self.gridLayout_2.addWidget(self.lineEdity, 0, 1, 1, 1)
        self.lineEditz = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditz.setObjectName("lineEditz")
        self.gridLayout_2.addWidget(self.lineEditz, 0, 2, 1, 1)
        self.pushButtonisinlan = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonisinlan.setObjectName("pushButtonisinlan")
        self.gridLayout_2.addWidget(self.pushButtonisinlan, 0, 3, 1, 1)
        self.checkBoxxyzkitle = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBoxxyzkitle.setObjectName("checkBoxxyzkitle")
        self.gridLayout_2.addWidget(self.checkBoxxyzkitle, 0, 4, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(Marley)
        self.layoutWidget3.setGeometry(QtCore.QRect(21, 41, 311, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditzipla = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEditzipla.setObjectName("lineEditzipla")
        self.gridLayout_3.addWidget(self.lineEditzipla, 0, 0, 1, 1)
        self.pushButtonziplabaslat = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonziplabaslat.setObjectName("pushButtonziplabaslat")
        self.gridLayout_3.addWidget(self.pushButtonziplabaslat, 0, 1, 1, 1)
        self.pushButtonzipladurdur = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonzipladurdur.setObjectName("pushButtonzipladurdur")
        self.gridLayout_3.addWidget(self.pushButtonzipladurdur, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(Marley)
        self.widget.setGeometry(QtCore.QRect(230, 160, 101, 211))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButtonkoordinatekle = QtWidgets.QPushButton(self.widget)
        self.pushButtonkoordinatekle.setObjectName("pushButtonkoordinatekle")
        self.gridLayout_5.addWidget(self.pushButtonkoordinatekle, 0, 0, 1, 1)
        self.pushButtontextekle = QtWidgets.QPushButton(self.widget)
        self.pushButtontextekle.setObjectName("pushButtontextekle")
        self.gridLayout_5.addWidget(self.pushButtontextekle, 1, 0, 1, 1)
        self.pushButtonkoordinatsil = QtWidgets.QPushButton(self.widget)
        self.pushButtonkoordinatsil.setObjectName("pushButtonkoordinatsil")
        self.gridLayout_5.addWidget(self.pushButtonkoordinatsil, 2, 0, 1, 1)
        self.pushButtonsecilenegit = QtWidgets.QPushButton(self.widget)
        self.pushButtonsecilenegit.setObjectName("pushButtonsecilenegit")
        self.gridLayout_5.addWidget(self.pushButtonsecilenegit, 3, 0, 1, 1)
        self.pushButtonkoordinatsave = QtWidgets.QPushButton(self.widget)
        self.pushButtonkoordinatsave.setObjectName("pushButtonkoordinatsave")
        self.gridLayout_5.addWidget(self.pushButtonkoordinatsave, 4, 0, 1, 1)
        self.pushButtongitgel = QtWidgets.QPushButton(self.widget)
        self.pushButtongitgel.setObjectName("pushButtongitgel")
        self.gridLayout_5.addWidget(self.pushButtongitgel, 5, 0, 1, 1)
        self.lineEditgitgeltime = QtWidgets.QLineEdit(self.widget)
        self.lineEditgitgeltime.setObjectName("lineEditgitgeltime")
        self.gridLayout_5.addWidget(self.lineEditgitgeltime, 6, 0, 1, 1)
        self.checkBoxherzamanustte = QtWidgets.QCheckBox(self.widget)
        self.checkBoxherzamanustte.setObjectName("checkBoxherzamanustte")
        self.gridLayout_5.addWidget(self.checkBoxherzamanustte, 7, 0, 1, 1)

        self.retranslateUi(Marley)
        QtCore.QMetaObject.connectSlotsByName(Marley)

    def retranslateUi(self, Marley):
        _translate = QtCore.QCoreApplication.translate
        Marley.setWindowTitle(_translate("Marley", "Form"))
        self.labelx.setText(_translate("Marley", "TextLabelX"))
        self.labely.setText(_translate("Marley", "TextLabelY"))
        self.labelz.setText(_translate("Marley", "TextLabelZ"))
        self.pushButtonxarttir.setText(_translate("Marley", "XArttir"))
        self.pushButtonyarttir.setText(_translate("Marley", "YArttir"))
        self.pushButtonzarttir.setText(_translate("Marley", "ZArttir"))
        self.pushButtonxazalt.setText(_translate("Marley", "XAzalt"))
        self.pushButtonyazalt.setText(_translate("Marley", "YAzalt"))
        self.pushButtonzazalt.setText(_translate("Marley", "ZAzalt"))
        self.lineEditx.setText(_translate("Marley", "5000"))
        self.lineEdity.setText(_translate("Marley", "5000"))
        self.lineEditz.setText(_translate("Marley", "5000"))
        self.pushButtonisinlan.setText(_translate("Marley", "Işınlan"))
        self.checkBoxxyzkitle.setText(_translate("Marley", "Kitle"))
        self.lineEditzipla.setText(_translate("Marley", "5000"))
        self.pushButtonziplabaslat.setText(_translate("Marley", "Zipla"))
        self.pushButtonzipladurdur.setText(_translate("Marley", "Dur"))
        self.pushButtonkoordinatekle.setText(_translate("Marley", "KoordEkle"))
        self.pushButtontextekle.setText(_translate("Marley", "TextdenEkle"))
        self.pushButtonkoordinatsil.setText(_translate("Marley", "KoordSil"))
        self.pushButtonsecilenegit.setText(_translate("Marley", "SeçileneGit"))
        self.pushButtonkoordinatsave.setText(_translate("Marley", "Kaydet"))
        self.pushButtongitgel.setText(_translate("Marley", "GitGel"))
        self.lineEditgitgeltime.setText(_translate("Marley", "1"))
        self.checkBoxherzamanustte.setText(_translate("Marley", "Her Zaman Üstte"))