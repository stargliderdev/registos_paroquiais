#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
from random import randrange

from PyQt5.QtWidgets import QLineEdit, QComboBox,QPlainTextEdit,QCheckBox,QDateEdit,QTextEdit


def get_value(obj, dic = {}):
        a = type(obj)
        if a == QLineEdit:
            return obj.text()
        elif a == QDateEdit:
            return obj.date().toPyDate()
        elif a == QCheckBox:
            return obj.isChecked()
        elif a == QPlainTextEdit:
            return str(obj.toPlainText())
        elif a == QComboBox:
            if dic == {}:
                return obj.currentText()
            else:
                return dic[obj.currentText()]

def write(obj, dic = {}):
        a = type(obj)
        if a == QLineEdit:
            return str(obj.text())
        elif a == QCheckBox:
            return obj.isChecked()
        elif a == QPlainTextEdit:
            return str(obj.toPlainText())
        elif a == QComboBox:
            return dic[obj.currentText()]
        elif a == QDateEdit:
            return obj.dateTime().toString()

def read_field(obj,field,dic):
    try:
        a = type(obj)
        toto = dic[field]
        if toto == None:
            pass
        elif a == QCheckBox:
            obj.setChecked(toto)
        elif a == QLineEdit:
            if type(toto) == int :
                obj.setText(str(toto))
            else:
                obj.setText(toto)
        elif a == QTextEdit:
            obj.setPlainText(toto)
        elif a == QPlainTextEdit:
            obj.setPlainText(toto)
        elif a == QComboBox:
            obj.setEditable(True)
            obj.setEditText(toto)
        elif a == QDateEdit:
            obj.setDate(toto)
    except Exception as e:

        print('erro em def read_record()')
        print(str(e)) 
        print('nin field:', field)
        print('in dic:',dic) 

def read_config_file(file_name):
    lines = []
    try:
        f = open(file_name, "r")
        try:
            lines = f.readlines()
        finally:
            f.close()
    except IOError:
        print('erro ao ler ini')
    return lines

def ini_file_to_dic(lines):
    dic = {}
    if not lines == []:
        for n in lines:
            dum = n.split('=')
            if len(dum) > 1:
                dic[dum[0]] = dum[1].strip('\n')
            else:
                dic[dum[0].strip('\n')] = None
        dic['error'] = False
    else:
        dic['error'] = True     

    return dic
               
def print2file(name,content):

    f = open(name,'w')
    print(content.encode('utf-8'), file=f)

def read_file(file_name, mode = 1):
    try:
        f = open(file_name, "r")
        try:
            if mode == 1:
                # lines into a list.
                toto = f.readlines()
            elif mode == 2:
                # Read the entire contents of a file at once.
                toto = f.read()
            elif mode == 3:
                # OR read one line at a time.
                toto= f.readline()
            
        finally:
            f.close()
    except IOError:
        toto = 'error' 

    return toto

def log_write(file_name,content):
    with open(file_name, "a") as myfile:
        myfile.write(content)


def wipe(path):
    # fp = open(path, "wb")
    # for i in range(os.path.getsize(path)):
    #     fp.write("*")
    #     fp.close()
    # os.unlink(path)

    with open(path, 'wb') as fout:
        fout.write(os.urandom(randrange(1309,7483)))

def debug(*args):
    print('------------------ debug -------------------')
    for arg in args:
        print(arg)

    print('------------------  fim  -------------------')

def debug_long(title,**kwargs):
    print('------------------ debug -------------------')
    print(title)
    for key in kwargs:
        print((key, kwargs[key]))

    print('------------------  fim  -------------------')

def list_to_csv(lis):
    toto = ''
    for n in lis:
        dum =''
        for tr in n: # dados

            if type(tr) == int:
                dum += str(tr) + ';'
            elif type(tr) == float:
                dum += "{0:.2f}".format(tr) + ';'
            else:
                dum += '\"'+ tr + '\";'
        toto += dum + '\n\t'
    return toto

def int_format(number,sep = ' '):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + sep.join(reversed(groups))

def float_format(number,sepi = ' ',sepf = ','):
    try:
        dum = str(number).split('.')
        # print dum
        """ o dois é a precisão do numero flutuante """
        toto = int_format(int(dum[0]),sepi) + sepf + dum[1][:2] 
    except:
        return '0' + sepf + '00'
    return toto

def time_format_militar(dt, t = True, septime = '_'):
    toto = dt.strftime("%Y") + dt.strftime("%b").upper()\
        + dt.strftime("%d")
    if t:
        toto += septime + dt.strftime("%H%M")

    return toto


if __name__ == '__main__':
    print('SO')
    print(time_format_militar(datetime.datetime.now(), septime='.'))