from PyQt6 import QtCore, uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from sound.sounds import Sound

import traceback
import io

# шаблон из Qt designer
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>679</width>
    <height>759</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(247, 248, 251);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0" colspan="3">
     <widget class="QTableView" name="table">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
    </item>
    <item row="1" column="0" alignment="Qt::AlignRight|Qt::AlignVCenter">
     <widget class="QPushButton" name="play">
      <property name="minimumSize">
       <size>
        <width>50</width>
        <height>50</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">font: 75 62pt &quot;Tahoma&quot;;
border: 1px solid rgb(200, 200, 200);
border-radius: 15px;
background-color: rgb(214, 214, 214);
width: 75px;
height: 75 px;</string>
      </property>
      <property name="text">
       <string>▶</string>
      </property>
     </widget>
    </item>
    <item row="1" column="1" alignment="Qt::AlignHCenter|Qt::AlignVCenter">
     <widget class="QPushButton" name="headphones">
      <property name="minimumSize">
       <size>
        <width>50</width>
        <height>50</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">font: 75 32pt &quot;Tahoma&quot;;
border: 1px solid rgb(200, 200, 200);
border-radius: 15px;
background-color: rgb(214, 214, 214);
width: 75px;
height: 75 px;</string>
      </property>
      <property name="text">
       <string>🎧</string>
      </property>
     </widget>
    </item>
    <item row="1" column="2" alignment="Qt::AlignLeft|Qt::AlignVCenter">
     <widget class="QPushButton" name="update">
      <property name="minimumSize">
       <size>
        <width>50</width>
        <height>50</height>
       </size>
      </property>
      <property name="styleSheet">
       <string notr="true">font: 75 42pt &quot;Tahoma&quot;;
border: 1px solid rgb(200, 200, 200);
border-radius: 15px;
background-color: rgb(214, 214, 214);
width: 75px;
height: 75 px;</string>
      </property>
      <property name="text">
       <string>↻</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):  # разрешение экрана
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Name(QMainWindow):  # программа
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):  # дизайн, назначение команд
        self.setWindowTitle('SoundPad')


def excepthook(exc_type, exc_value, exc_tb):  # ошибки
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)
