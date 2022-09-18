import time
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import pandas as pd
import csv
import os

#Calvin Reese
#6/1/22
#Thing Speak Plotter for Dr. Li's summer internship

class Ui_MainWindow(QWidget):
    def __init__(self,parent=None):
        super(Ui_MainWindow, self).__init__(parent)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow") #Creates the Window
        MainWindow.resize(800, 900) #Sets the window size
        MainWindow.setAutoFillBackground(False) #disables flat background
        MainWindow.setWindowIcon(QtGui.QIcon("Fort_Lewis_Skyhawks_logo.png")) #sets the top left corner's icon
        self.centralwidget = QtWidgets.QWidget(MainWindow) #sets the main window as the central widget
        self.centralwidget.setObjectName("centralwidget") # names the central widget as central widget so it can be referenced in the stylesheet
        
        QApplication.setAttribute(Qt.AA_DisableWindowContextHelpButton) #Turns off the question mark that shows up next to the X button

        #MainWindow.setStyleSheet("background-color: rgb(250,255,255)")

        self.everything = QtWidgets.QBoxLayout(2,self.centralwidget) #This is the layout that holds everything and puts it in the central widget
        self.buttonLayout = QtWidgets.QBoxLayout(0) #This is the layout that organizes the frames which hold all the buttons (the top half of the GUI)
        self.topboxes_0 = QtWidgets.QBoxLayout(2) #topboxes go inside the buttonLayout and hold the 3 sets of 8 buttons
        self.topboxes_1 = QtWidgets.QBoxLayout(2) 
        self.topboxes_2 = QtWidgets.QBoxLayout(2)
        self.topLabels_0 = QtWidgets.QBoxLayout(0)#TopLabels goes into the topboxes as the plot  export  name  temp labels
        self.topLabels_1 = QtWidgets.QBoxLayout(0)
        self.topLabels_2 = QtWidgets.QBoxLayout(0)
        #These predefine the layout that contain each set of plot, export, name and temp displays
        self.buttons_0 = QtWidgets.QBoxLayout(0)
        self.buttons_1 = QtWidgets.QBoxLayout(0)
        self.buttons_2 = QtWidgets.QBoxLayout(0)
        self.buttons_3 = QtWidgets.QBoxLayout(0)
        self.buttons_4 = QtWidgets.QBoxLayout(0)
        self.buttons_5 = QtWidgets.QBoxLayout(0)
        self.buttons_6 = QtWidgets.QBoxLayout(0)
        self.buttons_7 = QtWidgets.QBoxLayout(0)
        self.buttons_8 = QtWidgets.QBoxLayout(0)
        self.buttons_9 = QtWidgets.QBoxLayout(0)
        self.buttons_10 = QtWidgets.QBoxLayout(0)
        self.buttons_11 = QtWidgets.QBoxLayout(0)
        self.buttons_12 = QtWidgets.QBoxLayout(0)
        self.buttons_13 = QtWidgets.QBoxLayout(0)
        self.buttons_14 = QtWidgets.QBoxLayout(0)
        self.buttons_15 = QtWidgets.QBoxLayout(0)
        self.buttons_16 = QtWidgets.QBoxLayout(0)
        self.buttons_17 = QtWidgets.QBoxLayout(0)
        self.buttons_18 = QtWidgets.QBoxLayout(0)
        self.buttons_19 = QtWidgets.QBoxLayout(0)
        self.buttons_20 = QtWidgets.QBoxLayout(0)
        self.buttons_21 = QtWidgets.QBoxLayout(0)
        self.buttons_22 = QtWidgets.QBoxLayout(0)
        self.buttons_23 = QtWidgets.QBoxLayout(0)
        #These predefines each plot, export buttons and numbers that display the temps
        self.lcdNumber_0 = QtWidgets.QLCDNumber()
        self.pushButton_0 = QtWidgets.QPushButton()
        self.pushEButton_0 = QtWidgets.QPushButton()
        self.name_0 = QLabel(self.channelKey[0])
        self.buttonsFrame_0 = QtWidgets.QFrame() #note that I put everything I wanted stylized in frames because setStyleSheet() doesn't work on layouts, only widgets
        self.lcdNumber_1 = QtWidgets.QLCDNumber()
        self.pushButton_1 = QtWidgets.QPushButton()
        self.pushEButton_1 = QtWidgets.QPushButton()
        self.name_1 = QLabel(self.channelKey[1])
        self.buttonsFrame_1 = QtWidgets.QFrame()
        self.lcdNumber_2 = QtWidgets.QLCDNumber()
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushEButton_2 = QtWidgets.QPushButton()
        self.name_2 = QLabel(self.channelKey[2])
        self.buttonsFrame_2 = QtWidgets.QFrame()
        self.lcdNumber_3 = QtWidgets.QLCDNumber()
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushEButton_3 = QtWidgets.QPushButton()
        self.name_3 = QLabel(self.channelKey[3])
        self.buttonsFrame_3 = QtWidgets.QFrame()
        self.lcdNumber_4 = QtWidgets.QLCDNumber()
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushEButton_4 = QtWidgets.QPushButton()
        self.name_4 = QLabel(self.channelKey[4])
        self.buttonsFrame_4 = QtWidgets.QFrame()
        self.lcdNumber_5 = QtWidgets.QLCDNumber()
        self.pushButton_5 = QtWidgets.QPushButton()
        self.pushEButton_5 = QtWidgets.QPushButton()
        self.name_5 = QLabel(self.channelKey[5])
        self.buttonsFrame_5 = QtWidgets.QFrame()
        self.lcdNumber_6 = QtWidgets.QLCDNumber()
        self.pushButton_6 = QtWidgets.QPushButton()
        self.pushEButton_6 = QtWidgets.QPushButton()
        self.name_6 = QLabel(self.channelKey[6])
        self.buttonsFrame_6 = QtWidgets.QFrame()
        self.lcdNumber_7 = QtWidgets.QLCDNumber()
        self.pushButton_7 = QtWidgets.QPushButton()
        self.pushEButton_7 = QtWidgets.QPushButton()
        self.name_7 = QLabel(self.channelKey[7])
        self.buttonsFrame_7 = QtWidgets.QFrame()
        self.lcdNumber_8 = QtWidgets.QLCDNumber()
        self.pushButton_8 = QtWidgets.QPushButton()
        self.pushEButton_8 = QtWidgets.QPushButton()
        self.name_8 = QLabel(self.channelKey[8])
        self.buttonsFrame_8 = QtWidgets.QFrame()
        self.lcdNumber_9 = QtWidgets.QLCDNumber()
        self.pushButton_9 = QtWidgets.QPushButton()
        self.pushEButton_9 = QtWidgets.QPushButton()
        self.name_9 = QLabel(self.channelKey[9])
        self.buttonsFrame_9 = QtWidgets.QFrame()
        self.lcdNumber_10 = QtWidgets.QLCDNumber()
        self.pushButton_10 = QtWidgets.QPushButton()
        self.pushEButton_10 = QtWidgets.QPushButton()
        self.name_10 = QLabel(self.channelKey[10])
        self.buttonsFrame_10 = QtWidgets.QFrame()
        self.lcdNumber_11 = QtWidgets.QLCDNumber()
        self.pushButton_11 = QtWidgets.QPushButton()
        self.pushEButton_11 = QtWidgets.QPushButton()
        self.name_11 = QLabel(self.channelKey[11])
        self.buttonsFrame_11 = QtWidgets.QFrame()
        self.lcdNumber_12 = QtWidgets.QLCDNumber()
        self.pushButton_12 = QtWidgets.QPushButton()
        self.pushEButton_12 = QtWidgets.QPushButton()
        self.name_12 = QLabel(self.channelKey[12])
        self.buttonsFrame_12 = QtWidgets.QFrame()
        self.lcdNumber_13 = QtWidgets.QLCDNumber()
        self.pushButton_13 = QtWidgets.QPushButton()
        self.pushEButton_13 = QtWidgets.QPushButton()
        self.name_13 = QLabel(self.channelKey[13])
        self.buttonsFrame_13 = QtWidgets.QFrame()
        self.lcdNumber_14 = QtWidgets.QLCDNumber()
        self.pushButton_14 = QtWidgets.QPushButton()
        self.pushEButton_14 = QtWidgets.QPushButton()
        self.name_14 = QLabel(self.channelKey[14])
        self.buttonsFrame_14 = QtWidgets.QFrame()
        self.lcdNumber_15 = QtWidgets.QLCDNumber()
        self.pushButton_15 = QtWidgets.QPushButton()
        self.pushEButton_15 = QtWidgets.QPushButton()
        self.name_15 = QLabel(self.channelKey[15])
        self.buttonsFrame_15 = QtWidgets.QFrame()
        self.lcdNumber_16 = QtWidgets.QLCDNumber()
        self.pushButton_16 = QtWidgets.QPushButton()
        self.pushEButton_16 = QtWidgets.QPushButton()
        self.name_16 = QLabel(self.channelKey[16])
        self.buttonsFrame_16 = QtWidgets.QFrame()
        self.lcdNumber_17 = QtWidgets.QLCDNumber()
        self.pushButton_17 = QtWidgets.QPushButton()
        self.pushEButton_17 = QtWidgets.QPushButton()
        self.name_17 = QLabel(self.channelKey[17])
        self.buttonsFrame_17 = QtWidgets.QFrame()
        self.lcdNumber_18 = QtWidgets.QLCDNumber()
        self.pushButton_18 = QtWidgets.QPushButton()
        self.pushEButton_18 = QtWidgets.QPushButton()
        self.name_18 = QLabel(self.channelKey[18])
        self.buttonsFrame_18 = QtWidgets.QFrame()
        self.lcdNumber_19 = QtWidgets.QLCDNumber()
        self.pushButton_19 = QtWidgets.QPushButton()
        self.pushEButton_19 = QtWidgets.QPushButton()
        self.name_19 = QLabel(self.channelKey[19])
        self.buttonsFrame_19 = QtWidgets.QFrame()
        self.lcdNumber_20 = QtWidgets.QLCDNumber()
        self.pushButton_20 = QtWidgets.QPushButton()
        self.pushEButton_20 = QtWidgets.QPushButton()
        self.name_20 = QLabel(self.channelKey[20])
        self.buttonsFrame_20 = QtWidgets.QFrame()
        self.lcdNumber_21 = QtWidgets.QLCDNumber()
        self.pushButton_21 = QtWidgets.QPushButton()
        self.pushEButton_21 = QtWidgets.QPushButton()
        self.name_21 = QLabel(self.channelKey[21])
        self.buttonsFrame_21 = QtWidgets.QFrame()
        self.lcdNumber_22 = QtWidgets.QLCDNumber()
        self.pushButton_22 = QtWidgets.QPushButton()
        self.pushEButton_22 = QtWidgets.QPushButton()
        self.name_22 = QLabel(self.channelKey[22])
        self.buttonsFrame_22 = QtWidgets.QFrame()
        self.lcdNumber_23 = QtWidgets.QLCDNumber()
        self.pushButton_23 = QtWidgets.QPushButton()
        self.pushEButton_23 = QtWidgets.QPushButton()
        self.name_23 = QLabel(self.channelKey[23])
        self.buttonsFrame_23 = QtWidgets.QFrame()
