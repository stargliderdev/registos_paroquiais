#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

from PyQt5.QtWidgets import QTabWidget, QLabel, QTableWidgetItem, QVBoxLayout, QLineEdit, QComboBox, QDateEdit, \
    QWidget, QDialog, QHBoxLayout, QPushButton, QTextEdit, QMessageBox, QPlainTextEdit,QTextBrowser
from PyQt5.Qt import Qt
from PyQt5.QtCore import QDate

import qlib

def ex_grid_update(grid_ctrl, col, data=[], refresh=False, hidden=-1):
    def format_as_integer(d):
        # d = dado
        item = QTableWidgetItem()

        item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
        item.setText(str(d))
        return item

    def format_as_string(d):
        # d = dado
        item = QTableWidgetItem()

        #item.setTextAlignment(Qt.AlignRight)
        item.setText(d)
        return item

    def format_as_date_pld(d):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setText(d.strftime('%d.%b.%Y'))
        return item

    def format_as_date(d):
        item = QTableWidgetItem()
        v = QDate(d)
        item.setText(v.toString('dd.MM.yyyy'))
        item.setTextAlignment(Qt.AlignCenter)
        return item

    def format_as_string_center(d):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setText(d)
        return item

    headers = []
    col_type = []
    for k,v in col.items():
        # print v
        headers.append(v[0])
        col_type.append(v[1])
    colCount = len(headers)
    if not refresh :
        grid_ctrl.clear()
        grid_ctrl.setColumnCount(colCount)
        grid_ctrl.setHorizontalHeaderLabels(headers)
    grid_ctrl.setRowCount(0)
    grid_ctrl.setRowCount(len(data))
    lin = 0
    for n in data:
        for f in range(0,len(n)):
            if n[f] is None:
                pass
            else:
                if col_type[f] == 'i':
                    # print 'int'
                    grid_ctrl.setItem(lin, f, format_as_integer(n[f]))
                elif col_type[f] == 'd': # date
                    grid_ctrl.setItem(lin, f, format_as_date(n[f]))
                elif col_type[f] == 's':
                    grid_ctrl.setItem(lin, f, format_as_string(n[f]))
                elif col_type[f] == 'sc':
                    grid_ctrl.setItem(lin, f, format_as_string_center(n[f]))
        lin +=1
    if hidden >-1:
        grid_ctrl.hideColumn(hidden)
    if not refresh:
        grid_ctrl.resizeColumnsToContents()


def ex_grid__ctrl_update(grid_ctrl, col_dict, data = [], options = []):
    def format_as_integer(d):
        # d = dado
        item = QTableWidgetItem()

        item.setTextAlignment(Qt.AlignRight)
        item.setText(str(d))
        return item

    def format_as_string(d):
        # d = dado
        item = QTableWidgetItem()

        #item.setTextAlignment(Qt.AlignRight)
        item.setText(d)
        return item


    def format_as_date(d):
        # d = dado
        item = QTableWidgetItem()

        #item.setTextAlignment(Qt.AlignRight)
        item.setText(d.strftime('%d.%b.%Y'))
        return item

    def format_as_string_center(d):
        # d = dado
        item = QTableWidgetItem()

        item.setTextAlignment(Qt.AlignCenter)
        item.setText(d)
        return item

    number_of_columns = len(col_dict)
    headers = []
    col_type = []
    field_index = {}
    for k,v in col_dict.items():
        # print v
        headers.append(v[0])
        col_type.append(v[1])
        field_index[k] = v[2]
    colCount = len(headers)
    grid_ctrl.clear()
    grid_ctrl.setColumnCount(colCount)
    grid_ctrl.setHorizontalHeaderLabels(headers)
    grid_ctrl.setRowCount(0)
    grid_ctrl.setRowCount(len(data))
    lin = 0
    for n in data:
        for f in range(0,number_of_columns):
            if col_type[f] == 'i':
                # print 'int'
                grid_ctrl.setItem(lin, f, format_as_integer(n[field_index[f]]))
            elif col_type[f] == 'd': # date
                grid_ctrl.setItem(lin, f, format_as_date(n[field_index[f]]))
            elif col_type[f] == 's':
                grid_ctrl.setItem(lin, f, format_as_string(n[field_index[f]]))
            elif col_type[f] == 'sc':
                grid_ctrl.setItem(lin, f, format_as_string_center(n[field_index[f]]))
            elif col_type[f] == 'xb': # checkbox
                # grid_ctrl.setItem(lin, ' ', QCheckBox())
                grid_ctrl.setCellWidget(lin, f,qlib.checkBoxGrid())
        lin +=1
    grid_ctrl.resizeColumnsToContents()




if __name__ == '__main__':
    print('não corre')