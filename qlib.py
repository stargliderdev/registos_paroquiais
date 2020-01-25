#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTabWidget, QLabel, QCheckBox, QVBoxLayout, QLineEdit, QComboBox, QDateEdit, \
    QWidget, QDialog, QHBoxLayout
from PyQt5.QtCore import QObject
from PyQt5.Qt import Qt

# versão 1.0 2 NOV 2014

def checkBoxGrid(label=''):
    w = QWidget()
    l = QHBoxLayout(w)
    l.setContentsMargins(0,0,0,0)
    l.addStretch()
    c = QCheckBox(label)
    l.addWidget(c)
    l.addStretch()
    return w

def comboBoxGrid(ctrl_list):
    dum = QComboBox()
    # dum.setFrame(False)
    dum.addItems(ctrl_list)
    # dum.setEditable(True)
    return dum

class ComboBoxGrid(QObject):
    def __init__(self, ctrl_list):
        self.cb = QComboBox()
        # dum.setFrame(False)
        dum.addItems(ctrl_list)
        dum.setEditable(True)
    


def addHLayout(listobj1,label_size=80, label_align=Qt.AlignVCenter|Qt.AlignRight):
    dumLayout = QHBoxLayout()
    dumLayout.setContentsMargins(0,0,0,0)
    for n in listobj1:
        if (type(n)==str) or (type(n) == str):
            toto = QLabel(n)
            toto.setMinimumWidth(label_size)
            toto.setMaximumWidth(label_size)
            toto.setAlignment(label_align)
            dumLayout.addWidget(toto)
        elif type(n) == bool:
            dumLayout.addStretch()
        else:
            dumLayout.addWidget(n)
    return dumLayout

def addVLayout(listobj1):
    dumLayout = QVBoxLayout()
    for n in listobj1:
        if (type(n)==str) or (type(n) == str):
            dumLayout.addWidget(QLabel(n))
        elif type(n) == bool:
            dumLayout.addStretch()
        else:
            dumLayout.addWidget(n)
    return dumLayout