#This dictionary enables us to use a for loop to generate each set of buttons and LCD displays instead of using 700 lines of code to define each one individualy.
#It is orgainized as plot:plot button, export:export button, lcd:lcd display,  frame: button frame, name: name label, and section: topboxes
        self.buttonsDict = {"top0":self.buttons_0,"lcd0":self.lcdNumber_0,"plot0":self.pushButton_0,"export0":self.pushEButton_0,"name0":self.name_0,"frame0":self.buttonsFrame_0,"top1":self.buttons_1,"lcd1":self.lcdNumber_1,"plot1":self.pushButton_1,"export1":self.pushEButton_1,"name1":self.name_1,"frame1":self.buttonsFrame_1,"top2":self.buttons_2,"lcd2":self.lcdNumber_2,"plot2":self.pushButton_2,"export2":self.pushEButton_2,"name2":self.name_2,"frame2":self.buttonsFrame_2,"top3":self.buttons_3,"lcd3":self.lcdNumber_3,"plot3":self.pushButton_3,"export3":self.pushEButton_3,"name3":self.name_3,"frame3":self.buttonsFrame_3,"top4":self.buttons_4,"lcd4":self.lcdNumber_4,"plot4":self.pushButton_4,"export4":self.pushEButton_4,"name4":self.name_4,"frame4":self.buttonsFrame_4,"top5":self.buttons_5,"lcd5":self.lcdNumber_5,"plot5":self.pushButton_5,"export5":self.pushEButton_5,"name5":self.name_5,"frame5":self.buttonsFrame_5,"top6":self.buttons_6,"lcd6":self.lcdNumber_6,"plot6":self.pushButton_6,"export6":self.pushEButton_6,"name6":self.name_6,"frame6":self.buttonsFrame_6,"top7":self.buttons_7,"lcd7":self.lcdNumber_7,"plot7":self.pushButton_7,"export7":self.pushEButton_7,"name7":self.name_7,"frame7":self.buttonsFrame_7,"top8":self.buttons_8,"lcd8":self.lcdNumber_8,"plot8":self.pushButton_8,"export8":self.pushEButton_8,"name8":self.name_8,"frame8":self.buttonsFrame_8,"top9":self.buttons_9,"lcd9":self.lcdNumber_9,"plot9":self.pushButton_9,"export9":self.pushEButton_9,"name9":self.name_9,"frame9":self.buttonsFrame_9,"top10":self.buttons_10,"lcd10":self.lcdNumber_10,"plot10":self.pushButton_10,"export10":self.pushEButton_10,"name10":self.name_10,"frame10":self.buttonsFrame_10,"top11":self.buttons_11,"lcd11":self.lcdNumber_11,"plot11":self.pushButton_11,"export11":self.pushEButton_11,"name11":self.name_11,"frame11":self.buttonsFrame_11,"top12":self.buttons_12,"lcd12":self.lcdNumber_12,"plot12":self.pushButton_12,"export12":self.pushEButton_12,"name12":self.name_12,"frame12":self.buttonsFrame_12,"top13":self.buttons_13,"lcd13":self.lcdNumber_13,"plot13":self.pushButton_13,"export13":self.pushEButton_13,"name13":self.name_13,"frame13":self.buttonsFrame_13,"top14":self.buttons_14,"lcd14":self.lcdNumber_14,"plot14":self.pushButton_14,"export14":self.pushEButton_14,"name14":self.name_14,"frame14":self.buttonsFrame_14,"top15":self.buttons_15,"lcd15":self.lcdNumber_15,"plot15":self.pushButton_15,"export15":self.pushEButton_15,"name15":self.name_15,"frame15":self.buttonsFrame_15,"top16":self.buttons_16,"lcd16":self.lcdNumber_16,"plot16":self.pushButton_16,"export16":self.pushEButton_16,"name16":self.name_16,"frame16":self.buttonsFrame_16,"top17":self.buttons_17,"lcd17":self.lcdNumber_17,"plot17":self.pushButton_17,"export17":self.pushEButton_17,"name17":self.name_17,"frame17":self.buttonsFrame_17,"top18":self.buttons_18,"lcd18":self.lcdNumber_18,"plot18":self.pushButton_18,"export18":self.pushEButton_18,"name18":self.name_18,"frame18":self.buttonsFrame_18,"top19":self.buttons_19,"lcd19":self.lcdNumber_19,"plot19":self.pushButton_19,"export19":self.pushEButton_19,"name19":self.name_19,"frame19":self.buttonsFrame_19,"top20":self.buttons_20,"lcd20":self.lcdNumber_20,"plot20":self.pushButton_20,"export20":self.pushEButton_20,"name20":self.name_20,"frame20":self.buttonsFrame_20,"top21":self.buttons_21,"lcd21":self.lcdNumber_21,"plot21":self.pushButton_21,"export21":self.pushEButton_21,"name21":self.name_21,"frame21":self.buttonsFrame_21,"top22":self.buttons_22,"lcd22":self.lcdNumber_22,"plot22":self.pushButton_22,"export22":self.pushEButton_22,"name22":self.name_22,"frame22":self.buttonsFrame_22,"top23":self.buttons_23,"lcd23":self.lcdNumber_23,"plot23":self.pushButton_23,"export23":self.pushEButton_23,"name23":self.name_23,"frame23":self.buttonsFrame_23,"section0":self.topboxes_0,"section1":self.topboxes_1,"section2":self.topboxes_2}


