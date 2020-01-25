#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit,QDialog, QHBoxLayout,QPushButton, QMessageBox
from PyQt5.Qt import Qt

import parameters as pa
import libpg

class NewRecord(QDialog):
    def __init__(self,  parent = None):
        super(NewRecord,  self).__init__(parent)
        #self.resize(1024, 768)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.WindowTitleHint)
        self.setWindowTitle('Adiciona Acento')
        masterLayout = QVBoxLayout(self)

        """ single layout """
        dumLayout = QHBoxLayout()
        self.nas_ano = QLineEdit()
        self.nas_ano.setMaxLength(4)
        self.nas_ano.setText(str(pa.last_year))
        self.nas_ano.setInputMask('0000')
        dumLayout.addLayout(self.addHDumLayout(['Ano', self.nas_ano]))
        masterLayout.addLayout(dumLayout)
        """ single layout """
        dumLayout = QHBoxLayout()
        self.nas_registo = QLineEdit()
        self.nas_registo.setMaxLength(4)
        self.nas_registo.setInputMask('0000')
        dumLayout.addLayout(self.addHDumLayout(['Registo:', self.nas_registo]))
        masterLayout.addLayout(dumLayout)
        """ single layout """
        dumLayout = QHBoxLayout()
        self.nas_folha = QLineEdit()
        self.nas_folha.setMaxLength(10)
        dumLayout.addLayout(self.addHDumLayout(['Folha(s):', self.nas_folha]))
        masterLayout.addLayout(dumLayout)

        self.saveBtn = QPushButton('Cria Registo')
        # self.connect(self.saveBtn, SIGNAL("clicked()"), self.save_btn_click)
        self.saveBtn.clicked.connect(self.save_btn_click)
        
         
        self.cancelBtn = QPushButton('Cancela')
        # self.connect(self.cancelBtn, SIGNAL("clicked()"), self.cancel_btn_click)
        self.cancelBtn.clicked.connect(self.cancel_btn_click)
        
        masterLayout.addLayout(self.addHDumLayout([self.saveBtn,self.cancelBtn]))
        
    def save_btn_click(self):
        asrec = libpg.output_query_one('select nas_id from nascimentos '
                                       'where nas_ano=%s and nas_registo = %s',
            (int(self.nas_ano.text()), int(self.nas_registo.text())))
        if asrec == None:
            self.toto = {'ano':int(self.nas_ano.text()),'reg':int(self.nas_registo.text()),'folha':str(self.nas_folha.text())}
            self.close()
        else:
            QMessageBox.warning(None,
                self.trUtf8("Registo Duplicado"),
                self.trUtf8("""Já existe um registo com este numero e neste Ano."""),
                QMessageBox.StandardButtons(\
                QMessageBox.Ok))

    def cancel_btn_click(self):
        self.toto = {'ano': -1}
        self.close()


    # def refresh_form(self):
    #     read_field(self.nas_ano,'nas_ano',dict_)
    #     read_field(self.nas_registo,'nas_registo',dict_)
    #     read_field(self.nas_folha,'nas_folha',dict_)
    
    # def insert_record(self):
    #     sql = 'insert into table(nas_ano,nas_folha,nas_registo,\
    #     ) VALUES (%s,%s,%s,%s)'
    #     data = ()
    #     data += (write_record(self.nas_ano),)
    #     data += (write_record(self.nas_folha),)
    #     data += (write_record(self.nas_registo),)
    #     if not pa.last_year in pa.nascimentos_anos:
    #         pa.last_year = int(self.nas_ano)
    #         pa.nascimentos_anos.append(int(self.nas_ano))

    def addHDumLayout(self, listobj1, label_size = 70, align = Qt.AlignRight):
        """ v 2.0 SET2012"""  
        dumLayout = QHBoxLayout()
        for n in listobj1:
            if (type(n)==str) or (type(n) == str):
                toto = QLabel(n)
                toto.setMinimumWidth(label_size)
                toto.setMaximumWidth(label_size)
                toto.setAlignment(align)
                dumLayout.addWidget(toto)
            elif type(n) == bool:
                dumLayout.addStretch()
            else:
                dumLayout.addWidget(n)
        return dumLayout

    def addVDumLayout(self, listobj1, label_size = 120, align = Qt.AlignVCenter|Qt.AlignRight):  
        """ v 2.0 SET2012"""  
        dumLayout = QVBoxLayout()
        for n in listobj1:        
            if (type(n)==str) or (type(n) == str):
                toto = QLabel(n)
                toto.setMinimumWidth(label_size)
                toto.setMaximumWidth(label_size)
                toto.setAlignment(align)
                dumLayout.addWidget(toto)
            elif type(n) == bool:
                dumLayout.addStretch()
            else:

                dumLayout.addWidget(n)
        return dumLayout

if __name__ == '__main__':
    pass

