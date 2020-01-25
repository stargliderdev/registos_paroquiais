#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QTabWidget, QLabel, QCheckBox, QVBoxLayout, QLineEdit, QComboBox, QDateEdit, \
    QWidget, QDialog, QHBoxLayout, QDesktopWidget, QPushButton, QTextEdit, QMessageBox, QPlainTextEdit,QTextBrowser
from PyQt5.Qt import Qt

import settings
import parameters as pa

class SearchEngine(QDialog):
    def __init__(self, act=0, parent = None):
        super(SearchEngine,  self).__init__(parent)
        #self.resize(1024, 768)
        screen = QDesktopWidget().screenGeometry()
        self.center()

        # self.resize(1024, 768)
        # self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowTitle('Motor de Pesquisa')
        #vars
        self.toto = (False,)
        self.logic = ['E','OU']
        self.logic_dict = {0: ' and ', 1: ' or '}
        self.nas_order_dic = pa.nas_order_dic
        self.nas_order_items = pa.nas_order_items       
        self.cas_order_dic = pa.cas_order_dic
        self.cas_order_items = pa.cas_order_items
        self.obi_order_dic = pa.obi_order_dic
        self.obi_order_items = pa.obi_order_items

        mainLayout = QVBoxLayout(self)
        self.tabuladorTabWidget = QTabWidget()
        mainLayout.addWidget(self.tabuladorTabWidget)
        # masterLayout = QVBoxLayout(self)
        self.make_nas_tab()
        self.tabuladorTabWidget.addTab(self.tab1, 'Nascimentos')

        self.make_cas_tab()
        self.tabuladorTabWidget.addTab(self.tab2, 'Casamentos')

        self.make_obi_tab()
        self.tabuladorTabWidget.addTab(self.tab3, 'Óbitos')

        self.tabuladorTabWidget.setCurrentIndex(act)

        runBtn = QPushButton('Pesquisa')
        # self.connect(runBtn, SIGNAL("clicked()"), self.run_click)
        runBtn.clicked.connect(self.run_click)
        
        exitBtn = QPushButton('Sair')
        # self.connect(exitBtn, SIGNAL("clicked()"), self.exitClick)
        exitBtn.clicked.connect(self.exitClick)
        
        mainLayout.addLayout(self.addHDumLayout([runBtn,exitBtn]))

    def make_nas_tab(self):
        self.tab1 = QWidget()
        mainTabLayout = QVBoxLayout(self.tab1)

        self.nas_ini_year = QComboBox()
        self.nas_ini_year.addItems(pa.nascimentos_anos)
        self.nas_end_year = QComboBox()
        self.nas_end_year.addItems(pa.nascimentos_anos)
        mainTabLayout.addLayout(self.addHDumLayout(['Ano de Inicio', self.nas_ini_year,'Ano de Fim', self.nas_end_year]))

        self.nas_sortCbx = QComboBox()
        self.nas_sortCbx.addItems(self.nas_order_items)

        mainTabLayout.addLayout(self.addHDumLayout(['Ordena por', self.nas_sortCbx,True]))

        self.nasNomeEdit = QLineEdit()
        self.nasNomeLogic = QComboBox()
        self.nasNomeLogic.addItems(['----'])      
        mainTabLayout.addLayout(self.addHDumLayout(['Nome', self.nasNomeLogic, self.nasNomeEdit]))

        self.nasPaiEdit = QLineEdit()
        self.nasPaiLogic = QComboBox()
        self.nasPaiLogic.addItems(self.logic)      
        mainTabLayout.addLayout(self.addHDumLayout(['Pai', self.nasPaiLogic, self.nasPaiEdit]))

        self.nasMaeEdit = QLineEdit()
        self.nasMaeLogic = QComboBox()
        self.nasMaeLogic.addItems(self.logic)      
        mainTabLayout.addLayout(self.addHDumLayout(['Mãe', self.nasMaeLogic, self.nasMaeEdit]))
        
        self.nasAvoPatEdit = QLineEdit()
        self.nasAvoPatLogic = QComboBox()
        self.nasAvoPatLogic.addItems(self.logic)      
        mainTabLayout.addLayout(self.addHDumLayout(['Avô Paterno',self.nasAvoPatLogic, self.nasAvoPatEdit]))

        self.nasAvaPatEdit = QLineEdit()
        self.nasAvaPatLogic = QComboBox()
        self.nasAvaPatLogic.addItems(self.logic)      
        mainTabLayout.addLayout(self.addHDumLayout(['Avó Paterno',self.nasAvaPatLogic, self.nasAvaPatEdit]))

        self.nasAvoMatEdit = QLineEdit()
        self.nasAvoMatLogic = QComboBox()
        self.nasAvoMatLogic.addItems(self.logic)      
        mainTabLayout.addLayout(self.addHDumLayout(['Avô Materno',self.nasAvoMatLogic, self.nasAvoMatEdit]))

        self.nasAvaMatEdit = QLineEdit()
        self.nasAvaMatLogic = QComboBox()
        self.nasAvaMatLogic.addItems(self.logic)      
        mainTabLayout.addLayout(self.addHDumLayout(['Avó Materno',self.nasAvaMatLogic, self.nasAvaMatEdit]))

        if pa.nas_filter == {}:
            pass
        else:
            self.load_nas_dic()

    def make_cas_tab(self):
        self.tab2 = QWidget()
        mainTabLayout = QVBoxLayout(self.tab2)

        self.cas_ini_year = QComboBox()
        self.cas_ini_year.addItems(pa.casamentos_anos)
        self.cas_end_year = QComboBox()
        self.cas_end_year.addItems(pa.casamentos_anos)
        mainTabLayout.addLayout(self.addHDumLayout(['Ano de Inicio', self.cas_ini_year,'Ano de Fim', self.cas_end_year]))

        self.cas_sortCbx = QComboBox()
        self.cas_sortCbx.addItems(self.cas_order_items)
        mainTabLayout.addLayout(self.addHDumLayout(['Ordena por', self.cas_sortCbx,True]))

        self.casNoivoEdit = QLineEdit()
        self.casNoivoLogic = QComboBox()
        self.casNoivoLogic.addItems(['----'])
        mainTabLayout.addLayout(self.addHDumLayout(['Nome do Noivo', self.casNoivoLogic, self.casNoivoEdit]))

        self.casNoivaEdit = QLineEdit()
        self.casNoivaLogic = QComboBox()
        self.casNoivaLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Nome da Noiva', self.casNoivaLogic, self.casNoivaEdit]))

        self.casPaiNoivoEdit = QLineEdit()
        self.casPaiNoivoLogic = QComboBox()
        self.casPaiNoivoLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Pai do Noivo', self.casPaiNoivoLogic, self.casPaiNoivoEdit]))

        self.casMaeNoivoEdit = QLineEdit()
        self.casMaeNoivoLogic = QComboBox()
        self.casMaeNoivoLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Mãe do Noivo', self.casMaeNoivoLogic, self.casMaeNoivoEdit]))

        self.casPaiNoivaEdit = QLineEdit()
        self.casPaiNoivaLogic = QComboBox()
        self.casPaiNoivaLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Pai da Noiva', self.casPaiNoivaLogic, self.casPaiNoivaEdit]))

        self.casMaeNoivaEdit = QLineEdit()
        self.casMaeNoivaLogic = QComboBox()
        self.casMaeNoivaLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Mãe da Noiva', self.casMaeNoivaLogic, self.casMaeNoivaEdit]))

        if pa.cas_filter == {}:
            pass
        else:
            self.load_cas_dic()

    def make_obi_tab(self):
        self.tab3 = QWidget()
        mainTabLayout = QVBoxLayout(self.tab3)

        self.obi_ini_year = QComboBox()
        self.obi_ini_year.addItems(pa.obitos_anos)
        self.obi_end_year = QComboBox()
        self.obi_end_year.addItems(pa.obitos_anos)
        mainTabLayout.addLayout(self.addHDumLayout(['Ano de Inicio', self.obi_ini_year,'Ano de Fim', self.obi_end_year]))

        self.obi_sortCbx = QComboBox()
        self.obi_sortCbx.addItems(self.obi_order_items)
        mainTabLayout.addLayout(self.addHDumLayout(['Ordena por', self.obi_sortCbx,True]))

        self.obiNomeEdit = QLineEdit()
        self.obiNomeLogic = QComboBox()
        self.obiNomeLogic.addItems(['----'])
        mainTabLayout.addLayout(self.addHDumLayout(['Nome', self.obiNomeLogic, self.obiNomeEdit]))

        self.obiConjEdit = QLineEdit()
        self.obiConjLogic = QComboBox()
        self.obiConjLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Conjugue', self.obiConjLogic, self.obiConjEdit]))

        self.obiPaiEdit = QLineEdit()
        self.obiPaiLogic = QComboBox()
        self.obiPaiLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Pai', self.obiPaiLogic, self.obiPaiEdit]))

        self.obiMaeEdit = QLineEdit()
        self.obiMaeLogic = QComboBox()
        self.obiMaeLogic.addItems(self.logic)
        mainTabLayout.addLayout(self.addHDumLayout(['Mãe', self.obiMaeLogic, self.obiMaeEdit]))

        if pa.obi_filter == {}:
            pass
        else:
            self.load_obi_dic()

    def load_nas_dic(self):
        self.nas_ini_year.setCurrentIndex(pa.nas_filter['ini_year'])
        self.nas_end_year.setCurrentIndex(pa.nas_filter['end_year'])
        self.nas_sortCbx.setCurrentIndex(pa.nas_filter['sort_by'])
        self.nasNomeEdit.setText(pa.nas_filter['nome'])
        self.nasPaiEdit.setText(pa.nas_filter['pai'])
        self.nasPaiLogic.setCurrentIndex(pa.nas_filter['pai_log'])
        self.nasMaeEdit.setText(pa.nas_filter['mae'])
        self.nasMaeLogic.setCurrentIndex(pa.nas_filter['mae_log'])
        self.nasAvoPatEdit.setText(pa.nas_filter['avo_pat'])
        self.nasAvoPatLogic.setCurrentIndex(pa.nas_filter['avo_pat_log'])
        self.nasAvaPatEdit.setText(pa.nas_filter['ava_pat'])
        self.nasAvaPatLogic.setCurrentIndex(pa.nas_filter['ava_pat_log'])
        self.nasAvoMatEdit.setText(pa.nas_filter['avo_mat'])
        self.nasAvoMatLogic.setCurrentIndex(pa.nas_filter['avo_mat_log'])
        self.nasAvaMatEdit.setText(pa.nas_filter['ava_mat'])
        self.nasAvaMatLogic.setCurrentIndex(pa.nas_filter['ava_mat_log'])
    
    def load_cas_dic(self):
        self.cas_ini_year.setCurrentIndex(pa.cas_filter['ini_year'])
        self.cas_end_year.setCurrentIndex(pa.cas_filter['end_year'])
        self.cas_sortCbx.setCurrentIndex(pa.cas_filter['sort_by'])
        self.casNoivoEdit.setText(pa.cas_filter['noivo'])
        self.casNoivaEdit.setText(pa.cas_filter['noiva'])
        self.casNoivaLogic.setCurrentIndex(pa.cas_filter['noiva_log'])
        self.casPaiNoivoEdit.setText(pa.cas_filter['pai_noivo'])
        self.casPaiNoivoLogic.setCurrentIndex(pa.cas_filter['pai_noivo_log'])
        self.casMaeNoivoEdit.setText(pa.cas_filter['mae_noivo'])
        self.casMaeNoivoLogic.setCurrentIndex(pa.cas_filter['mae_noivo_log'])
        self.casPaiNoivaEdit.setText(pa.cas_filter['pai_noiva'])
        self.casPaiNoivaLogic.setCurrentIndex(pa.cas_filter['pai_noiva_log'])
        self.casMaeNoivaEdit.setText(pa.cas_filter['mae_noiva'])
        self.casMaeNoivaLogic.setCurrentIndex(pa.cas_filter['mae_noiva_log'])
  
    def load_obi_dic(self):
        self.obi_ini_year.setCurrentIndex(pa.obi_filter['ini_year'])
        self.obi_end_year.setCurrentIndex(pa.obi_filter['end_year'])
        self.obi_sortCbx.setCurrentIndex(pa.obi_filter['sort_by'])
        self.obiNomeEdit.setText(pa.obi_filter['nome'])
        # self.obiNomeLogic.setCurrentIndex(pa.obi_filter['nome_log'])
        self.obiConjEdit.setText(pa.obi_filter['conj'])
        self.obiConjLogic.setCurrentIndex(pa.obi_filter['conj_log'])
        self.obiPaiEdit.setText(pa.obi_filter['pai'])
        self.obiPaiLogic.setCurrentIndex(pa.obi_filter['pai_log'])
        self.obiMaeEdit.setText(pa.obi_filter['mae'])
        self.obiMaeLogic.setCurrentIndex(pa.obi_filter['mae_log'])

        
    def run_click (self):
        self.tab = self.tabuladorTabWidget.currentIndex()
        if self.tab == 0:
            self.nas_mk_sql()
        elif self.tab == 1:
            self.cas_mk_sql()
        elif self.tab == 2:
            self.obi_mk_sql()
            
    def nas_mk_sql(self):
        sql = ''
        filter = []
        pa.nas_filter = dict(ini_year=self.nas_ini_year.currentIndex(), end_year=self.nas_end_year.currentIndex(), sort_by=self.nas_sortCbx.currentIndex(),
                             nome=self.nasNomeEdit.text(), pai=self.nasPaiEdit.text(), pai_log=self.nasPaiLogic.currentIndex(), mae=self.nasMaeEdit.text(),
                             mae_log=self.nasMaeLogic.currentIndex(), avo_pat=self.nasAvoPatEdit.text(), avo_pat_log=self.nasAvoPatLogic.currentIndex(),
                             ava_pat=self.nasAvaPatEdit.text(), ava_pat_log=self.nasAvaPatLogic.currentIndex(), avo_mat=self.nasAvoMatEdit.text(),
                             avo_mat_log=self.nasAvoMatLogic.currentIndex(), ava_mat=self.nasAvaMatEdit.text(), ava_mat_log=self.nasAvaMatLogic.currentIndex())
        sql += '''SELECT nas_id, nas_ano, nas_registo, nas_data, nas_nome, nas_pai, nas_mae,
                nas_avo_paterno, nas_avo_paterna, nas_avo_materno, nas_avo_materna from nascimentos
                WHERE nas_ano >= ''' + self.nas_ini_year.currentText() + ''' and  nas_ano <=''' + self.nas_end_year.currentText()
        if not self.nasNomeEdit.text() == '':
            search = '\'%%' + self.nasNomeEdit.text().lower() + '%%\''
            filter.append(' lower(nas_nome) like ''' + search)
        
        if not self.nasPaiEdit.text() == '':
            search = '\'%%' + self.nasPaiEdit.text().lower() + '%%\''
            # print 'logic',self.logic_dict[self.nasPaiLogic.currentIndex()]
            filter.append(self.logic_dict[self.nasPaiLogic.currentIndex()] +  ' lower(nas_pai) like ''' + search)

        if not self.nasMaeEdit.text() == '':
            search = '\'%%' + self.nasMaeEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.nasMaeLogic.currentIndex()] +' lower(nas_mae) like ''' + search)

        if not self.nasAvoPatEdit.text() == '':
            search = '\'%%' + self.nasAvoPatEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.nasAvoPatLogic.currentIndex()] +' lower(nas_avo_paterno) like ''' + search)

        if not self.nasAvaPatEdit.text() == '':
            search = '\'%%' + self.nasAvaPatEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.nasAvaPatLogic.currentIndex()] +' lower(nas_avo_paterna) like ''' + search)

        if not self.nasAvoMatEdit.text() == '':
            search = '\'%%' + self.nasAvoMatEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.nasAvoMatLogic.currentIndex()] +' lower(nas_avo_materno) like ''' + search)

        if not self.nasAvaMatEdit.text() == '':
            search = '\'%%' + self.nasAvaMatEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.nasAvaMatLogic.currentIndex()] +' lower(nas_avo_materna) like ''' + search)
        order_by = ' order by ' + self.nas_order_dic[self.nas_sortCbx.currentIndex()]
        if filter == []:
            self.toto = False,''
        else:
            h = ''.join(filter)
            if h.find('and',0,5) > -1:
                e = ''
            else:
                e = ' and '
            sql += e + h + order_by
            self.toto = True,self.tab,sql
            self.close()

    def cas_mk_sql(self):
        sql = ''
        filter = []
        pa.cas_filter = dict(ini_year=self.cas_ini_year.currentIndex(), end_year=self.cas_end_year.currentIndex(), sort_by=self.cas_sortCbx.currentIndex(),
                             noivo=self.casNoivoEdit.text(),noiva=self.casNoivaEdit.text(), noiva_log=self.casNoivaLogic.currentIndex(), 
                             pai_noivo=self.casPaiNoivoEdit.text(),pai_noivo_log=self.casPaiNoivoLogic.currentIndex(), 
                             mae_noivo=self.casMaeNoivoEdit.text(), mae_noivo_log=self.casMaeNoivoLogic.currentIndex(),
                             pai_noiva=self.casPaiNoivaEdit.text(), pai_noiva_log=self.casPaiNoivaLogic.currentIndex(),
                             mae_noiva=self.casMaeNoivaEdit.text(), mae_noiva_log=self.casMaeNoivaLogic.currentIndex())
                             
        sql += '''SELECT cas_id, cas_ano, cas_registo, cas_data, cas_noivo, cas_noiva, cas_noivo_pai, cas_noivo_mae,
                cas_noiva_pai, cas_noiva_mae from casamentos
                WHERE cas_ano >= ''' + self.cas_ini_year.currentText() + ''' and  cas_ano <=''' + self.cas_end_year.currentText()

        if not self.casNoivoEdit.text() == '':
            search = '\'%%' + self.casNoivoEdit.text().lower() + '%%\''
            filter.append(' lower(cas_noivo) like ''' + search)
        
        if not self.casNoivaEdit.text() == '':
            search = '\'%%' + self.casNoivaEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.casNoivaLogic.currentIndex()] + ' lower(cas_noiva) like ''' + search)
        
        if not self.casPaiNoivoEdit.text() == '':
            search = '\'%%' + self.casPaiNoivoEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.casPaiNoivoLogic.currentIndex()] +  ' lower(cas_noivo_pai) like ''' + search)

        if not self.casMaeNoivoEdit.text() == '':
            search = '\'%%' + self.casMaeNoivoEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.casMaeNoivoLogic.currentIndex()] +' lower(cas_noivo_mae) like ''' + search)

        if not self.casPaiNoivaEdit.text() == '':
            search = '\'%%' + self.casPaiNoivaEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.casPaiNoivaLogic.currentIndex()] +  ' lower(cas_noiva_pai) like ''' + search)

        if not self.casMaeNoivaEdit.text() == '':
            search = '\'%%' + self.casMaeNoivaEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.casMaeNoivaLogic.currentIndex()] +' lower(cas_noiva_mae) like ''' + search)

        order_by = ' order by ' + self.cas_order_dic[self.cas_sortCbx.currentIndex()]

        if filter == []:
            self.toto = False,''
        else:
            h = ''.join(filter)
            if h.find('and',0,5) > -1:
                e = ''
            else:
                e = ' and '
            sql += e + h + order_by
            self.toto = True,self.tab,sql
            self.close()

    def obi_mk_sql(self):
        sql = ''
        filter = []
        pa.obi_filter = dict(ini_year=self.obi_ini_year.currentIndex(), end_year=self.obi_end_year.currentIndex(), sort_by=self.obi_sortCbx.currentIndex(),
                             nome=self.obiNomeEdit.text(), conj=self.obiConjEdit.text(), conj_log=self.obiConjLogic.currentIndex(), 
                             mae=self.obiMaeEdit.text(),
                             mae_log=self.obiMaeLogic.currentIndex(),
                             pai=self.obiPaiEdit.text(), pai_log=self.obiPaiLogic.currentIndex())
        sql += '''SELECT obi_id, obi_ano, obi_registo, obi_data, obi_nome, obi_conj, obi_pai, obi_mae
                from obitos
                WHERE obi_ano >= ''' + self.obi_ini_year.currentText() + ''' and  obi_ano <=''' + self.obi_end_year.currentText()
        if not self.obiNomeEdit.text() == '':
            search = '\'%%' + self.obiNomeEdit.text().lower() + '%%\''
            filter.append(' lower(obi_nome) like ''' + search)
        
        if not self.obiConjEdit.text() == '':
            search = '\'%%' + self.obiConjEdit.text().lower() + '%%\''
            # print 'logic',self.logic_dict[self.obiPaiLogic.currentIndex()]
            filter.append(self.logic_dict[self.obiConjLogic.currentIndex()] +  ' lower(obi_conj) like ''' + search)

        if not self.obiPaiEdit.text() == '':
            search = '\'%%' + self.obiPaiEdit.text().lower() + '%%\''
            # print 'logic',self.logic_dict[self.obiPaiLogic.currentIndex()]
            filter.append(self.logic_dict[self.obiPaiLogic.currentIndex()] +  ' lower(obi_pai) like ''' + search)

        if not self.obiMaeEdit.text() == '':
            search = '\'%%' + self.obiMaeEdit.text().lower() + '%%\''
            filter.append(self.logic_dict[self.obiMaeLogic.currentIndex()] +' lower(obi_mae) like ''' + search)

        order_by = ' order by ' + self.obi_order_dic[self.obi_sortCbx.currentIndex()]
        if filter == []:
            self.toto = False,''
        else:
            h = ''.join(filter)
            if h.find('and',0,5) > -1:
                e = ''
            else:
                e = ' and '
            sql += e + h + order_by
            self.toto = True,self.tab,sql
            self.close()

    def exitClick (self):
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addHDumLayout(self, listobj1, label_size = 120, label_align = Qt.AlignVCenter|Qt.AlignRight):
        """ v 2.0 SET2012"""  
        dumLayout = QHBoxLayout()
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

def main():
    pa.config = settings.ini_file_to_dic(settings.read_config_file('config.ini'))
    pa.conn_string = "host=" +  pa.config['host'] + " dbname=" + pa.config['dbname'] + " user=root password=masterkey"

    app = QApplication(sys.argv)
    form = SearchEngine()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