#Menu Bar
        menuBar = MainWindow.menuBar()
        # fileMenu is the top menu bar which holds the file, plot options, and refresh
        fileMenu = QMenu("&File", self) #file holds the triggers for everything that references a channel, including export, adding, removing, and renaming options
        menuBar.addMenu(fileMenu)
        exportAll = QAction("&Export All",self)
        exportAll.triggered.connect(self.exportAllData)
        fileMenu.addAction(exportAll)
        rename = QAction("&Rename Channels",self)
        rename.triggered.connect(self.renameChannels)
        fileMenu.addAction(rename)   
        newChannel = QAction("&New Channels",self)
        newChannel.triggered.connect(self.addChannel)
        fileMenu.addAction(newChannel)   
        removeChannel = QAction("&Remove Channels",self)
        removeChannel.triggered.connect(self.delChannel)
        fileMenu.addAction(removeChannel)

        plotOptions = QMenu("&Plot Options",self) # plot options holds the options in which you can display the plots including poping out the plots and removing the integrated plot display
        menuBar.addMenu(plotOptions)
        togglePlots = QAction("&Toggle Popout Plots",self)
        togglePlots.triggered.connect(self.togglePopoutPlots)
        plotOptions.addAction(togglePlots)
        hideShowPlot = QAction("&Hide/Show Plot",self)
        hideShowPlot.triggered.connect(self.togglePlot)
        plotOptions.addAction(hideShowPlot)


        refresher = QAction("&Refresh Page",self) #this will refresh to make sure all the proper buttons are being displayed and the most current data is used
        refresher.triggered.connect(self.refresh)
        menuBar.addAction(refresher)

