#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTabWidget, QLabel, QCheckBox, QVBoxLayout, QLineEdit, QComboBox, QDateEdit, \
    QWidget, QDialog, QHBoxLayout, QDesktopWidget, QPushButton,  QMessageBox, QPlainTextEdit
from PyQt5.Qt import Qt

import stdio
import libpg
import parameters as pa
import lib_paroquia

class Dialog(QDialog):
    def __init__(self, nas_id,  parent = None):
        super(Dialog,  self).__init__(parent)
        self.resize(1200, 768)
        self.center()
        self.nas_dic = lib_paroquia.get_nascimentos_data(nas_id)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.WindowTitleHint)
        self.setWindowTitle('Altera Registo de Nascimento') 
        c_box_width = 260
        masterLayout = QHBoxLayout(self)
        mainLayout = QVBoxLayout()

        self.nas_id = QLineEdit()
        self.nas_id.setMaximumWidth(60)

        self.nas_ano = QLineEdit()
        self.nas_ano.setMaximumWidth(60)
        self.nas_registo = QLineEdit()
        self.nas_registo.setMaximumWidth(60)
        self.nas_folha = QLineEdit()
        self.nas_folha.setMaximumWidth(60)
        self.nas_folha.setMaxLength(10)

        mainLayout.addLayout(self.addHDumLayout(['Num:',self.nas_id,'Ano:',self.nas_ano,
            'Registo:',self.nas_registo,'Folha(s):',self.nas_folha,True]))

        dumLayout = QHBoxLayout()
        self.nas_data_baptismo = QDateEdit()
        self.nas_data_baptismo.setDisplayFormat("dd.MM.yyyy")
        # self.nas_data_nascimento = QDateEdit()
        # self.nas_data_nascimento.setDisplayFormat("dd.MMM.yyyy")
        self.nas_data = QLineEdit()

        self.nas_sexo = QComboBox()
        self.nas_sexo.setEditable(True)
        self.nas_sexo.addItems(pa.dsSexo)
        self.nas_numero_filho = QLineEdit()
        self.nas_numero_filho.setMaximumWidth(50)
        self.nas_pais_casados = QCheckBox()
        dumLayout.addLayout(self.addHDumLayout(['Data:',self.nas_data,
            'Baptizado a:',self.nas_data_baptismo, 'Sexo:',self.nas_sexo,'# Filho:',self.nas_numero_filho,
           'Pais são casados:',self.nas_pais_casados,True]))
        mainLayout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_nome = QLineEdit()
        self.nas_nome.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Nome:',self.nas_nome]))
        mainLayout.addLayout(dumLayout)

        self.nas_pai = QLineEdit()
        self.nas_pai.setMaxLength(50)
        self.nas_pai_idade = QLineEdit()
        self.nas_pai_idade.setMaximumWidth(30)


        self.nas_pai_estado = QComboBox()
        self.nas_pai_estado.setEditable(True)
        self.nas_pai_estado.addItems(pa.dsEstados)
        mainLayout.addLayout(self.addHDumLayout(
            ['Pai:',self.nas_pai,'Estado:',self.nas_pai_estado,'Idade:',self.nas_pai_idade]))


        self.nas_pai_nat = QComboBox()
        self.nas_pai_nat.setEditable(True)
        self.nas_pai_nat.setMaximumWidth(c_box_width)
        self.nas_pai_nat.addItems(pa.dsLocais)
        mainLayout.addLayout(self.addHDumLayout(['Naturalidade:',self.nas_pai_nat,True]))

        self.nas_pai_res = QComboBox()
        self.nas_pai_res.setEditable(True)
        self.nas_pai_res.setMaximumWidth(c_box_width)
        self.nas_pai_res.addItems(pa.dsLocais)
        mainLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_pai_res,True]))
        self.nas_pai_prof = QComboBox()
        self.nas_pai_prof.setEditable(True)
        self.nas_pai_prof.addItems(pa.dsProfissoes)
        mainLayout.addLayout(self.addHDumLayout(['Profissão:',self.nas_pai_prof, True]))


        self.nas_mae = QLineEdit()
        self.nas_mae.setMaxLength(50)
        self.nas_mae_idade = QLineEdit()
        self.nas_mae_idade.setMaximumWidth(30)


        self.nas_mae_estado = QComboBox()
        self.nas_mae_estado.setEditable(True)
        self.nas_mae_estado.addItems(pa.dsEstados)

        mainLayout.addLayout(self.addHDumLayout(['Mãe:',self.nas_mae,'Estado Civil:',self.nas_mae_estado,'Idade:',self.nas_mae_idade]))
        
        self.nas_mae_nat = QComboBox()
        self.nas_mae_nat.setEditable(True)
        self.nas_mae_nat.setMaximumWidth(c_box_width)
        self.nas_mae_nat.addItems(pa.dsLocais)
        mainLayout.addLayout(self.addHDumLayout(['Naturalidade:',self.nas_mae_nat, True]))

        self.nas_mae_res = QComboBox()
        self.nas_mae_res.setEditable(True)
        self.nas_mae_res.setMaximumWidth(c_box_width)
        self.nas_mae_res.addItems(pa.dsLocais)
        mainLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_mae_res, True]))

        self.nas_mae_prof = QComboBox()
        self.nas_mae_prof.setEditable(True)
        self.nas_pai_prof.setMaximumWidth(c_box_width)
        self.nas_mae_prof.addItems(pa.dsProfissoes)
        mainLayout.addLayout(self.addHDumLayout(['Profissão:',self.nas_mae_prof, True]))

        # cria tabulador
        self.tabuladorTabWidget = QTabWidget() 

        # cria pagina
        self.tab1 = QWidget()
        dumLayout = QVBoxLayout(self.tab1)
   
        self.nas_avo_paterno = QLineEdit()
        self.nas_avo_paterno.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Avô Paterno:',self.nas_avo_paterno, True]))

        self.nas_avo_paterno_prof = QComboBox()
        self.nas_avo_paterno_prof.setMaximumWidth(c_box_width)
        self.nas_avo_paterno_prof.setEditable(True)
        self.nas_avo_paterno_prof.addItems(pa.dsProfissoes)
        dumLayout.addLayout(self.addHDumLayout(['Profissão:',self.nas_avo_paterno_prof, True]))

        self.nas_avo_paterno_nat = QComboBox()
        self.nas_avo_paterno_nat.setEditable(True)
        self.nas_avo_paterno_nat.setMaximumWidth(c_box_width)
        self.nas_avo_paterno_nat.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Naturalidade:',self.nas_avo_paterno_nat, True]))

        self.nas_avo_paterno_res = QComboBox()
        self.nas_avo_paterno_res.setEditable(True)
        self.nas_avo_paterno_res.setMaximumWidth(c_box_width)
        self.nas_avo_paterno_res.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_avo_paterno_res, True]))
        
        # fecha a pagina
        self.tabuladorTabWidget.addTab(self.tab1, 'Avô Paterno')

        # nova pagina
        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        self.nas_avo_paterna = QLineEdit()
        self.nas_avo_paterna.setMaxLength(50)
        tab1Layout.addLayout(self.addHDumLayout(['Avó Paterna:',self.nas_avo_paterna]))

        self.nas_avo_paterna_prof = QComboBox()
        self.nas_avo_paterna_prof.setEditable(True)
        self.nas_avo_paterna_prof.setMaximumWidth(c_box_width)
        self.nas_avo_paterna_prof.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(self.addHDumLayout(['Profissão:',self.nas_avo_paterna_prof, True]))

        self.nas_avo_paterna_nat = QComboBox()
        self.nas_avo_paterna_nat.setEditable(True)
        self.nas_avo_paterna_nat.setMaximumWidth(c_box_width)
        self.nas_avo_paterna_nat.addItems(pa.dsLocais)
        tab1Layout.addLayout(self.addHDumLayout(['Naturalidade:',self.nas_avo_paterna_nat, True]))

        self.nas_avo_paterna_res = QComboBox()
        self.nas_avo_paterna_res.setEditable(True)
        self.nas_avo_paterna_res.setMaximumWidth(c_box_width)
        self.nas_avo_paterna_res.addItems(pa.dsLocais)
        tab1Layout.addLayout(self.addHDumLayout(['Residencia:',self.nas_avo_paterna_res, True]))

        # fecha pagina
        self.tabuladorTabWidget.addTab(self.tab1, 'Avó Paterna')

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        self.nas_avo_materno = QLineEdit()
        self.nas_avo_materno.setMaxLength(50)
        tab1Layout.addLayout(self.addHDumLayout(['Avô Materno',self.nas_avo_materno]))

        self.nas_avo_materno_prof = QComboBox()
        self.nas_avo_materno_prof.setEditable(True)
        self.nas_avo_materno_prof.setMaximumWidth(c_box_width)
        self.nas_avo_materno_prof.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(self.addHDumLayout(['Profissão:',self.nas_avo_materno_prof, True]))

        self.nas_avo_materno_nat = QComboBox()
        self.nas_avo_materno_nat.setEditable(True)
        self.nas_avo_materno_nat.setMaximumWidth(c_box_width)
        self.nas_avo_materno_nat.addItems(pa.dsLocais)
        tab1Layout.addLayout(self.addHDumLayout(['Naturalidade:',self.nas_avo_materno_nat, True]))

        self.nas_avo_materno_res = QComboBox()
        self.nas_avo_materno_res.setEditable(True)
        self.nas_avo_materno_res.setMaximumWidth(c_box_width)
        self.nas_avo_materno_res.addItems(pa.dsLocais)
        tab1Layout.addLayout(self.addHDumLayout(['Residencia',self.nas_avo_materno_res, True]))
        
        self.tabuladorTabWidget.addTab(self.tab1, 'Avô Materno')


        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        self.nas_avo_materna = QLineEdit()
        self.nas_avo_materna.setMaxLength(50)
        tab1Layout.addLayout(self.addHDumLayout(['Avó Materna:',self.nas_avo_materna]))

        self.nas_avo_materna_prof = QComboBox()
        self.nas_avo_materna_prof.setEditable(True)
        self.nas_avo_materna_prof.setMaximumWidth(c_box_width)
        self.nas_avo_materna_prof.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(self.addHDumLayout(['Profissão:',self.nas_avo_materna_prof, True]))

        self.nas_avo_materna_nat = QComboBox()
        self.nas_avo_materna_nat.setEditable(True)
        self.nas_avo_materna_nat.setMaximumWidth(c_box_width)
        self.nas_avo_materna_nat.addItems(pa.dsLocais)
        tab1Layout.addLayout(self.addHDumLayout(['Naturalidade:',self.nas_avo_materna_nat, True]))

        self.nas_avo_materna_res = QComboBox()
        self.nas_avo_materna_res.setEditable(True)
        self.nas_avo_materna_res.setMaximumWidth(c_box_width)
        self.nas_avo_materna_res.addItems(pa.dsLocais)
        tab1Layout.addLayout(self.addHDumLayout(['Residencia:',self.nas_avo_materna_res, True]))

        self.tabuladorTabWidget.addTab(self.tab1, 'Avó Materna') 

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        self.nas_padrinho = QLineEdit()
        self.nas_padrinho.setMaxLength(50)
        tab1Layout.addLayout(self.addHDumLayout(['Padrinho:',self.nas_padrinho]))
       

        self.nas_padrinho_estado = QComboBox()
        self.nas_padrinho_estado.setEditable(True)
        self.nas_padrinho_estado.setMaximumWidth(c_box_width)
        self.nas_padrinho_estado.addItems(pa.dsEstados)
        tab1Layout.addLayout(self.addHDumLayout(['Estado:',self.nas_padrinho_estado,True]))

        self.nas_padrinho_prof = QComboBox()
        self.nas_padrinho_prof.setEditable(True)
        self.nas_padrinho_prof.setMaximumWidth(c_box_width)
        self.nas_padrinho_prof.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(self.addHDumLayout(['Profissão:',self.nas_padrinho_prof,True]))

        self.nas_padrinho_res = QComboBox()
        self.nas_padrinho_res.setEditable(True)
        self.nas_padrinho_res.setMaximumWidth(c_box_width)
        self.nas_padrinho_res.addItems(pa.dsLocais)
        self.nas_padrinho_assinou = QCheckBox()
        tab1Layout.addLayout(self.addHDumLayout(['Residencia:',self.nas_padrinho_res,'Assinou?:',self.nas_padrinho_assinou, True]))

        self.tabuladorTabWidget.addTab(self.tab1, 'Padrinho')

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        self.nas_madrinha = QLineEdit()
        self.nas_madrinha.setMaxLength(50)
        tab1Layout.addLayout(self.addHDumLayout(['Madrinha:',self.nas_madrinha]))

        self.nas_madrinha_estado = QComboBox()
        self.nas_madrinha_estado.setEditable(True)
        self.nas_madrinha_estado.setMaximumWidth(c_box_width)
        self.nas_madrinha_estado.addItems(pa.dsEstados)
        tab1Layout.addLayout(self.addHDumLayout(['Estado:',self.nas_madrinha_estado, True]))
        
        self.nas_madrinha_prof = QComboBox()
        self.nas_madrinha_prof.setEditable(True)
        self.nas_madrinha_prof.setMaximumWidth(c_box_width)
        self.nas_madrinha_prof.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(self.addHDumLayout(['Profissão:',self.nas_madrinha_prof, True]))
        
        self.nas_madrinha_res = QComboBox()
        self.nas_madrinha_res.setEditable(True)
        self.nas_madrinha_res.setMaximumWidth(c_box_width)
        self.nas_madrinha_res.addItems(pa.dsLocais)
        
        self.nas_madrinha_assinou = QCheckBox()
        tab1Layout.addLayout(self.addHDumLayout(['Residencia:',self.nas_madrinha_res,'Assinou?:',self.nas_madrinha_assinou, True]))

        self.tabuladorTabWidget.addTab(self.tab1, 'Madrinha')

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        dumLayout = QHBoxLayout()
        self.nas_t1 = QLineEdit()
        self.nas_t1.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Nome:',self.nas_t1]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t1_prof = QComboBox()
        self.nas_t1_prof.setEditable(True)
        self.nas_t1_prof.setMaximumWidth(c_box_width)
        self.nas_t1_prof.addItems(pa.dsProfissoes)
        dumLayout.addLayout(self.addHDumLayout(['Profissão',self.nas_t1_prof, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t1_res = QComboBox()
        self.nas_t1_res.setEditable(True)
        self.nas_t1_res.setMaximumWidth(c_box_width)    
        self.nas_t1_res.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_t1_res, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t1_estado = QComboBox()
        self.nas_t1_estado.setEditable(True)
        self.nas_t1_estado.setMaximumWidth(c_box_width)
        self.nas_t1_estado.addItems(pa.dsEstados)
        dumLayout.addLayout(self.addHDumLayout(['Estado:',self.nas_t1_estado, True]))
        tab1Layout.addLayout(dumLayout)

        self.tabuladorTabWidget.addTab(self.tab1, 'Test. 1')

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        dumLayout = QHBoxLayout()
        self.nas_t2 = QLineEdit()
        self.nas_t2.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Nome:',self.nas_t2]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t2_prof = QComboBox()
        self.nas_t2_prof.setEditable(True)
        self.nas_t2_prof.setMaximumWidth(c_box_width)
        self.nas_t2_prof.addItems(pa.dsProfissoes)
        dumLayout.addLayout(self.addHDumLayout(['Profissão',self.nas_t2_prof, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t2_res = QComboBox()
        self.nas_t2_res.setEditable(True)
        self.nas_t2_res.setMaximumWidth(c_box_width)
        self.nas_t2_res.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_t2_res, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t2_estado = QComboBox()
        self.nas_t2_estado.setEditable(True)
        self.nas_t2_estado.setMaximumWidth(c_box_width)
        self.nas_t2_estado.addItems(pa.dsEstados)
        dumLayout.addLayout(self.addHDumLayout(['Estado:',self.nas_t2_estado, True]))
        tab1Layout.addLayout(dumLayout)

        self.tabuladorTabWidget.addTab(self.tab1, 'Test. 2')
        # mainLayout.addWidget(self.tabuladorTabWidget)

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        dumLayout = QHBoxLayout()
        self.nas_t3 = QLineEdit()
        self.nas_t3.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Nome:',self.nas_t3]))
        tab1Layout.addLayout(dumLayout)

        self.nas_t3_prof = QComboBox()
        self.nas_t3_prof.setEditable(True)
        self.nas_t3_prof.setMaximumWidth(c_box_width)
        self.nas_t3_prof.addItems(pa.dsProfissoes)
        tab1Layout.addLayout(self.addHDumLayout(['Profissão',self.nas_t3_prof, True]))

        dumLayout = QHBoxLayout()
        self.nas_t3_res = QComboBox()
        self.nas_t3_res.setEditable(True)
        self.nas_t3_res.setMaximumWidth(c_box_width)
        self.nas_t3_res.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_t3_res, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t3_estado = QComboBox()
        self.nas_t3_estado.setEditable(True)
        self.nas_t3_estado.setMaximumWidth(c_box_width)
        self.nas_t3_estado.addItems(pa.dsEstados)
        dumLayout.addLayout(self.addHDumLayout(['Estado:',self.nas_t3_estado, True]))
        tab1Layout.addLayout(dumLayout)

        self.tabuladorTabWidget.addTab(self.tab1, 'Test. 3')
        # mainLayout.addWidget(self.tabuladorTabWidget)

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        dumLayout = QHBoxLayout()
        self.nas_t4 = QLineEdit()
        self.nas_t4.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Testemunha:',self.nas_t4]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t4_prof = QComboBox()
        self.nas_t4_prof.setEditable(True)
        self.nas_t4_prof.setMaximumWidth(c_box_width)
        self.nas_t4_prof.addItems(pa.dsProfissoes)
        dumLayout.addLayout(self.addHDumLayout(['Profissão',self.nas_t4_prof, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t4_res = QComboBox()
        self.nas_t4_res.setEditable(True)
        self.nas_t4_res.setMaximumWidth(c_box_width)
        self.nas_t4_res.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_t4_res, True]))
        tab1Layout.addLayout(dumLayout)


        dumLayout = QHBoxLayout()
        self.nas_t4_estado = QComboBox()
        self.nas_t4_estado.setEditable(True)
        self.nas_t4_estado.setMaximumWidth(c_box_width)
        self.nas_t4_estado.addItems(pa.dsEstados)
        dumLayout.addLayout(self.addHDumLayout(['Estado:',self.nas_t4_estado, True]))
        tab1Layout.addLayout(dumLayout)

        self.tabuladorTabWidget.addTab(self.tab1, 'Test. 4')
        # mainLayout.addWidget(self.tabuladorTabWidget)

        self.tab1 = QWidget()
        tab1Layout = QVBoxLayout(self.tab1)

        dumLayout = QHBoxLayout()
        self.nas_t5 = QLineEdit()
        self.nas_t5.setMaxLength(50)
        dumLayout.addLayout(self.addHDumLayout(['Nome:',self.nas_t5]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t5_prof = QComboBox()
        self.nas_t5_prof.setEditable(True)
        self.nas_t5_prof.setMaximumWidth(c_box_width)
        self.nas_t5_prof.addItems(pa.dsProfissoes)
        dumLayout.addLayout(self.addHDumLayout(['Profissão',self.nas_t5_prof, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t5_res = QComboBox()
        self.nas_t5_res.setEditable(True)
        self.nas_t5_res.setMaximumWidth(c_box_width)
        self.nas_t5_res.addItems(pa.dsLocais)
        dumLayout.addLayout(self.addHDumLayout(['Residencia:',self.nas_t5_res, True]))
        tab1Layout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_t5_estado = QComboBox()
        self.nas_t5_estado.setEditable(True)
        self.nas_t5_estado.setMaximumWidth(c_box_width)
        self.nas_t5_estado.addItems(pa.dsEstados)
        dumLayout.addLayout(self.addHDumLayout(['Estado:',self.nas_t5_estado, True]))
        tab1Layout.addLayout(dumLayout)
        self.tabuladorTabWidget.addTab(self.tab1, 'Test. 5')
        mainLayout.addWidget(self.tabuladorTabWidget)

        dumLayout = QHBoxLayout()
        self.nas_padre = QComboBox()
        self.nas_padre.setEditable(True)
        self.nas_padre.addItems(pa.dsPadres)
        self.nas_padre_res = QComboBox()
        self.nas_padre_res.setEditable(True)
        self.nas_padre_res.addItems(pa.dsLocais)
        self.nas_selos = QLineEdit()
        self.nas_selos.setMinimumWidth(60)
        dumLayout.addLayout(self.addHDumLayout(['Padre',self.nas_padre,'Residencia:',self.nas_padre_res,'Selos:',self.nas_selos,True]))
        mainLayout.addLayout(dumLayout)

        dumLayout = QHBoxLayout()
        self.nas_obs = QPlainTextEdit()
        # self.nas_obs.setMaximumHeight(100)
        dumLayout.addLayout(self.addHDumLayout(['Observações:',self.nas_obs]))
        mainLayout.addLayout(dumLayout)

        # self.backwardBtn = QPushButton('<')
        # if pa.current_index == -1:
        #     self.backwardBtn.setEnabled(False)
        # self.connect(self.backwardBtn, SIGNAL("clicked()"), self.backward_click)
        # self.backwardBtn.clicked.connect(self.backward_click)
        

        # self.forwardBtn = QPushButton('>')
        # if pa.current_index == -1:
        #     self.forwardBtn.setEnabled(False)
        # self.connect(self.forwardBtn, SIGNAL("clicked()"), self.forward_click)
        # self.forwardBtn.clicked.connect(self.forward_click)
         
         
        self.saveBtn = QPushButton('Guarda')
        self.saveBtn.clicked.connect(self.save_btn_click)
        
        self.save_and_closeBtn = QPushButton('Guarda e Sai')
        self.save_and_closeBtn.clicked.connect(self.save_and_close_btn_click)
        
         
        self.cancelBtn = QPushButton('Sair sem Guardar')
        self.cancelBtn.clicked.connect(self.cancel_btn_click)

        mainLayout.addLayout(self.addHDumLayout([self.saveBtn,self.save_and_closeBtn,self.cancelBtn]))
        masterLayout.addLayout(mainLayout)
        self.refresh_form()

    def forward_click(self):
        if pa.current_index < pa.current_dataset_limit:
            pa.current_index +=1
            pa.current_record = pa.current_dataset[pa.current_index]
            self.nas_dic = get_nascimentos_data(pa.current_dataset[pa.current_index])
            self.refresh_form()
        else:
            self.forwardBtn.setEnabled(False)
            self.backwardBtn.setEnabled(True)

    def backward_click(self):
        if pa.current_index > 0:
            pa.current_index -=1
            pa.current_record = pa.current_dataset[pa.current_index]
            self.nas_dic = get_nascimentos_data(pa.current_dataset[pa.current_index])
            self.refresh_form()
        else:
            self.forwardBtn.setEnabled(True)
            self.backwardBtn.setEnabled(False)


    def save_btn_click(self):
        ## pa.obitos_rec
        if self.check_fields_locais():
            if self.check_fields_profissoes():
                if self.check_fields_padres():
                    self.save_record()
                    
    def save_and_close_btn_click(self):
        if self.check_fields_locais():
            if self.check_fields_profissoes():
                if self.check_fields_padres():
                    self.save_record()
                    self.close()

    def cancel_btn_click(self):
        self.close()

    def check_fields_locais(self):
        # 'check_fields_locais'
        for n in self.nas_pai_nat, self.nas_pai_res, self.nas_mae_nat, self.nas_mae_res, self.nas_avo_paterno_nat,\
                self.nas_avo_paterno_res, self.nas_avo_paterna_nat, self.nas_avo_paterna_res, self.nas_avo_materno_nat, self.nas_avo_materno_res, \
                self.nas_avo_materna_nat, self.nas_avo_materna_res, self.nas_padrinho_res, self.nas_madrinha_res, self.nas_t1_res, \
                self.nas_t2_res, self.nas_t3_res, self.nas_t4_res, self.nas_t5_res, self.nas_padre_res:
            toto = n.currentText()
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
    def check_fields_profissoes(self):
        # # 'check_fields_profissoes'
        for n in self.nas_pai_prof, self.nas_mae_prof, self.nas_avo_paterno_prof, self.nas_avo_paterna_prof, self.nas_avo_materno_prof,\
            self.nas_avo_materna_prof, self.nas_padrinho_prof, self.nas_madrinha_prof, self.nas_t1_prof, self.nas_t2_prof,\
            self.nas_t3_prof, self.nas_t4_prof, self.nas_t5_prof:

            toto = n.currentText()
            if toto not in pa.profissoes_dict :
                # # 'não existe',n.currentText()
                if self.askForNew('Adiciona Profissão','Adicionar esta Profissão?', toto):
                    # # 'addciona local'
                    libpg.add_record_to_table('profissoes', 'prof',toto)
                    # # 'refresca dicionarios'
                    lib_paroquia.get_profissoes()
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

        toto = self.nas_padre.currentText()
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
        # stdio.read_field(self.nas_data_nascimento,'nas_data_nascimento',self.nas_dic)
        # stdio.read_field(self.nas_local,'nas_local',self.nas_dic)
        stdio.read_field(self.nas_id,'nas_id',self.nas_dic)
        stdio.read_field(self.nas_ano,'nas_ano',self.nas_dic)
        stdio.read_field(self.nas_registo,'nas_registo',self.nas_dic)
        stdio.read_field(self.nas_folha,'nas_folha',self.nas_dic)
        stdio.read_field(self.nas_data_baptismo,'nas_data_baptismo',self.nas_dic)
        stdio.read_field(self.nas_data,'nas_data',self.nas_dic)
        stdio.read_field(self.nas_nome,'nas_nome',self.nas_dic)
        stdio.read_field(self.nas_numero_filho,'nas_numero_filho',self.nas_dic)
        stdio.read_field(self.nas_sexo,'nas_sexo',self.nas_dic)
        stdio.read_field(self.nas_pais_casados,'nas_pais_casados',self.nas_dic)
        stdio.read_field(self.nas_pai,'nas_pai',self.nas_dic)
        stdio.read_field(self.nas_pai_idade,'nas_pai_idade',self.nas_dic)
        stdio.read_field(self.nas_pai_estado,'nas_pai_estado',self.nas_dic)
        stdio.read_field(self.nas_pai_nat,'nas_pai_nat',self.nas_dic)
        stdio.read_field(self.nas_pai_res,'nas_pai_res',self.nas_dic)
        stdio.read_field(self.nas_pai_prof,'nas_pai_prof',self.nas_dic)
        stdio.read_field(self.nas_mae,'nas_mae',self.nas_dic)
        stdio.read_field(self.nas_mae_nat,'nas_mae_nat',self.nas_dic)
        stdio.read_field(self.nas_mae_res,'nas_mae_res',self.nas_dic)
        stdio.read_field(self.nas_mae_prof,'nas_mae_prof',self.nas_dic)
        stdio.read_field(self.nas_avo_paterno,'nas_avo_paterno',self.nas_dic)
        stdio.read_field(self.nas_avo_paterno_prof,'nas_avo_paterno_prof',self.nas_dic)
        stdio.read_field(self.nas_avo_paterno_nat,'nas_avo_paterno_nat',self.nas_dic)
        stdio.read_field(self.nas_avo_paterno_res,'nas_avo_paterno_res',self.nas_dic)
        stdio.read_field(self.nas_avo_paterna,'nas_avo_paterna',self.nas_dic)
        stdio.read_field(self.nas_avo_paterna_prof,'nas_avo_paterna_prof',self.nas_dic)
        stdio.read_field(self.nas_avo_paterna_nat,'nas_avo_paterna_nat',self.nas_dic)
        stdio.read_field(self.nas_avo_paterna_res,'nas_avo_paterna_res',self.nas_dic)
        stdio.read_field(self.nas_avo_materno,'nas_avo_materno',self.nas_dic)
        stdio.read_field(self.nas_avo_materno_prof,'nas_avo_materno_prof',self.nas_dic)
        stdio.read_field(self.nas_avo_materno_nat,'nas_avo_materno_nat',self.nas_dic)
        stdio.read_field(self.nas_avo_materno_res,'nas_avo_materno_res',self.nas_dic)
        stdio.read_field(self.nas_avo_materna,'nas_avo_materna',self.nas_dic)
        stdio.read_field(self.nas_avo_materna_prof,'nas_avo_materna_prof',self.nas_dic)
        stdio.read_field(self.nas_avo_materna_nat,'nas_avo_materna_nat',self.nas_dic)
        stdio.read_field(self.nas_avo_materna_res,'nas_avo_materna_res',self.nas_dic)
        stdio.read_field(self.nas_padrinho,'nas_padrinho',self.nas_dic)
        stdio.read_field(self.nas_padrinho_estado,'nas_padrinho_estado',self.nas_dic)
        stdio.read_field(self.nas_padrinho_prof,'nas_padrinho_prof',self.nas_dic)
        stdio.read_field(self.nas_padrinho_res,'nas_padrinho_res',self.nas_dic)
        stdio.read_field(self.nas_padrinho_assinou,'nas_padrinho_assinou',self.nas_dic)
        stdio.read_field(self.nas_madrinha,'nas_madrinha',self.nas_dic)
        stdio.read_field(self.nas_madrinha_estado,'nas_madrinha_estado',self.nas_dic)
        stdio.read_field(self.nas_madrinha_prof,'nas_madrinha_prof',self.nas_dic)
        stdio.read_field(self.nas_madrinha_res,'nas_madrinha_res',self.nas_dic)
        stdio.read_field(self.nas_madrinha_assinou,'nas_madrinha_assinou',self.nas_dic)
        stdio.read_field(self.nas_t1,'nas_t1',self.nas_dic)
        stdio.read_field(self.nas_t1_prof,'nas_t1_prof',self.nas_dic)
        stdio.read_field(self.nas_t1_res,'nas_t1_res',self.nas_dic)
        stdio.read_field(self.nas_t1_estado,'nas_t1_estado',self.nas_dic)
        stdio.read_field(self.nas_t2,'nas_t2',self.nas_dic)
        stdio.read_field(self.nas_t2_prof,'nas_t2_prof',self.nas_dic)
        stdio.read_field(self.nas_t2_res,'nas_t2_res',self.nas_dic)
        stdio.read_field(self.nas_t2_estado,'nas_t2_estado',self.nas_dic)
        stdio.read_field(self.nas_t3,'nas_t3',self.nas_dic)
        stdio.read_field(self.nas_t3_prof,'nas_t3_prof',self.nas_dic)
        stdio.read_field(self.nas_t3_res,'nas_t3_res',self.nas_dic)
        stdio.read_field(self.nas_t3_estado,'nas_t3_estado',self.nas_dic)
        stdio.read_field(self.nas_t4,'nas_t4',self.nas_dic)
        stdio.read_field(self.nas_t4_prof,'nas_t4_prof',self.nas_dic)
        stdio.read_field(self.nas_t4_res,'nas_t4_res',self.nas_dic)
        stdio.read_field(self.nas_t4_estado,'nas_t4_estado',self.nas_dic)
        stdio.read_field(self.nas_t5,'nas_t5',self.nas_dic)
        stdio.read_field(self.nas_t5_prof,'nas_t5_prof',self.nas_dic)
        stdio.read_field(self.nas_t5_res,'nas_t5_res',self.nas_dic)
        stdio.read_field(self.nas_t5_estado,'nas_t5_estado',self.nas_dic)
        stdio.read_field(self.nas_padre,'nas_padre',self.nas_dic)
        stdio.read_field(self.nas_padre_res,'nas_padre_res',self.nas_dic)
        stdio.read_field(self.nas_selos,'nas_selos',self.nas_dic)
        stdio.read_field(self.nas_obs,'nas_obs',self.nas_dic)
        stdio.read_field(self.nas_mae_idade,'nas_mae_idade',self.nas_dic)
        stdio.read_field(self.nas_mae_estado,'nas_mae_estado',self.nas_dic)

    def save_record(self):
        # nas_local=%s, 
        # data += (stdio.get_value(self.nas_local,pa.locais_dict),)
        sql = '''UPDATE nascimentos set 
        nas_ano=%s, 
        nas_registo=%s, 
        nas_folha=%s, 
        nas_data=%s, 
        nas_data_baptismo=%s, 
        nas_nome=%s, 
        nas_numero_filho=%s, 
        nas_sexo=%s, 
        nas_pais_casados=%s, 
        nas_pai=%s, 
        nas_pai_idade=%s, 
        nas_pai_estado=%s, 
        nas_pai_nat=%s, 
        nas_pai_res=%s, 
        nas_pai_prof=%s, 
        nas_mae=%s, 
        nas_mae_nat=%s, 
        nas_mae_res=%s, 
        nas_mae_prof=%s, 
        nas_avo_paterno=%s, 
        nas_avo_paterno_prof=%s, 
        nas_avo_paterno_nat=%s, 
        nas_avo_paterno_res=%s, 
        nas_avo_paterna=%s, 
        nas_avo_paterna_prof=%s, 
        nas_avo_paterna_nat=%s, 
        nas_avo_paterna_res=%s, 
        nas_avo_materno=%s, 
        nas_avo_materno_prof=%s, 
        nas_avo_materno_nat=%s, 
        nas_avo_materno_res=%s, 
        nas_avo_materna=%s, 
        nas_avo_materna_prof=%s, 
        nas_avo_materna_nat=%s, 
        nas_avo_materna_res=%s, 
        nas_padrinho=%s, 
        nas_padrinho_estado=%s, 
        nas_padrinho_prof=%s, 
        nas_padrinho_res=%s, 
        nas_padrinho_assinou=%s, 
        nas_madrinha=%s, 
        nas_madrinha_estado=%s, 
        nas_madrinha_prof=%s, 
        nas_madrinha_res=%s, 
        nas_madrinha_assinou=%s, 
        nas_t1=%s, 
        nas_t1_prof=%s, 
        nas_t1_res=%s, 
        nas_t1_estado=%s, 
        nas_t2=%s, 
        nas_t2_prof=%s, 
        nas_t2_res=%s, 
        nas_t2_estado=%s, 
        nas_t3=%s, 
        nas_t3_prof=%s, 
        nas_t3_res=%s, 
        nas_t3_estado=%s, 
        nas_t4=%s, 
        nas_t4_prof=%s, 
        nas_t4_res=%s, 
        nas_t4_estado=%s, 
        nas_t5=%s, 
        nas_t5_prof=%s, 
        nas_t5_res=%s, 
        nas_t5_estado=%s, 
        nas_padre=%s, 
        nas_padre_res=%s, 
        nas_selos=%s, 
        nas_obs=%s, 
        nas_mae_idade=%s, 
        nas_mae_estado=%s 
         WHERE nas_id= %s'''
        data = ()
        data += (stdio.get_value(self.nas_ano),)
        data += (stdio.get_value(self.nas_registo),)
        data += (stdio.get_value(self.nas_folha),)
        data += (stdio.get_value(self.nas_data),)
        data += (stdio.get_value(self.nas_data_baptismo),)
        data += (stdio.get_value(self.nas_nome),)
        data += (stdio.get_value(self.nas_numero_filho),)
        data += (stdio.get_value(self.nas_sexo,pa.sexo_dict),)
        data += (stdio.get_value(self.nas_pais_casados),)
        data += (stdio.get_value(self.nas_pai),)
        data += (stdio.get_value(self.nas_pai_idade),)
        data += (stdio.get_value(self.nas_pai_estado, pa.estados_dict),)
        data += (stdio.get_value(self.nas_pai_nat,pa.locais_dict),)
        data += (stdio.get_value(self.nas_pai_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_pai_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_mae),)
        data += (stdio.get_value(self.nas_mae_nat,pa.locais_dict),)
        data += (stdio.get_value(self.nas_mae_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_mae_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_avo_paterno),)
        data += (stdio.get_value(self.nas_avo_paterno_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_avo_paterno_nat,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_paterno_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_paterna),)
        data += (stdio.get_value(self.nas_avo_paterna_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_avo_paterna_nat,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_paterna_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_materno),)
        data += (stdio.get_value(self.nas_avo_materno_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_avo_materno_nat,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_materno_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_materna),)
        data += (stdio.get_value(self.nas_avo_materna_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_avo_materna_nat,pa.locais_dict),)
        data += (stdio.get_value(self.nas_avo_materna_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_padrinho),)
        data += (stdio.get_value(self.nas_padrinho_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_padrinho_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_padrinho_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_padrinho_assinou),)
        data += (stdio.get_value(self.nas_madrinha),)
        data += (stdio.get_value(self.nas_madrinha_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_madrinha_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_madrinha_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_madrinha_assinou),)
        data += (stdio.get_value(self.nas_t1),)
        data += (stdio.get_value(self.nas_t1_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_t1_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_t1_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_t2),)
        data += (stdio.get_value(self.nas_t2_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_t2_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_t2_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_t3),)
        data += (stdio.get_value(self.nas_t3_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_t3_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_t3_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_t4),)
        data += (stdio.get_value(self.nas_t4_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_t4_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_t4_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_t5),)
        data += (stdio.get_value(self.nas_t5_prof,pa.profissoes_dict),)
        data += (stdio.get_value(self.nas_t5_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_t5_estado,pa.estados_dict),)
        data += (stdio.get_value(self.nas_padre,pa.padres_dict),)
        data += (stdio.get_value(self.nas_padre_res,pa.locais_dict),)
        data += (stdio.get_value(self.nas_selos),)
        data += (stdio.get_value(self.nas_obs),
            stdio.get_value(self.nas_mae_idade),
            stdio.get_value(self.nas_mae_estado,pa.estados_dict), pa.current_record)
        libpg.execute_query(sql,data)



    # def make_write_sql(self,table, fields, index):
    #     toto = ''
    #     toto += 'sql =  'UPDATE ' + table + ' set    n\'
    #     for n in fields:
    #         if len(n) == 2:
    #             toto += n[1] + '=%s,    n'
    #         else:
    #             toto += n[1] + '=%s,    n'

    #     toto += 'where id = %s ' + str(index)
    #     toto += 'data = ()'
    #     for n in fields:
    #         if len(n) == 2:
    #             toto += 'data += (get_value(self.' + n[1] + ')  n'
    #         else:
    #             toto += 'data += (get_value( n'

    #     toto += ' ''
    #     stdio.print2file('update_sql.py',unicode(toto))

    def askForNew(self, caption, prefix, text):
        if QMessageBox.information(None,
                self.trUtf8("" + str(caption) + ""),
                self.trUtf8("" + str(prefix)+' n' +str(text)+""),
                QMessageBox.StandardButtons( 
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

    
    def setSizes(self, object,w,h):       
        object.setMaximumHeight (h)
        object.setMinimumHeight(h)
        object.setMaximumWidth(w)
        object.setMinimumWidth(w)

    def setSizeWidth(self, object, value):
        object.setMaximumWidth(value)
        object.setMinimumWidth(value)

    def setBtnSquare(self, object,value=60):       
        object.setMaximumHeight (value)
        object.setMinimumHeight(value)
        object.setMaximumWidth(value)
        object.setMinimumWidth(value)


    def check_obj(self, obj):
        if type(obj) == QLineEdit:
            if obj.text().isEmpty():
                return False
            else:
                return True
        if type(obj) == QPlainTextEdit:
            if obj.toPlainText().isEmpty():
                return False
            else:
                return True

    def addHDumLayout(self, listobj1, label_size = 90, align = Qt.AlignVCenter|Qt.AlignRight):
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