# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plot.ui'
#
# Created: Wed May 08 10:02:53 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_win_plot(object):
    def setupUi(self, win_plot):
        win_plot.setObjectName(_fromUtf8("win_plot"))
        win_plot.resize(800, 600)
        self.centralwidget = QtGui.QWidget(win_plot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.qwtPlot = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.verticalLayout.addWidget(self.qwtPlot)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
                
        self.currentNote = QtGui.QLabel(self.centralwidget)
        self.currentNote.setObjectName(_fromUtf8("currentNote"))
        self.horizontalLayout.addWidget(self.currentNote)
        
        self.nextNote = QtGui.QLabel(self.centralwidget)
        self.nextNote.setObjectName(_fromUtf8("nextNote"))
        self.horizontalLayout.addWidget(self.nextNote)

        font = QtGui.QFont("Arial", 14, QtGui.QFont.Bold) 
        self.currentNote.setFont(font)
        self.nextNote.setFont(font)
                

#        self.btnA = QtGui.QPushButton(self.centralwidget)
#        self.btnA.setObjectName(_fromUtf8("btnA"))
#        self.horizontalLayout.addWidget(self.btnA)

        self.verticalLayout.addLayout(self.horizontalLayout)
        win_plot.setCentralWidget(self.centralwidget)

        self.retranslateUi(win_plot)
        QtCore.QMetaObject.connectSlotsByName(win_plot)

    def retranslateUi(self, win_plot):
        win_plot.setWindowTitle(QtGui.QApplication.translate("win_plot", "Song Builder", None, QtGui.QApplication.UnicodeUTF8))
#        self.btnA.setText(QtGui.QApplication.translate("win_plot", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.currentNote.setText(QtGui.QApplication.translate("win_plot", "Current Note: ", None, QtGui.QApplication.UnicodeUTF8))
        self.nextNote.setText(QtGui.QApplication.translate("win_plot", "Try Playing: ", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qwt5

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    win_plot = QtGui.QMainWindow()
    ui = Ui_win_plot()
    ui.setupUi(win_plot)
    win_plot.show()
    sys.exit(app.exec_())