# Plot
        self.figure = plt.figure()
        plt.title("Temperature in Fahrenheit (past 20 mins)",fontsize=15)
        #plt.xlabel("time")
        plt.ylabel("Temperature",fontsize=15)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar(self.canvas,self)

        # creating a Vertical Box layout
        layout = QVBoxLayout()
        
        # adding tool bar to the layout
        layout.addWidget(self.toolbar)
          
        # adding canvas to the layout
        layout.addWidget(self.canvas)
        # setting layout to the main window
        self.plot = QtWidgets.QBoxLayout(2)
        self.plot.addLayout(layout)

#Top Labels being generated after being defined above
        plotLabel_0 = QLabel("Plot")
        plotLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        exportLabel_0 = QLabel("Export")
        exportLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        nameLabel_0 = QLabel("Name")
        nameLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        tempLabel_0 = QLabel("Temperature")
        tempLabel_0.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabels_0.addWidget(plotLabel_0)
        self.topLabels_0.addWidget(exportLabel_0)
        self.topLabels_0.addWidget(nameLabel_0)
        self.topLabels_0.addWidget(tempLabel_0)
        plotLabel_1 = QLabel("Plot")
        plotLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        exportLabel_1 = QLabel("Export")
        exportLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        nameLabel_1 = QLabel("Name")
        nameLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        tempLabel_1 = QLabel("Temperature")
        tempLabel_1.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabels_1.addWidget(plotLabel_1)
        self.topLabels_1.addWidget(exportLabel_1)
        self.topLabels_1.addWidget(nameLabel_1)
        self.topLabels_1.addWidget(tempLabel_1)
        plotLabel_2 = QLabel("Plot")
        plotLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        exportLabel_2 = QLabel("Export")
        exportLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        nameLabel_2 = QLabel("Name")
        nameLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        tempLabel_2 = QLabel("Temperature")
        tempLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabels_2.addWidget(plotLabel_2)
        self.topLabels_2.addWidget(exportLabel_2)
        self.topLabels_2.addWidget(nameLabel_2)
        self.topLabels_2.addWidget(tempLabel_2)

        self.topboxes_0.addLayout(self.topLabels_0)
        self.topboxes_1.addLayout(self.topLabels_1)
        self.topboxes_2.addLayout(self.topLabels_2)
        
#Font for LCD. This makes it easier to see what the LCD displays are showing
        lcdfont = QtGui.QFont()
        lcdfont.setBold(True)
        lcdfont.setItalic(False) 
        lcdfont.setWeight(75)

# Buttons set up
        for i in range(0,24):
            j = str(i)
            self.buttonsDict["lcd"+j].setFont(lcdfont) #setting the font for each LCD
            self.buttonsDict["lcd"+j].setAutoFillBackground(False) #Making the background of each LCD transparent
            self.buttonsDict["lcd"+j].setSegmentStyle(QLCDNumber.Flat) #Makes the LCD a little easier to read stylewise
            self.buttonsDict["lcd"+j].setDigitCount(3) #makes the LCD fit nicely with everything and will never need more than 3 digits (hopefully)
            self.buttonsDict["lcd"+j].setStyleSheet("color: white;\nborder-color: black;") #defines the colors of the LCD digits
            self.buttonsDict["plot"+j].setObjectName("pushButton_"+j) #defines the name of the plot button to be used in the stylesheet
            self.buttonsDict["plot"+j].setSizePolicy(1,1) #makes the button resize with the window
            self.buttonsDict["export"+j].setObjectName("pushEButton_"+j)
            self.buttonsDict["export"+j].setSizePolicy(1,1)
            self.buttonsDict["name"+j].setSizePolicy(1,1) #makes the name resize with the window
            self.buttonsDict["name"+j].setAlignment(QtCore.Qt.AlignCenter) #centers the name in it's deticated space
            self.buttonsDict["name"+j].setFixedWidth(150) #makes the name always size 150 to keep all the buttons and LCDs uniform no matter how big the name is (note this limits the number of charicters to 15)
            #add each element to it's respective spot
            self.buttonsDict["top"+j].addWidget(self.buttonsDict["plot"+j])
            self.buttonsDict["top"+j].addWidget(self.buttonsDict["export"+j])
            self.buttonsDict["top"+j].addWidget(self.buttonsDict["name"+j])
            self.buttonsDict["top"+j].addWidget(self.buttonsDict["lcd"+j])
            self.buttonsDict["frame"+j].setLayout(self.buttonsDict["top"+j])
            self.buttonsDict["section"+str(int(i/8))].addWidget(self.buttonsDict["frame"+j])
            notResize = self.buttonsDict["frame"+j].sizePolicy()#makes it so if a button set is not displayed, it still takes up the room so all the buttons are uniform
            notResize.setRetainSizeWhenHidden(True)
            self.buttonsDict["frame"+j].setSizePolicy(notResize)
            if(len(self.channelURL)<=i):
                self.buttonsDict["frame"+j].setVisible(False) #hides any button sets that cannot be used
            #Decor - button sets
            self.buttonsDict["frame"+j].setStyleSheet("""
             QPushButton { 
                 background-color: rgb(255,195,80);
                 border-style: outset;
                 border-width: 2px;
                 border-radius: 10px;
                 border-color: rgb(255,165,60);
                 min-width: 10em;
                 padding: -64px;}
             QPushButton:pressed {
                 border-style: inset;}
             QPushButton:hover {
                 background-color: rgb(225,180,70);}
             QLabel{
                 font: "Helvetica"}
             QFrame{
                 border-style: outset;
             }""")# the negative padding on the QPushButtons makes it so the buttons shrink when the window gets smaller, everything else makes them look nice.
