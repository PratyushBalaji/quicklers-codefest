import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from short import *

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('/Users/PratyushBalaji/Desktop/codefest/lung cancer/test.ui',self)

        # Button
        self.button.clicked.connect(self.submit)

        # Spin Box
        self.ageBox.setMinimum(1)
        self.ageBox.setMaximum(100)

    
    def submit(self):
        ipArr = []

        # Gender
        ipArr.append(self.male.isChecked())
        
        # Age
        ipArr.append(self.ageBox.value())

        # smoking
        ipArr.append(self.SMOKING.isChecked())

        # yellow
        ipArr.append(self.YELLOW_FINGERS.isChecked())

        # anxiety
        ipArr.append(self.ANXIETY.isChecked())
        
        # peer
        ipArr.append(self.PEER_PRESSURE.isChecked())

        # chronic
        ipArr.append(self.CHRONIC_DISEASE.isChecked())

        # fatigue
        ipArr.append(self.FATIGUE.isChecked())

        # allergy
        ipArr.append(self.ALLERGY.isChecked())

        # wheezing
        ipArr.append(self.WHEEZING.isChecked())

        # alc
        ipArr.append(self.ALCOHOL_CONSUMING.isChecked())

        # coughing
        ipArr.append(self.COUGHING.isChecked())

        # breath
        ipArr.append(self.SHORTNESS_OF_BREATH.isChecked())

        # swallowing
        ipArr.append(self.SWALLOWING_DIFFICULTY.isChecked())

        # chest
        ipArr.append(self.CHEST_PAIN.isChecked())

        # self.ALCOHOL_CONSUMING.isChecked()
        for i in range(len(ipArr)):
            if ipArr[i] == True:
                ipArr[i] = 1
            elif ipArr[i] == False:
                ipArr[i] = 0

        num = pred(ipArr)
        if num[0] == 1:
            self.final_2.setText("By analysing patterns from over 10000 cancer positive and negative patients, we find that your selection closely resembles that of a cancer patient")
        else:
            self.final_2.setText("you probably dont have cancer lol")


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(700)
widget.setFixedWidth(800)

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")