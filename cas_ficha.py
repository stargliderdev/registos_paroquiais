#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QTabWidget, QCheckBox, QVBoxLayout, QLineEdit, QComboBox, QDateEdit, \
    QWidget, QDialog, QHBoxLayout, QPushButton,  QMessageBox, QPlainTextEdit,QDesktopWidget

import stdio
import libpg
import parameters as pa
import lib_paroquia
import qlib

class Dialog(QDialog):
    def __init__(self, cas_id,  parent = None):
        super(Dialog,  self).__init__(parent)
        self.center()
        self.setWindowTitle('Altera Registo de casamento') 
        self.cas_dic = lib_paroquia.get_casamento(cas_id)
        self.c_box_with = 260
        masterLayout = QHBoxLayout(self)
        mainLayout = QVBoxLayout()

        self.cas_idEdit = QLineEdit()
        self.cas_idEdit.setMaximumWidth(60)

        self.cas_ano = QLineEdit()
        self.cas_ano.setMaximumWidth(60)
        self.cas_registo = QLineEdit()
        self.cas_registo.setMaximumWidth(60)
        self.cas_folha = QLineEdit()
        self.cas_folha.setMaximumWidth(60)
        self.cas_folha.setMaxLength(10)
        self.cas_data = QDateEdit()
        self.cas_data.setDisplayFormat("dd.MM.yyyy")
        mainLayout.addLayout(qlib.addHLayout(['Num:',self.cas_idEdit,'Ano:',self.cas_ano,
            'Registo:',self.cas_registo,'Folha(s):',self.cas_folha,'Data',self.cas_data, True]))

        self.cas_noivo = QLineEdit()
        self.cas_noivo.setMaxLength(50)
        self.cas_noivo.setMaximumWidth(350)

        self.cas_noivo_idade = QLineEdit()
        self.cas_noivo_idade.setMaximumWidth(30)

        self.cas_noivo_estado = QComboBox()
        self.cas_noivo_estado.setEditable(True)
        self.cas_noivo_estado.addItems(pa.dsEstados)
        self.cas_noivo_assinou = QCheckBox()
        mainLayout.addLayout(qlib.addHLayout(['Noivo:',self.cas_noivo,'Idade:',self.cas_noivo_idade,'Estado:',self.cas_noivo_estado,
            'Assinou',self.cas_noivo_assinou,True]))

        self.cas_noivo_naturalidade = QComboBox()
        self.cas_noivo_naturalidade.setEditable(True)
        self.cas_noivo_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_noivo_naturalidade.addItems(pa.dsLocais)
        mainLayout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_noivo_naturalidade, True]))

        self.cas_noivo_residencia = QComboBox()
        self.cas_noivo_residencia.setEditable(True)
        self.cas_noivo_residencia.setMaximumWidth(self.c_box_with)
        self.cas_noivo_residencia.addItems(pa.dsLocais)
        mainLayout.addLayout(qlib.addHLayout(['Residencia:',self.cas_noivo_residencia, True]))
        self.cas_noivo_profissao = QComboBox()
        self.cas_noivo_profissao.setMaximumWidth(self.c_box_with)
        self.cas_noivo_profissao.setEditable(True)
        self.cas_noivo_profissao.addItems(pa.dsProfissoes)
        mainLayout.addLayout(qlib.addHLayout(['Profissão:',self.cas_noivo_profissao, True]))

        self.cas_noiva = QLineEdit()
        self.cas_noiva.setMaxLength(50)
        self.cas_noiva.setMaximumWidth(350)

        self.cas_noiva_idade = QLineEdit()
        self.cas_noiva_idade.setMaximumWidth(30)

        self.cas_noiva_estado = QComboBox()
        self.cas_noiva_estado.setEditable(True)
        self.cas_noiva_estado.addItems(pa.dsEstados)
        self.cas_noiva_assinou = QCheckBox()
        mainLayout.addLayout(qlib.addHLayout(['Noiva:',self.cas_noiva,'Idade:',self.cas_noiva_idade,'Estado:',self.cas_noiva_estado,'Assinou',self.cas_noivo_assinou, True]))
        
        self.cas_noiva_naturalidade = QComboBox()
        self.cas_noiva_naturalidade.setEditable(True)
        self.cas_noiva_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_noiva_naturalidade.addItems(pa.dsLocais)
        mainLayout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_noiva_naturalidade, True]))       
        self.cas_noiva_residencia = QComboBox()
        self.cas_noiva_residencia.setEditable(True)
        self.cas_noiva_residencia.setMaximumWidth(self.c_box_with)
        self.cas_noiva_residencia.addItems(pa.dsLocais)
        mainLayout.addLayout(qlib.addHLayout(['Residencia:',self.cas_noiva_residencia, True]))
        self.cas_noiva_profissao = QComboBox()
        self.cas_noiva_profissao.setMaximumWidth(self.c_box_with)
        self.cas_noiva_profissao.setEditable(True)
        self.cas_noiva_profissao.addItems(pa.dsProfissoes)
        mainLayout.addLayout(qlib.addHLayout(['Profissão:',self.cas_noiva_profissao, True]))

        # cria tabulador
        self.tabuladorTabWidget = QTabWidget() 
        mainLayout.addWidget(self.tabuladorTabWidget)

        self.cas_noivo_pai()
        self.tabuladorTabWidget.addTab(self.tab1, 'Pai do Noivo')
        self.cas_noivo_mae()
        self.tabuladorTabWidget.addTab(self.tab2, 'Mãe do Noivo')
        self.cas_noiva_pai()
        self.tabuladorTabWidget.addTab(self.tab3, 'Pai da Noiva')
        self.cas_noiva_mae()
        self.tabuladorTabWidget.addTab(self.tab4, 'Mãe da Noiva')
        self.cas_t1()
        self.tabuladorTabWidget.addTab(self.tab5, '1ª Testemunha')
        self.cas_t2()
        self.tabuladorTabWidget.addTab(self.tab6, '2ª Testemunha')
        self.cas_t3()
        self.tabuladorTabWidget.addTab(self.tab7, '3ª Testemunha')
        self.cas_t4()
        self.tabuladorTabWidget.addTab(self.tab8, '4ª Testemunha')
        self.cas_t5()
        self.tabuladorTabWidget.addTab(self.tab9, '5ª Testemunha')

        # dumLayout = QHBoxLayout()
        self.cas_padre = QComboBox()
        self.cas_padre.setEditable(True)
        self.cas_padre.addItems(pa.dsPadres)
        self.cas_padre_residencia = QComboBox()
        self.cas_padre_residencia.setEditable(True)
        self.cas_padre_residencia.addItems(pa.dsLocais)
        self.cas_selo = QLineEdit()
        self.cas_selo.setMinimumWidth(60)
        mainLayout.addLayout(qlib.addHLayout(['Padre',self.cas_padre,'Residencia:',self.cas_padre_residencia,'Selos:',self.cas_selo,True]))
        # mainLayout.addLayout(dumLayout)

        # dumLayout = QHBoxLayout()
        self.cas_obs = QPlainTextEdit()
        # self.cas_obs.setMaximumHeight(100)
        mainLayout.addLayout(qlib.addVLayout(['Observações:',self.cas_obs]))
        #
        self.saveBtn = QPushButton('Guarda')
        # self.connect(self.saveBtn, SIGNAL("clicked()"), self.save_btn_click)

        self.save_and_closeBtn = QPushButton('Guarda e Sai')
        # self.connect(self.save_and_closeBtn, SIGNAL("clicked()"), self.save_and_close_btn_click)
         
        self.cancelBtn = QPushButton('Sair sem Guardar')
        # self.connect(self.cancelBtn, SIGNAL("clicked()"), self.cancel_btn_click)

        mainLayout.addLayout(qlib.addHLayout([self.saveBtn,self.save_and_closeBtn,self.cancelBtn]))
        masterLayout.addLayout(mainLayout)
        self.resize(1024, 800)
        self.refresh_form()

    def cas_noivo_pai(self):
        # cria pagina
        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)
   
        self.cas_noivo_pai = QLineEdit()
        self.cas_noivo_pai.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Pai do Noivo:',self.cas_noivo_pai, True]))

        self.cas_noivo_pai_profissao = QComboBox()
        self.cas_noivo_pai_profissao.setMaximumWidth(self.c_box_with)
        self.cas_noivo_pai_profissao.setEditable(True)
        self.cas_noivo_pai_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão:',self.cas_noivo_pai_profissao, True]))

        self.cas_noivo_pai_naturalidade = QComboBox()
        self.cas_noivo_pai_naturalidade.setEditable(True)
        self.cas_noivo_pai_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_noivo_pai_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_noivo_pai_naturalidade, True]))

        self.cas_noivo_pai_residencia = QComboBox()
        self.cas_noivo_pai_residencia.setEditable(True)
        self.cas_noivo_pai_residencia.setMaximumWidth(self.c_box_with)
        self.cas_noivo_pai_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_noivo_pai_residencia, True]))
        self.cas_noivo_pai_falecido = QCheckBox()
        tab1Layout.addLayout(qlib.addHLayout(['Falecido:',self.cas_noivo_pai_falecido, True]))

        # fecha a pagina
        self.tabuladorTabWidget.addTab(self.tab1, 'Pai do Noivo')

        # nova pagina
    def cas_noivo_mae(self):
        self.tab2 = QWidget()
        tab1Layout = QVBoxLayout(self.tab2)

        self.cas_noivo_mae = QLineEdit()
        self.cas_noivo_mae.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Mãe da Noivo:',self.cas_noivo_mae]))

        self.cas_noivo_mae_profissao = QComboBox()
        self.cas_noivo_mae_profissao.setEditable(True)
        self.cas_noivo_mae_profissao.setMaximumWidth(self.c_box_with)
        self.cas_noivo_mae_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão:',self.cas_noivo_mae_profissao, True]))

        self.cas_noivo_mae_naturalidade = QComboBox()
        self.cas_noivo_mae_naturalidade.setEditable(True)
        self.cas_noivo_mae_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_noivo_mae_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_noivo_mae_naturalidade, True]))

        self.cas_noivo_mae_residencia = QComboBox()
        self.cas_noivo_mae_residencia.setEditable(True)
        self.cas_noivo_mae_residencia.setMaximumWidth(self.c_box_with)
        self.cas_noivo_mae_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_noivo_mae_residencia, True]))
        self.cas_noivo_mae_falecido = QCheckBox()
        tab1Layout.addLayout(qlib.addHLayout(['Falecida:',self.cas_noivo_mae_falecido, True]))

        # fecha pagina
        # self.tabuladorTabWidget.addTab(self.tab1, u'Mãe do Noivo')
    def cas_noiva_pai(self):
        self.tab3 = QWidget()
        tab1Layout = QVBoxLayout(self.tab3)

        self.cas_noiva_pai = QLineEdit()
        self.cas_noiva_pai.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Pai da Noiva',self.cas_noiva_pai]))

        self.cas_noiva_pai_profissao = QComboBox()
        self.cas_noiva_pai_profissao.setEditable(True)
        self.cas_noiva_pai_profissao.setMaximumWidth(self.c_box_with)
        self.cas_noiva_pai_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão:',self.cas_noiva_pai_profissao, True]))

        self.cas_noiva_pai_naturalidade = QComboBox()
        self.cas_noiva_pai_naturalidade.setEditable(True)
        self.cas_noiva_pai_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_noiva_pai_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_noiva_pai_naturalidade, True]))

        self.cas_noiva_pai_residencia = QComboBox()
        self.cas_noiva_pai_residencia.setEditable(True)
        self.cas_noiva_pai_residencia.setMaximumWidth(self.c_box_with)
        self.cas_noiva_pai_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia',self.cas_noiva_pai_residencia, True]))
        self.cas_noiva_pai_falecido = QCheckBox()
        tab1Layout.addLayout(qlib.addHLayout(['Falecido:',self.cas_noiva_pai_falecido, True]))
        # self.tabuladorTabWidget.addTab(self.tab1, u'Pai da Noiva')
    def cas_noiva_mae(self):

        self.tab4 = QWidget()
        tab1Layout = QVBoxLayout(self.tab4)

        self.cas_noiva_mae = QLineEdit()
        self.cas_noiva_mae.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Mãe da Noiva:',self.cas_noiva_mae]))

        self.cas_noiva_mae_profissao = QComboBox()
        self.cas_noiva_mae_profissao.setEditable(True)
        self.cas_noiva_mae_profissao.setMaximumWidth(self.c_box_with)
        self.cas_noiva_mae_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão:',self.cas_noiva_mae_profissao, True]))

        self.cas_noiva_mae_naturalidade = QComboBox()
        self.cas_noiva_mae_naturalidade.setEditable(True)
        self.cas_noiva_mae_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_noiva_mae_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_noiva_mae_naturalidade, True]))

        self.cas_noiva_mae_residencia = QComboBox()
        self.cas_noiva_mae_residencia.setEditable(True)
        self.cas_noiva_mae_residencia.setMaximumWidth(self.c_box_with)
        self.cas_noiva_mae_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_noiva_mae_residencia, True]))
        self.cas_noiva_mae_falecido = QCheckBox()
        tab1Layout.addLayout(qlib.addHLayout(['Falecido:',self.cas_noiva_mae_falecido, True]))


    def cas_t1(self):
        self.tab5 = QWidget()
        tab1Layout = QVBoxLayout(self.tab5)

        # dumLayout = QHBoxLayout()
        self.cas_t1 = QLineEdit()
        self.cas_t1.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Nome:',self.cas_t1]))
        self.cas_t1_profissao = QComboBox()
        self.cas_t1_profissao.setEditable(True)
        self.cas_t1_profissao.setMaximumWidth(self.c_box_with)
        self.cas_t1_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão',self.cas_t1_profissao, True]))

        # dumLayout = QHBoxLayout()
        self.cas_t1_residencia = QComboBox()
        self.cas_t1_residencia.setEditable(True)
        self.cas_t1_residencia.setMaximumWidth(self.c_box_with)    
        self.cas_t1_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_t1_residencia, True]))

        self.cas_t1_naturalidade = QComboBox()
        self.cas_t1_naturalidade.setEditable(True)
        self.cas_t1_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_t1_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_t1_naturalidade, True]))

        # dumLayout = QHBoxLayout()
        self.cas_t1_estado = QComboBox()
        self.cas_t1_estado.setEditable(True)
        self.cas_t1_estado.setMaximumWidth(self.c_box_with)
        self.cas_t1_estado.addItems(pa.dsEstados)
        self.cas_t1_assinou = QCheckBox()
        tab1Layout.addLayout(qlib.addHLayout(['Estado:',self.cas_t1_estado,'Assinou:', self.cas_t1_assinou, True]))

    def cas_t2(self):
        self.tab6 = QWidget()
        tab1Layout = QVBoxLayout(self.tab6)
        self.cas_t2 = QLineEdit()
        self.cas_t2.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Nome:',self.cas_t2]))

        self.cas_t2_profissao = QComboBox()
        self.cas_t2_profissao.setEditable(True)
        self.cas_t2_profissao.setMaximumWidth(self.c_box_with)
        self.cas_t2_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão',self.cas_t2_profissao, True]))

        self.cas_t2_residencia = QComboBox()
        self.cas_t2_residencia.setEditable(True)
        self.cas_t2_residencia.setMaximumWidth(self.c_box_with)
        self.cas_t2_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_t2_residencia, True]))
        self.cas_t2_naturalidade = QComboBox()
        self.cas_t2_naturalidade.setEditable(True)
        self.cas_t2_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_t2_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_t2_naturalidade, True]))

        self.cas_t2_estado = QComboBox()
        self.cas_t2_estado.setEditable(True)
        self.cas_t2_estado.setMaximumWidth(self.c_box_with)
        self.cas_t2_estado.addItems(pa.dsEstados)
        self.cas_t2_assinou = QCheckBox()

        tab1Layout.addLayout(qlib.addHLayout(['Estado:',self.cas_t2_estado, True]))


    def cas_t3(self):
        self.tab7 = QWidget()
        tab1Layout = QVBoxLayout(self.tab7)

        dumLayout = QHBoxLayout()
        self.cas_t3 = QLineEdit()
        self.cas_t3.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Nome:',self.cas_t3]))
        
        self.cas_t3_profissao = QComboBox()
        self.cas_t3_profissao.setEditable(True)
        self.cas_t3_profissao.setMaximumWidth(self.c_box_with)
        self.cas_t3_profissao.addItems(pa.dsProfissoes)
        
        dumLayout = QHBoxLayout()
        self.cas_t3_residencia = QComboBox()
        self.cas_t3_residencia.setEditable(True)
        self.cas_t3_residencia.setMaximumWidth(self.c_box_with)
        self.cas_t3_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_t3_residencia, True]))
        self.cas_t3_naturalidade = QComboBox()
        self.cas_t3_naturalidade.setEditable(True)
        self.cas_t3_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_t3_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_t3_naturalidade, True]))
        dumLayout = QHBoxLayout()
        self.cas_t3_estado = QComboBox()
        self.cas_t3_estado.setEditable(True)
        self.cas_t3_estado.setMaximumWidth(self.c_box_with)
        self.cas_t3_estado.addItems(pa.dsEstados)
        self.cas_t3_assinou = QCheckBox()
        
        tab1Layout.addLayout(qlib.addHLayout(['Estado:',self.cas_t3_estado, True]))
        
    def cas_t4(self):
        self.tab8 = QWidget()
        tab1Layout = QVBoxLayout(self.tab8)

        self.cas_t4 = QLineEdit()
        self.cas_t4.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Testemunha:',self.cas_t4]))

        self.cas_t4_profissao = QComboBox()
        self.cas_t4_profissao.setEditable(True)
        self.cas_t4_profissao.setMaximumWidth(self.c_box_with)
        self.cas_t4_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão',self.cas_t4_profissao, True]))

        self.cas_t4_residencia = QComboBox()
        self.cas_t4_residencia.setEditable(True)
        self.cas_t4_residencia.setMaximumWidth(self.c_box_with)
        self.cas_t4_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_t4_residencia, True]))
        self.cas_t4_naturalidade = QComboBox()
        self.cas_t4_naturalidade.setEditable(True)
        self.cas_t4_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_t4_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_t4_naturalidade, True]))
        self.cas_t4_estado = QComboBox()
        self.cas_t4_estado.setEditable(True)
        self.cas_t4_estado.setMaximumWidth(self.c_box_with)
        self.cas_t4_estado.addItems(pa.dsEstados)
        self.cas_t4_assinou = QCheckBox()
        
        tab1Layout.addLayout(qlib.addHLayout(['Estado:',self.cas_t4_estado, True]))


    def cas_t5(self):
        self.tab9 = QWidget()
        tab1Layout = QVBoxLayout(self.tab9)
        
        self.cas_t5 = QLineEdit()
        self.cas_t5.setMaxLength(50)
        tab1Layout.addLayout(qlib.addHLayout(['Nome:',self.cas_t5]))
        
        self.cas_t5_profissao = QComboBox()
        self.cas_t5_profissao.setEditable(True)
        self.cas_t5_profissao.setMaximumWidth(self.c_box_with)
        self.cas_t5_profissao.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(qlib.addHLayout(['Profissão',self.cas_t5_profissao, True]))
                
        self.cas_t5_residencia = QComboBox()
        self.cas_t5_residencia.setEditable(True)
        self.cas_t5_residencia.setMaximumWidth(self.c_box_with)
        self.cas_t5_residencia.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Residencia:',self.cas_t5_residencia, True]))
        self.cas_t5_naturalidade = QComboBox()
        self.cas_t5_naturalidade.setEditable(True)
        self.cas_t5_naturalidade.setMaximumWidth(self.c_box_with)
        self.cas_t5_naturalidade.addItems(pa.dsLocais)
        tab1Layout.addLayout(qlib.addHLayout(['Naturalidade:',self.cas_t5_naturalidade, True]))

        self.cas_t5_estado = QComboBox()
        self.cas_t5_estado.setEditable(True)
        self.cas_t5_estado.setMaximumWidth(self.c_box_with)
        self.cas_t5_estado.addItems(pa.dsEstados)
        self.cas_t5_assinou = QCheckBox()
        
        tab1Layout.addLayout(qlib.addHLayout(['Estado:',self.cas_t5_estado, True]))
        
    def forward_click(self):
        if pa.current_index < pa.current_dataset_limit:
            pa.current_index +=1
            pa.current_record = pa.current_dataset[pa.current_index]
            self.cas_dic = get_cascimentos_data(pa.current_dataset[pa.current_index])
            self.refresh_form()
        else:
            self.forwardBtn.setEnabled(False)
            self.backwardBtn.setEnabled(True)

    def backward_click(self):
        if pa.current_index > 0:
            pa.current_index -=1
            pa.current_record = pa.current_dataset[pa.current_index]
            self.cas_dic = get_cascimentos_data(pa.current_dataset[pa.current_index])
            self.refresh_form()
        else:
            self.forwardBtn.setEnabled(True)
            self.backwardBtn.setEnabled(False)
        

    def save_btn_click(self):
        ## pa.obitos_rec
        if self.check_fields_locais():
            if self.check_fields_profissaoissoes():
                if self.check_fields_padres():
                    self.save_record()
    def save_and_close_btn_click(self):
        if self.check_fields_locais():
            if self.check_fields_profissaoissoes():
                if self.check_fields_padres():
                    self.save_record()
                    self.close()

    def cancel_btn_click(self):
        self.close()

    def check_fields_locais(self):
        # 'check_fields_locais'
        for n in self.cas_pai_naturalidade, self.cas_pai_residencia, self.cas_mae_naturalidade, self.cas_mae_residencia, self.cas_avo_paterno_naturalidade,\
                self.cas_avo_paterno_residencia, self.cas_noivo_mae_naturalidade, self.cas_noivo_mae_residencia, self.cas_noiva_pai_naturalidade, self.cas_noiva_pai_residencia,\
                self.cas_noiva_mae_naturalidade, self.cas_noiva_mae_residencia, self.cas_padrinho_residencia, self.cas_madrinha_residencia, self.cas_t1_residencia,\
                self.cas_t2_residencia, self.cas_t3_residencia, self.cas_t4_residencia, self.cas_t5_residencia, self.cas_padre_residencia:
            toto = str(n.currentText())
            if toto not in pa.locais_dict :
                # # 'não existe',n.currentText()
                if self.askForNew('Adiciona Locais','Adicionar este Local?', toto):
                    # # 'addciona local'
                    libpg.add_record_to_table('locais', 'local',toto)
                    # # 'refresca dicionarios'
                    lib_paroquia.get_locais()
                    toto = True
                else:
                    # 'toto = False'
                    toto = False
                    break
            else:
                toto = True
        return toto
    def check_fields_profissaoissoes(self):
        # # 'check_fields_profissaoissoes'
        for n in self.cas_pai_profissao, self.cas_mae_profissao, self.cas_avo_paterno_profissao, self.cas_noivo_mae_profissao, self.cas_noiva_pai_profissao,\
            self.cas_noiva_mae_profissao, self.cas_padrinho_profissao, self.cas_madrinha_profissao, self.cas_t1_profissao, self.cas_t2_profissao,\
            self.cas_t3_profissao, self.cas_t4_profissao, self.cas_t5_profissao:

            toto = str(n.currentText())
            if toto not in pa.profissoes_dict :
                # # 'não existe',n.currentText()
                if self.askForNew('Adiciona Profissão','Adicionar esta Profissão?', toto):
                    # # 'addciona local'
                    libpg.add_record_to_table('profissoes', 'prof',toto)
                    # # 'refresca dicionarios'
                    lib_paroquia.get_profissaoissoes()
                    toto = True
                else:
                    # # 'toto = False'
                    toto = False
                    break
            else:
                toto = True
        return toto 
    
    def check_fields_padres(self):
        # # 'check_fields_padres'

        toto = str(self.cas_padre.currentText())
        if toto not in pa.padres_dict :
            # # 'não existe',n.currentText()
            if self.askForNew('Adiciona Paroco','Adicionar este Paroco?', toto):
                # # 'addciona local'
                libpg.add_record_to_table('padres', 'pa_nome',toto)
                # # 'refresca dicionarios'
                lib_paroquia.get_padres()
                toto = True
            else:
                # # 'toto = False'
                toto = False
        else:
            toto = True
        return toto

    def refresh_form(self):
        # stdio.read_field(self.cas_data_cascimento,'cas_data_cascimento',self.cas_dic)
        # stdio.read_field(self.cas_local,'cas_local',self.cas_dic)
        stdio.read_field(self.cas_idEdit,'cas_id',self.cas_dic)
        stdio.read_field(self.cas_ano,'cas_ano',self.cas_dic)
        stdio.read_field(self.cas_registo,'cas_registo',self.cas_dic)
        stdio.read_field(self.cas_folha,'cas_folha',self.cas_dic)
        stdio.read_field(self.cas_data,'cas_data',self.cas_dic)
        stdio.read_field(self.cas_noivo,'cas_noivo',self.cas_dic)
        stdio.read_field(self.cas_noivo_idade,'cas_noivo_idade',self.cas_dic)
        stdio.read_field(self.cas_noivo_estado,'cas_noivo_estado',self.cas_dic)
        stdio.read_field(self.cas_noivo_profissao,'cas_noivo_profissao',self.cas_dic)
        stdio.read_field(self.cas_noivo_residencia,'cas_noivo_residencia',self.cas_dic)
        stdio.read_field(self.cas_noivo_naturalidade,'cas_noivo_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_noivo_assinou,'cas_noivo_assinou',self.cas_dic)
        stdio.read_field(self.cas_noiva,'cas_noiva',self.cas_dic)
        stdio.read_field(self.cas_noiva_idade,'cas_noiva_idade',self.cas_dic)
        stdio.read_field(self.cas_noiva_estado,'cas_noiva_estado',self.cas_dic)
        stdio.read_field(self.cas_noiva_profissao,'cas_noiva_profissao',self.cas_dic)
        stdio.read_field(self.cas_noiva_naturalidade,'cas_noiva_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_noiva_residencia,'cas_noiva_residencia',self.cas_dic)
        stdio.read_field(self.cas_noiva_assinou,'cas_noiva_assinou',self.cas_dic)
        stdio.read_field(self.cas_noivo_pai,'cas_noivo_pai',self.cas_dic)
        stdio.read_field(self.cas_noivo_pai_profissao,'cas_noivo_pai_profissao',self.cas_dic)
        stdio.read_field(self.cas_noivo_pai_naturalidade,'cas_noivo_pai_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_noivo_pai_residencia,'cas_noivo_pai_residencia',self.cas_dic)
        stdio.read_field(self.cas_noivo_pai_falecido,'cas_noivo_pai_falecido',self.cas_dic)
        stdio.read_field(self.cas_noivo_mae,'cas_noivo_mae',self.cas_dic)
        stdio.read_field(self.cas_noivo_mae_profissao,'cas_noivo_mae_profissao',self.cas_dic)
        stdio.read_field(self.cas_noivo_mae_naturalidade,'cas_noivo_mae_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_noivo_mae_residencia,'cas_noivo_mae_residencia',self.cas_dic)
        stdio.read_field(self.cas_noivo_mae_falecido,'cas_noivo_mae_falecido',self.cas_dic)
        stdio.read_field(self.cas_noiva_pai,'cas_noiva_pai',self.cas_dic)
        stdio.read_field(self.cas_noiva_pai_profissao,'cas_noiva_pai_profissao',self.cas_dic)
        stdio.read_field(self.cas_noiva_pai_naturalidade,'cas_noiva_pai_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_noiva_pai_residencia,'cas_noiva_pai_residencia',self.cas_dic)
        stdio.read_field(self.cas_noiva_pai_falecido,'cas_noiva_pai_falecido',self.cas_dic)
        stdio.read_field(self.cas_noiva_mae,'cas_noiva_mae',self.cas_dic)
        stdio.read_field(self.cas_noiva_mae_profissao,'cas_noiva_mae_profissao',self.cas_dic)
        stdio.read_field(self.cas_noiva_mae_naturalidade,'cas_noiva_mae_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_noiva_mae_residencia,'cas_noiva_mae_residencia',self.cas_dic)
        stdio.read_field(self.cas_noiva_mae_falecido,'cas_noiva_mae_falecido',self.cas_dic)
        stdio.read_field(self.cas_t1,'cas_t1',self.cas_dic)
        stdio.read_field(self.cas_t1_estado,'cas_t1_estado',self.cas_dic)
        stdio.read_field(self.cas_t1_profissao,'cas_t1_profissao',self.cas_dic)
        stdio.read_field(self.cas_t1_naturalidade,'cas_t1_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_t1_residencia,'cas_t1_residencia',self.cas_dic)
        stdio.read_field(self.cas_t1_assinou,'cas_t1_assinou',self.cas_dic)
        stdio.read_field(self.cas_t2,'cas_t2',self.cas_dic)
        stdio.read_field(self.cas_t2_estado,'cas_t2_estado',self.cas_dic)
        stdio.read_field(self.cas_t2_profissao,'cas_t2_profissao',self.cas_dic)
        stdio.read_field(self.cas_t2_naturalidade,'cas_t2_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_t2_residencia,'cas_t2_residencia',self.cas_dic)
        stdio.read_field(self.cas_t2_assinou,'cas_t2_assinou',self.cas_dic)
        stdio.read_field(self.cas_t3,'cas_t3',self.cas_dic)
        stdio.read_field(self.cas_t3_estado,'cas_t3_estado',self.cas_dic)
        stdio.read_field(self.cas_t3_profissao,'cas_t3_profissao',self.cas_dic)
        stdio.read_field(self.cas_t3_naturalidade,'cas_t3_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_t3_residencia,'cas_t3_residencia',self.cas_dic)
        stdio.read_field(self.cas_t3_assinou,'cas_t3_assinou',self.cas_dic)
        stdio.read_field(self.cas_t4,'cas_t4',self.cas_dic)
        stdio.read_field(self.cas_t4_estado,'cas_t4_estado',self.cas_dic)
        stdio.read_field(self.cas_t4_profissao,'cas_t4_profissao',self.cas_dic)
        stdio.read_field(self.cas_t4_naturalidade,'cas_t4_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_t4_residencia,'cas_t4_residencia',self.cas_dic)
        stdio.read_field(self.cas_t4_assinou,'cas_t4_assinou',self.cas_dic)
        stdio.read_field(self.cas_t5,'cas_t5',self.cas_dic)
        stdio.read_field(self.cas_t5_estado,'cas_t5_estado',self.cas_dic)
        stdio.read_field(self.cas_t5_profissao,'cas_t5_profissao',self.cas_dic)
        stdio.read_field(self.cas_t5_naturalidade,'cas_t5_naturalidade',self.cas_dic)
        stdio.read_field(self.cas_t5_residencia,'cas_t5_residencia',self.cas_dic)
        stdio.read_field(self.cas_t5_assinou,'cas_t5_assinou',self.cas_dic)
        stdio.read_field(self.cas_selo,'cas_selo',self.cas_dic)
        stdio.read_field(self.cas_padre,'cas_padre',self.cas_dic)
        stdio.read_field(self.cas_obs,'cas_obs',self.cas_dic)
        
    def save_record(self):
        # cas_local=%s,\
        # data += (stdio.write_record(self.cas_local,pa.locais_dict),)
        sql = 'UPDATE cascimentos set\
        cas_ano=%s,\
        cas_registo=%s,\
        cas_folha=%s,\
        cas_data=%s,\
        cas_data_baptismo=%s,\
        cas_nome=%s,\
        cas_numero_filho=%s,\
        cas_sexo=%s,\
        cas_pais_casados=%s,\
        cas_pai=%s,\
        cas_pai_idade=%s,\
        cas_pai_estado=%s,\
        cas_pai_naturalidade=%s,\
        cas_pai_residencia=%s,\
        cas_pai_profissao=%s,\
        cas_mae=%s,\
        cas_mae_naturalidade=%s,\
        cas_mae_residencia=%s,\
        cas_mae_profissao=%s,\
        cas_avo_paterno=%s,\
        cas_avo_paterno_profissao=%s,\
        cas_avo_paterno_naturalidade=%s,\
        cas_avo_paterno_residencia=%s,\
        cas_noivo_mae=%s,\
        cas_noivo_mae_profissao=%s,\
        cas_noivo_mae_naturalidade=%s,\
        cas_noivo_mae_residencia=%s,\
        cas_noiva_pai=%s,\
        cas_noiva_pai_profissao=%s,\
        cas_noiva_pai_naturalidade=%s,\
        cas_noiva_pai_residencia=%s,\
        cas_noiva_mae=%s,\
        cas_noiva_mae_profissao=%s,\
        cas_noiva_mae_naturalidade=%s,\
        cas_noiva_mae_residencia=%s,\
        cas_padrinho=%s,\
        cas_padrinho_estado=%s,\
        cas_padrinho_profissao=%s,\
        cas_padrinho_residencia=%s,\
        cas_padrinho_assinou=%s,\
        cas_madrinha=%s,\
        cas_madrinha_estado=%s,\
        cas_madrinha_profissao=%s,\
        cas_madrinha_residencia=%s,\
        cas_madrinha_assinou=%s,\
        cas_t1=%s,\
        cas_t1_profissao=%s,\
        cas_t1_residencia=%s,\
        cas_t1_estado=%s,\
        cas_t2=%s,\
        cas_t2_profissao=%s,\
        cas_t2_residencia=%s,\
        cas_t2_estado=%s,\
        cas_t3=%s,\
        cas_t3_profissao=%s,\
        cas_t3_residencia=%s,\
        cas_t3_estado=%s,\
        cas_t4=%s,\
        cas_t4_profissao=%s,\
        cas_t4_residencia=%s,\
        cas_t4_estado=%s,\
        cas_t5=%s,\
        cas_t5_profissao=%s,\
        cas_t5_residencia=%s,\
        cas_t5_estado=%s,\
        cas_padre=%s,\
        cas_padre_residencia=%s,\
        cas_selos=%s,\
        cas_obs=%s,\
        cas_mae_idade=%s,\
        cas_mae_estado=%s\
         WHERE cas_id= %s'
        data = ()
        data += (stdio.write_record(self.cas_ano),)
        data += (stdio.write_record(self.cas_registo),)
        data += (stdio.write_record(self.cas_folha),)
        data += (stdio.write_record(self.cas_data),)
        data += (stdio.write_record(self.cas_data_baptismo),)
        data += (stdio.write_record(self.cas_nome),)
        data += (stdio.write_record(self.cas_numero_filho),)
        data += (stdio.write_record(self.cas_sexo,pa.sexo_dict),)
        data += (stdio.write_record(self.cas_pais_casados),)
        data += (stdio.write_record(self.cas_pai),)
        data += (stdio.write_record(self.cas_pai_idade),)
        data += (stdio.write_record(self.cas_pai_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_pai_naturalidade,pa.locais_dict),)
        data += (stdio.write_record(self.cas_pai_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_pai_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_mae),)
        data += (stdio.write_record(self.cas_mae_naturalidade,pa.locais_dict),)
        data += (stdio.write_record(self.cas_mae_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_mae_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_avo_paterno),)
        data += (stdio.write_record(self.cas_avo_paterno_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_avo_paterno_naturalidade,pa.locais_dict),)
        data += (stdio.write_record(self.cas_avo_paterno_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_noivo_mae),)
        data += (stdio.write_record(self.cas_noivo_mae_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_noivo_mae_naturalidade,pa.locais_dict),)
        data += (stdio.write_record(self.cas_noivo_mae_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_noiva_pai),)
        data += (stdio.write_record(self.cas_noiva_pai_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_noiva_pai_naturalidade,pa.locais_dict),)
        data += (stdio.write_record(self.cas_noiva_pai_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_noiva_mae),)
        data += (stdio.write_record(self.cas_noiva_mae_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_noiva_mae_naturalidade,pa.locais_dict),)
        data += (stdio.write_record(self.cas_noiva_mae_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_padrinho),)
        data += (stdio.write_record(self.cas_padrinho_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_padrinho_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_padrinho_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_padrinho_assinou),)
        data += (stdio.write_record(self.cas_madrinha),)
        data += (stdio.write_record(self.cas_madrinha_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_madrinha_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_madrinha_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_madrinha_assinou),)
        data += (stdio.write_record(self.cas_t1),)
        data += (stdio.write_record(self.cas_t1_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_t1_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_t1_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_t2),)
        data += (stdio.write_record(self.cas_t2_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_t2_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_t2_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_t3),)
        data += (stdio.write_record(self.cas_t3_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_t3_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_t3_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_t4),)
        data += (stdio.write_record(self.cas_t4_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_t4_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_t4_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_t5),)
        data += (stdio.write_record(self.cas_t5_profissao,pa.profissoes_dict),)
        data += (stdio.write_record(self.cas_t5_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_t5_estado,pa.estados_dict),)
        data += (stdio.write_record(self.cas_padre,pa.padres_dict),)
        data += (stdio.write_record(self.cas_padre_residencia,pa.locais_dict),)
        data += (stdio.write_record(self.cas_selo),)
        data += (stdio.write_record(self.cas_obs),
        stdio.write_record(self.cas_mae_idade),
        stdio.write_record(self.cas_mae_estado,pa.estados_dict), pa.current_record)
        libpg.execute_query(sql,data)



    # def make_write_sql(self,table, fields, index):
    #     toto = ''
    #     toto += 'sql = \'UPDATE ' + table + ' set \\\n'
    #     for n in fields:
    #         if len(n) == 2:
    #             toto += n[1] + '=%s, \\\n'
    #         else:
    #             toto += n[1] + '=%s, \\\n'
    # 
    #     toto += 'where id = %s ' + str(index)
    #     toto += 'data = ()'
    #     for n in fields:
    #         if len(n) == 2:
    #             toto += 'data += (write_record(self.' + n[1] + ') \n'
    #         else:
    #             toto += 'data += (write_record(\n'
    # 
    #     toto += '\''
    #     stdio.print2file('update_sql.py',unicode(toto))

    def askForNew(self, caption, prefix, text):
        if QMessageBox.information(None,
                self.trUtf8("" + str(caption) + ""),
                self.trUtf8("" + str(prefix)+'\n' +str(text)+""),
                QMessageBox.StandardButtons(\
                    QMessageBox.Cancel),
                QMessageBox.Ok) == QMessageBox.Ok:
            return True
        else:
            return False


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 
    # def setSizes(self, object,w,h):       
    #     object.setMaximumHeight (h)
    #     object.setMinimumHeight(h)
    #     object.setMaximumWidth(w)
    #     object.setMinimumWidth(w)

    # def setSizeWidth(self, object, value):
    #     object.setMaximumWidth(value)
    #     object.setMinimumWidth(value)
    # 
    # def setBtnSquare(self, object,value=60):       
    #     object.setMaximumHeight (value)
    #     object.setMinimumHeight(value)
    #     object.setMaximumWidth(value)
    #     object.setMinimumWidth(value)

    # 
    # def check_obj(self, obj):
    #     if type(obj) == QLineEdit:
    #         if obj.text().isEmpty():
    #             return False
    #         else:
    #             return True
    #     if type(obj) == QPlainTextEdit:
    #         if obj.toPlainText().isEmpty():
    #             return False
    #         else:
    #             return True

def main():
    app = QApplication(sys.argv)
    form = Dialog(4)
    form.show()
    app.exec_()

if __name__ == '__main__':
    import settings
    pa.config = settings.ini_file_to_dic(settings.read_config_file('config.ini'))
    pa.conn_string = "host=" + pa.config['host'] + " dbname=" + pa.config['dbname'] + " user=root password=masterkey"
    #pa.conn_string = "host=192.168.0.98 dbname=registos_paroquiais_sandbox user=root password=masterkey"
    pa.dsSexo = ['Masculino','Feminino']
    pa.sexo_dict = {'Masculino':1,'Feminino':2}

    lib_paroquia.get_estados()
    lib_paroquia.get_locais()
    lib_paroquia.get_profissoes()
    lib_paroquia.get_padres()
    lib_paroquia.get_causas()
    pa.current_index = 450
    # self.cas_dic = get_cascimentos_data(pa.current_index)
    main()