#Laying out the Layout
        self.topFrame_0 = QtWidgets.QFrame()
        self.topFrame_0.setLayout(self.topboxes_0)
        self.buttonLayout.addWidget(self.topFrame_0)
        self.topFrame_0.setFrameStyle(6)
        self.topFrame_0.setFrameShadow(2)
        self.topFrame_0.setMidLineWidth(2)
        self.topFrame_1 = QtWidgets.QFrame()
        self.topFrame_1.setLayout(self.topboxes_1)
        self.buttonLayout.addWidget(self.topFrame_1)
        self.topFrame_1.setFrameShape(6)
        self.topFrame_2 = QtWidgets.QFrame()
        self.topFrame_2.setLayout(self.topboxes_2)
        self.buttonLayout.addWidget(self.topFrame_2)
        self.topFrame_2.setFrameShape(6)
        if(len(self.channelURL)<=8): #these hide the larger topboxes so the less buttons there are, the more space they can take
            self.topFrame_1.hide()
        if(len(self.channelURL)<=16):
            self.topFrame_2.hide()

        self.everything.addLayout(self.buttonLayout) #This adds the top buttons and the plot to the "everything" layout so that everything is organized correctly no matter the size of the window
        self.everything.addLayout(self.plot)
        self.topFrame_0.setObjectName("topFrame_0")
        self.topFrame_1.setObjectName("topFrame_1")
        self.topFrame_2.setObjectName("topFrame_2")
#Decor-MainWindow
        MainWindow.setStyleSheet("""
        #MainWindow{
            background-image: url(Fort lewis Background.png);
        }
        #topFrame_0{
           border-style: outset;
           border-width: 2px;
           border-radius: 10px;
           border-color: rgb(253,186,47);
           min-width: 10em;
        }
        #topFrame_1{
           border-style: outset;
           border-width: 2px;
           border-radius: 10px;
           border-color: rgb(253,186,47);
           min-width: 10em;
        }
        #topFrame_2{
           border-style: outset;
           border-width: 2px;
           border-radius: 10px;
           border-color: rgb(253,186,47);
           min-width: 10em;
        }
        QLabel{
            font-family: Arial;
            font-size: 13pt;
            font-weight: bold;
            color: white;
        }""")
        

#Assignning Buttons
#the lambda: option allows me to pass a value into the function rather than simply calling it
#The usual format is .connect(self.function)
        try:
            self.pushButton_0.clicked.connect(lambda: self.showData(0))
            self.pushEButton_0.clicked.connect(lambda: self.exportData(0))
            self.pushButton_1.clicked.connect(lambda: self.showData(1))
            self.pushEButton_1.clicked.connect(lambda: self.exportData(1))
            self.pushButton_2.clicked.connect(lambda: self.showData(2))
            self.pushEButton_2.clicked.connect(lambda: self.exportData(2))
            self.pushButton_3.clicked.connect(lambda: self.showData(3))
            self.pushEButton_3.clicked.connect(lambda: self.exportData(3))
            self.pushButton_4.clicked.connect(lambda: self.showData(4))
            self.pushEButton_4.clicked.connect(lambda: self.exportData(4))
            self.pushButton_5.clicked.connect(lambda: self.showData(5))
            self.pushEButton_5.clicked.connect(lambda: self.exportData(5))
            self.pushButton_6.clicked.connect(lambda: self.showData(6))
            self.pushEButton_6.clicked.connect(lambda: self.exportData(6))
            self.pushButton_7.clicked.connect(lambda: self.showData(7))
            self.pushEButton_7.clicked.connect(lambda: self.exportData(7))
            self.pushButton_8.clicked.connect(lambda: self.showData(8))
            self.pushEButton_8.clicked.connect(lambda: self.exportData(8))
            self.pushButton_9.clicked.connect(lambda: self.showData(9))
            self.pushEButton_9.clicked.connect(lambda: self.exportData(9))
            self.pushButton_10.clicked.connect(lambda: self.showData(10))
            self.pushEButton_10.clicked.connect(lambda: self.exportData(10))
            self.pushButton_11.clicked.connect(lambda: self.showData(11))
            self.pushEButton_11.clicked.connect(lambda: self.exportData(11))
            self.pushButton_12.clicked.connect(lambda: self.showData(12))
            self.pushEButton_12.clicked.connect(lambda: self.exportData(12))
            self.pushButton_13.clicked.connect(lambda: self.showData(13))
            self.pushEButton_13.clicked.connect(lambda: self.exportData(13))
            self.pushButton_14.clicked.connect(lambda: self.showData(14))
            self.pushEButton_14.clicked.connect(lambda: self.exportData(14))
            self.pushButton_15.clicked.connect(lambda: self.showData(15))
            self.pushEButton_15.clicked.connect(lambda: self.exportData(15))
            self.pushButton_16.clicked.connect(lambda: self.showData(16))
            self.pushEButton_16.clicked.connect(lambda: self.exportData(16))
            self.pushButton_17.clicked.connect(lambda: self.showData(17))
            self.pushEButton_17.clicked.connect(lambda: self.exportData(17))
            self.pushButton_18.clicked.connect(lambda: self.showData(18))
            self.pushEButton_18.clicked.connect(lambda: self.exportData(18))
            self.pushButton_19.clicked.connect(lambda: self.showData(19))
            self.pushEButton_19.clicked.connect(lambda: self.exportData(19))
            self.pushButton_20.clicked.connect(lambda: self.showData(20))
            self.pushEButton_20.clicked.connect(lambda: self.exportData(20))
            self.pushButton_21.clicked.connect(lambda: self.showData(21))
            self.pushEButton_21.clicked.connect(lambda: self.exportData(21))
            self.pushButton_22.clicked.connect(lambda: self.showData(22))
            self.pushEButton_22.clicked.connect(lambda: self.exportData(22))
            self.pushButton_23.clicked.connect(lambda: self.showData(23))
            self.pushEButton_23.clicked.connect(lambda: self.exportData(23))
        except:
            pass

