# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialogdetails.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDetails(object):
    def setupUi(self, DialogDetails):
        DialogDetails.setObjectName("DialogDetails")
        DialogDetails.resize(452, 341)
        self.gridLayout = QtWidgets.QGridLayout(DialogDetails)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(DialogDetails)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lengthorg = QtWidgets.QLabel(DialogDetails)
        self.lengthorg.setText("")
        self.lengthorg.setObjectName("lengthorg")
        self.gridLayout.addWidget(self.lengthorg, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(DialogDetails)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lengthresult = QtWidgets.QLabel(DialogDetails)
        self.lengthresult.setText("")
        self.lengthresult.setObjectName("lengthresult")
        self.gridLayout.addWidget(self.lengthresult, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DialogDetails)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.procents = QtWidgets.QLabel(DialogDetails)
        self.procents.setText("")
        self.procents.setObjectName("procents")
        self.gridLayout.addWidget(self.procents, 2, 1, 1, 1)

        self.retranslateUi(DialogDetails)
        QtCore.QMetaObject.connectSlotsByName(DialogDetails)

    def retranslateUi(self, DialogDetails):
        _translate = QtCore.QCoreApplication.translate
        DialogDetails.setWindowTitle(_translate("DialogDetails", "Dialog"))
        self.label.setText(_translate("DialogDetails", "Length of the original audio:"))
        self.label_2.setText(_translate("DialogDetails", "Length of the result:"))
        self.label_3.setText(_translate("DialogDetails", "Time was reduced by:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogDetails = QtWidgets.QDialog()
    ui = Ui_DialogDetails()
    ui.setupUi(DialogDetails)
    DialogDetails.show()
    sys.exit(app.exec_())