#Other Functions
        MainWindow.setCentralWidget(self.centralwidget) #sets the centralwidget which has the "everything" layout as the central widget in the main window4

        self.statusBar = QtWidgets.QStatusBar(MainWindow) #creates the status bar
        self.statusBar.setObjectName("statusbar")
        self.progressBar = QProgressBar()
        self.statusBar.addWidget(self.progressBar)

        #AutoUpdate code: every second update the next lcd with current data. This prevents lag spikes of fetching all the data from all the channels at once while keeping everything updated
        self.updateLCD() #this is the initial fetching of data and displaying it one all the LCDs (this is why it takes a second to launch the program)
        self.timer=QTimer()
        self.timer.setInterval(10000) #this defines how rapidly the code updates each channel's display
        self.timer.start()
        self.counter = 0 #This keeps track of which channel needs to be updated next
        self.timer.timeout.connect(self.updateCycle)#exicutes updateCycle every time the interval is met
        '''usr code'''

        MainWindow.setStatusBar(self.statusBar)#sets the statusbar in the bottom window

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updateCycle(self): #this carries out the individual update from the timer
        self.counter += 1 #increment which channel needs to be updated
        self.counter = self.counter % len(self.channelURL) #cycles around the number of channels
        try: #This is tried because sometimes the URL reading fails and will throw an exception and we just want it to move on instead of crashing if that happens so it can try again later
            self.read_single_thingspeak(self.counter) #reads in the data for channel selection
            self.buttonsDict["lcd"+str<MouseMove>(self.counter)].display(self.data[self.counter][1][-1]) #update that LCD display with the updated info
        except: pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Reader")) #this is the title of the window

    def updateLCD(self): #display all newest temps
        self.read_data_thingspeak() #fetch all the new data
        for i in range(0,len(self.channelURL)):
            try: #if there isn't any data for an LCD since there is no channel, it just won't update since it shouldn't be displayed anyway
                self.buttonsDict["lcd"+str(i)].display(self.data[i][1][-1]) #update each LCD display
            except:
                pass

    def read_single_thingspeak(self,selectChannel,results=100): #reads the data from a single channel with a defult number of results as 100 (this is changed to 1000 in the export)
        try:
                URL=self.channelURL[selectChannel]#use & to separate multiple requests.timezone has been added to it.If No. of results are not specified, it reads anything <=100 data entries.
            #URL_2='https://api.thingspeak.com/channels/983197/fields/1.json?api_key=26ZX2F1R5YCUA83A&results=8000&timezone=America%2FDenver'#read 8000 data entries, about 3 days 
            #URL='https://api.thingspeak.com/channels/983197/fields/1.json?api_key=26ZX2F1R5YCUA83A&timezone=America%2FDenver'#if you do not specify the '&results=xx' it will read all the data since a few days ago (seems like it is 8 days)  
                URL = URL[0:URL.find("results=")+8]+str(results)+"&timezone=America%2FDenver" #fetches the data with the requested number of data points
                get_data=requests.get(URL).json() #converts the .json data from thingspeak into raw data
                feild_1=get_data['feeds'] 
                 #print(feild_1)
                temp=[] #all the temp points
                time=[] #all the time points
                for x in feild_1:
                    try:#if there is nan data, then it will throw an exception and skip it
                        temp.append(int(x['field1']))#pulls the data from the first set of data being sent to that channel
                        time.append(x['created_at'])
                    except: pass
                newselftm=[]#only shows the date and the time
                for tm in time:
                    newselftm.append(tm[:19])
    
                self.data[selectChannel]=[newselftm,temp]#update the data dict with the new data (new channels are appended to the end)
                                                                  #I chose to use an enumerated dictionary instead of a list because it is much easier to convert a dict to a pd.dataFrame than a list
        except Exception as e: print(e)

    def read_data_thingspeak(self,results = 100): #this function updates all available channels
        self.statusBar.show()
        self.progressBar.setValue(0)
        for selectChannel in range(len(self.channelURL)):
            self.read_single_thingspeak(selectChannel, results)
            self.progressBar.setValue(int(100/len(self.channelURL)*(selectChannel+1)))
        self.statusBar.hide()

    def togglePopoutPlots(self): self.popoutPlots = not(self.popoutPlots) #this toggles if a plot will become a popup when clicked
    def togglePlot(self): #This toggles if the embedded plot is shown or not
        if self.canvas.isVisible(): #reads if the canvas is hidden or not and toggles it's visible
            self.canvas.hide()#the toolbar and the plot are seperate widgets that need to be toggled independently
            self.toolbar.hide()
        else:
            self.canvas.show()
            self.toolbar.hide()

    def showData(self,selectChannel): #this updates the embedded plot
        if(selectChannel >= len(self.channelURL)): #checks to make sure the requested data exists
            return #don't do anything if the data doesn't exist
        self.figure.clear() #clears the canvas
        if(self.popoutPlots): #if popout plots are toggled on then generate the popout plot first
            self.popoutData(selectChannel)

        fig=plt.figure(figsize=(12,10))
        halftm=len(self.data[selectChannel][0])//2 #get every other data point for visablility
        halft=len(self.data[selectChannel][1])//2
        ax=self.figure.add_subplot(111) #turn the actual plot into a subplot do it displays in the embedded window
        ax.set_title("Temperature in "+self.channelKey[selectChannel]+" (past 20 mins)",fontsize=15) #set title
        ax.set_ylabel("Temperature",fontsize=15) #set label
        times = [e[11:16] for e in self.data[selectChannel][0]] #only show the hour and minute for visability and simplicity
        ax.scatter(times[halftm:-1], self.data[selectChannel][1][halft:-1],c=self.data[selectChannel][1][halft:-1], cmap='plasma',vmin = 0,vmax = 50) #plot the data
        plt.setp(ax.get_xticklabels(),rotation=10,ha="right") #rotate the x labels for visability
        for label in ax.get_xticklabels()[::2]: #hide half the x labels for visability
            label.set_visible(False)
        self.canvas.draw() #actually show the plot on the canvas

    def popoutData(self,selectChannel): #this displays a popout plot (see comments from showData for details)
        fig=plt.figure(self.channelKey[selectChannel],figsize=(12,10))
        plt.title("Temperature in "+self.channelKey[selectChannel]+" (past 20 mins)",fontsize=20)
        plt.ylabel("Temperature",fontsize=20)
        halftm=len(self.data[selectChannel][0])//2
        halft=len(self.data[selectChannel][1])//2
        ax=plt.subplot(1,1,1)
        times = [e[11:16] for e in self.data[selectChannel][0]]
        ax.scatter(times[halftm:-1], self.data[selectChannel][1][halft:-1],c=self.data[selectChannel][1][halft:-1], cmap='plasma',vmin = 0,vmax = 50)
        plt.setp(ax.get_xticklabels(),rotation=30,ha="right")
        for label in ax.get_xticklabels()[::2]:
            label.set_visible(False)
        fig.show()



    def exportData(self,selectChannel): # export 8000 data points to CSV
        if(selectChannel >= len(self.channelURL)): #if the channel doesn't exist, do nothing
            return
        self.read_data_thingspeak(8000)#pull updated data up to 8000 points (this SIGNIFICANTLY slows the export process, maybe make the number of points an option?)
        allData = pd.DataFrame(self.data[selectChannel]).transpose()#convert to dataframe
        allData.columns=["Time-"+self.channelKey[selectChannel],"Temp-"+self.channelKey[selectChannel]] #define column names

        try:
            allData.to_csv(self.channelKey[selectChannel]+"-tempData.csv",index=False) #export the data to .csv
        except:
            msg = QMessageBox()#error popup for trying to write to an open file
            msg.setWindowTitle("Error Generating File")
            msg.setText("Uh-Oh! Something Went Wrong!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setInformativeText("Try Closing:"+self.channelKey[selectChannel]+"-tempData.csv")
            if msg.exec_() == QMessageBox.Retry:
                self.exportData(selectChannel)

    def exportAllData(self):# exports 8000 data points from every channel to CSV
        self.read_data_thingspeak(8000)
        allData = pd.DataFrame()      
        labels = []
        for i in range(0,len(self.data)): 
            allData["Time-"+self.channelKey[i]] = pd.Series(self.data[i][0])
            allData["Temp-"+self.channelKey[i]] = pd.Series(self.data[i][1])

        try:
           allData.to_csv("tempData.csv",index=False)
        except:
            msg = QMessageBox()#error popup for trying to write to an open file
            msg.setWindowTitle("Error Generating File")
            msg.setText("Uh-Oh! Something Went Wrong!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setInformativeText("Try Closing: tempData.csv")
            if msg.exec_() == QMessageBox.Retry:
                self.exportAllData()

    def renameChannels(self): #renames the labels of a channel and saves it
        selection, ok = QInputDialog.getItem(self,"Rename Channel","Select A Channel to Rename:",self.channelKey[0:len(self.channelURL)],editable = False)
        if ok == False:
            return
        newName, ok = QInputDialog.getText(self,"Rename Channel","New Name:")
        if ok == False:
            return
        for name in self.channelKey:
            if(name == newName):
                msg = QMessageBox()#error popup for a duplicate name to prevent confusion in the program and for the user
                msg.setWindowTitle("Name Error")
                msg.setText("Error: Duplicate Name")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
                msg.setDefaultButton(QMessageBox.Retry)
                msg.setInformativeText('Try using : "'+newName+'_1"')
                if msg.exec_() == QMessageBox.Retry:
                    self.renameChannels()
                return
        if(len(newName) > 15):
                msg = QMessageBox() #error popup for a name that cannot be properly displayed (over char limit)
                msg.setWindowTitle("Name Error")
                msg.setText("Error: Over Character Limit")
                msg.setIcon(QMessageBox.Critical)
                msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
                msg.setDefaultButton(QMessageBox.Retry)
                msg.setInformativeText('Please pick a name less than 15 characters.')
                if msg.exec_() == QMessageBox.Retry:
                    self.renameChannels()
                return

        if(newName != ""): #cannot make a nonexistant name (same as a cancel)
            for i in range(0,len(self.channelKey)): #locate the old name
                if(selection == self.channelKey[i]): 
                    self.channelKey[i]=newName #set the new name
                    break
            self.saveChannel() #save the new name to the save name
            self.refresh() #display the new name and refresh the data

    def addChannel(self):  #adds a new channel and saves it
        API, ok = QInputDialog.getText(self,"New Channel","Channel API:") #get API from user
        if ok == False: return #if cancel is pressed, cancel the function
        ID, ok = QInputDialog.getText(self,"New Channel","Channel ID:") #get Channel ID from user
        if ok == False: return
        newName, ok = QInputDialog.getText(self,"New Channel","Channel Name:")#get new name for the channel
        if ok == False: return
        try:

            for name in self.channelKey:
                if(name == newName):
                    msg = QMessageBox()#error popup for duplicate names to prevent confusion in the program and for the user
                    msg.setWindowTitle("Name Error")
                    msg.setText("Error: Duplicate Name")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
                    msg.setDefaultButton(QMessageBox.Retry)
                    msg.setInformativeText('Try using : "'+newName+'_1"')
                    if msg.exec_() == QMessageBox.Retry:
                        self.addChannel()
                    return
            if(len(newName) > 15):
                    msg = QMessageBox()#error popup for a name that cannot be properly displayed
                    msg.setWindowTitle("Name Error")
                    msg.setText("Error: Over Character Limit")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
                    msg.setDefaultButton(QMessageBox.Retry)
                    msg.setInformativeText('Please pick a name less than 15 characters.')
                    if msg.exec_() == QMessageBox.Retry:
                        self.addChannel()
                    return
            #first test that the channel has data
            get_data=requests.get('https://api.thingspeak.com/channels/'+ID+'/fields/1.json?api_key='+API+'&results=100&timezone=America%2FDenver').json()
            feild_1=get_data['feeds']
            #add the channel to the list
            self.channelURL.append('https://api.thingspeak.com/channels/'+ID+'/fields/1.json?api_key='+API+'&results=100&timezone=America%2FDenver')
            self.channelKey[len(self.channelURL)-1]=str(newName) #add the new name to the list
            self.saveChannel()#save the new channel and name
            self.refresh()#show the new channel
        except PermissionError:
            msg = QMessageBox()#error popup for writing the new channel to the save file
            msg.setWindowTitle("Error Adding Channel")
            msg.setText("Uh-Oh! Something Went Wrong!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setInformativeText("Try Closing Channels.csv")
            if msg.exec_() == QMessageBox.Retry:
                self.addChannel()
        except:
            msg = QMessageBox() #error popup for a nonexistant channel
            msg.setWindowTitle("Error Adding Channel")
            msg.setText("Uh-Oh! Something Went Wrong!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.setInformativeText("Either the API or ID was incorrect.")
            if msg.exec_() == QMessageBox.Retry:
                self.addChannel()

    def delChannel(self): #removes a channel from GUI and save file
        selection, ok = QInputDialog.getItem(self,"Delete Channel","Select A Channel to Remove:",self.channelKey[0:len(self.channelURL)])
        if ok == False:
            return
        for i in range(0,len(self.channelURL)):
            if(self.channelKey[i] == selection):
                del self.channelURL[i]
                del self.channelKey[i]
                self.channelKey.append('newTemp')
                self.saveChannel()
                self.refresh()
                break

        
    def refresh(self): #makes sure all the buttons are displayed properly and updates all the LCDs with current data
        plt.close('all') 
        for i in self.channelURL:
            match len(self.channelURL): #shows all the usable buttons and hides the rest
                case 0:
                    self.buttonsDict["frame0"].hide()
                case 1:
                    self.buttonsDict["frame0"].show()
                    self.buttonsDict["frame1"].hide()
                case 2:
                    self.buttonsDict["frame1"].show()
                    self.buttonsDict["frame2"].hide()
                case 3:
                    self.buttonsDict["frame2"].show()
                    self.buttonsDict["frame3"].hide()
                case 4:
                    self.buttonsDict["frame3"].show()
                    self.buttonsDict["frame4"].hide()
                case 5:
                    self.buttonsDict["frame4"].show()
                    self.buttonsDict["frame5"].hide()
                case 6:
                    self.buttonsDict["frame5"].show()
                    self.buttonsDict["frame6"].hide()
                case 7:
                    self.buttonsDict["frame6"].show()
                    self.buttonsDict["frame7"].hide()
                case 8:
                    self.topFrame_1.hide()
                    self.buttonsDict["frame7"].show()
                    self.buttonsDict["frame8"].hide()
                case 9:
                    self.topFrame_1.show()
                    self.buttonsDict["frame8"].show()
                    self.buttonsDict["frame9"].hide()
                case 10:
                    self.buttonsDict["frame9"].show()
                    self.buttonsDict["frame10"].hide()
                case 11:
                    self.buttonsDict["frame10"].show()
                    self.buttonsDict["frame11"].hide()
                case 12:
                    self.buttonsDict["frame11"].show()
                    self.buttonsDict["frame12"].hide()
                case 13:
                    self.buttonsDict["frame12"].show()
                    self.buttonsDict["frame13"].hide()
                case 14:
                    self.buttonsDict["frame13"].show()
                    self.buttonsDict["frame14"].hide()
                case 15:
                    self.buttonsDict["frame14"].show()
                    self.buttonsDict["frame15"].hide()
                case 16:
                    self.topFrame_2.hide()
                    self.buttonsDict["frame15"].show()
                    self.buttonsDict["frame16"].hide()
                case 17:
                    self.topFrame_2.show()
                    self.buttonsDict["frame16"].show()
                    self.buttonsDict["frame17"].hide()
                case 18:
                    self.buttonsDict["frame17"].show()
                    self.buttonsDict["frame18"].hide()
                case 19:
                    self.buttonsDict["frame18"].show()
                    self.buttonsDict["frame19"].hide()
                case 20:
                    self.buttonsDict["frame19"].show()
                    self.buttonsDict["frame20"].hide()
                case 21:
                    self.buttonsDict["frame20"].show()
                    self.buttonsDict["frame21"].hide()
                case 22:
                    self.buttonsDict["frame21"].show()
                    self.buttonsDict["frame22"].hide()
                case 23:
                    self.buttonsDict["frame22"].show()
                    self.buttonsDict["frame23"].hide()
                case 24:
                    self.buttonsDict["frame23"].show()
            try:
                self.name_0.setText(self.channelKey[0])  #updates all the name labels to their correct names
                self.name_1.setText(self.channelKey[1])
                self.name_2.setText(self.channelKey[2])
                self.name_3.setText(self.channelKey[3])
                self.name_4.setText(self.channelKey[4])
                self.name_5.setText(self.channelKey[5])
                self.name_6.setText(self.channelKey[6])
                self.name_7.setText(self.channelKey[7])
                self.name_8.setText(self.channelKey[8])
                self.name_9.setText(self.channelKey[9])
                self.name_10.setText(self.channelKey[10])
                self.name_11.setText(self.channelKey[11])
                self.name_12.setText(self.channelKey[12])
                self.name_13.setText(self.channelKey[13])
                self.name_14.setText(self.channelKey[14])
                self.name_15.setText(self.channelKey[15])
                self.name_16.setText(self.channelKey[16])
                self.name_17.setText(self.channelKey[17])
                self.name_18.setText(self.channelKey[18])
                self.name_19.setText(self.channelKey[19])
                self.name_20.setText(self.channelKey[20])
                self.name_21.setText(self.channelKey[21])
                self.name_22.setText(self.channelKey[22])
                self.name_23.setText(self.channelKey[23])
            except:
                pass
        self.updateLCD() #fetch all new data and display it on all the LCDs

    def saveChannel(self): #updates the save file with any edits made
        with open('Channels.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.channelURL)
            writer.writerow(self.channelKey)

    def ChannelName_init(self): #defines any prerequired variables and parces out the save data
        self.data={}#holds the data read from ThingSpeak
        self.popoutPlots=False#toggle for popout plots option
        self.channelKey = channelSave[1]#holds the names of all the channels
        extend = ["newChannel"]*(24-len(self.channelKey))#gives a name to anything unnamed to prevent errors
        self.channelKey = self.channelKey+extend
        self.channelURL = channelSave[0]#holds all the ThingSpeak links
        for i in range(0,len(self.channelURL)):
            if (self.channelURL[i]==""):
                self.channelURL = self.channelURL[0:i-1]
                break
       
''' user code '''
if __name__ == '__main__':
    with open('Channels.csv', newline='') as f:
        channelSave = list(csv.reader(f)) #opens the save file and reads everything to a temporary variable

    #tt=read_data_thingspeak()
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.ChannelName_init()
    ui.setupUi(MainWindow)
#    ui.updateLCD(tt[-1])
    #tt[-1]+='1'
    MainWindow.show() # show the GUI
    #ui.showData() # plot the most recent 100 data points
    sys.exit(app.exec_())
