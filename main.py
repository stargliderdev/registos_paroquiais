#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime
import os
import ftplib
import subprocess
import base64

from PyQt5.QtWidgets import QDesktopWidget, QLabel, QVBoxLayout, QComboBox, \
    QTableWidget, QPushButton, QHBoxLayout, QTableWidgetItem, \
    QWidget, QTabWidget, QApplication, QMessageBox, QStyleFactory, QDialog
from PyQt5.Qt import Qt


import parameters as pa
import libpg
import stdio
import lib_paroquia
import settings
import nas_ficha
import cas_ficha
import insert_record
import filter
import ex_grid
import qlib


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        screen = QDesktopWidget().screenGeometry()
        self.resize(1280, 1024)
        # self.showMaximized()

        self.setWindowTitle('Registos Paroquiais')
        self.mainLayout = QVBoxLayout(self)
        # self.html_view = None
        # self.gridNascimentos = None
        # self.tipo = 0
        # self.current_output = 0  # 0 gridNascimentos, 1 html
        self.nas_order_dict = pa.nas_order_dic
        self.nas_order_items = pa.nas_order_items
        self.cas_order_dict = pa.cas_order_dic
        self.cas_order_items = pa.cas_order_items
        self.obi_order_dict = pa.obi_order_dic
        self.obi_order_items = pa.obi_order_items
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        insertBtn = QPushButton('Inserir Acento')
        insertBtn.clicked.connect(self.insert_record_click)

        refreshBtn = QPushButton('Actualiza')
        refreshBtn.clicked.connect(self.view_as_gridNascimentos)

        # view_as_gridNascimentosBtn = QPushButton('Grelha')
        # self.connect(view_as_gridNascimentosBtn, SIGNAL("clicked()"), self.view_as_gridNascimentos)

        viewHTMLBtn = QPushButton('Relatório')
        # self.connect(viewHTMLBtn, SIGNAL("clicked()"), self.view_as_HTML)
        viewHTMLBtn.clicked.connect(self.view_as_HTML)
        

        filterBtn = QPushButton('Filtro')
        # self.connect(filterBtn, SIGNAL("clicked()"), self.filter_click)
        filterBtn.clicked.connect(self.filter_click)
        
        backup_dbBtn = QPushButton('Cópia de Segurança')
        # self.connect(backup_dbBtn, SIGNAL("clicked()"), self.backup_c_click)
        # back.clicked.connect(self.)
        
        # info_Btn = QPushButton(u'Info')
        # self.connect(info_Btn, SIGNAL("clicked()"), self.info_click)

        exitBtn = QPushButton('Sair')
        # self.connect(exitBtn, SIGNAL("clicked()"), self.exit_click)
        exitBtn.clicked.connect(self.exit_click)
        

        self.mainLayout.addLayout(
            self.addHDumLayout([insertBtn, refreshBtn,  viewHTMLBtn, filterBtn, True, backup_dbBtn, exitBtn]))

        self.tabuladorTabWidget = QTabWidget()
        self.mainLayout.addWidget(self.tabuladorTabWidget)

        self.make_nas_tab()
        self.tabuladorTabWidget.addTab(self.tab1, 'Nascimentos')

        self.make_cas_tab()
        self.tabuladorTabWidget.addTab(self.tab2, 'Casamentos')

        self.make_obi_tab()
        self.tabuladorTabWidget.addTab(self.tab3, 'Óbitos')

    def make_nas_tab(self):
        self.tab1 = QWidget()
        mainTabLayout = QVBoxLayout(self.tab1)
        self.gridNascimentos = QTableWidget()
        self.nas_anoCB = QComboBox()
        self.nas_anoCB.setEditable(True)
        self.nas_anoCB.addItems(pa.nascimentos_anos)
        self.nas_anoCB.setEditText(str(pa.nas_year))
        # self.connect(self.nas_anoCB, SIGNAL("currentIndexChanged(QString)"), self.nas_anoCB_change)
        self.nas_anoCB.currentIndexChanged.connect(self.nas_anoCB_change)
        

        self.nas_sort_byCB = QComboBox()
        self.nas_sort_byCB.addItems(self.nas_order_items)
        self.nas_sort_byCB.setCurrentIndex(1)
        self.nas_sort_byCB.currentIndexChanged.connect(self.nas_anoCB_change)
        
        mainTabLayout.addLayout(qlib.addHLayout(['Ano:',self.nas_anoCB,'Ordena por:',self.nas_sort_byCB, True]))
        mainTabLayout.addWidget(self.gridNascimentos)
        self.gridNascimentos.setSelectionBehavior(QTableWidget.SelectRows)
        self.gridNascimentos.setSelectionMode(QTableWidget.SingleSelection)
        self.gridNascimentos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.gridNascimentos.verticalHeader().setDefaultSectionSize(20)
        self.gridNascimentos.setAlternatingRowColors(True)
        self.gridNascimentos.verticalHeader().setVisible(False)
        self.update_gridNascimentos()
        mainTabLayout.addWidget(self.gridNascimentos)
        self.gridNascimentos.itemDoubleClicked.connect(self.gridNascimentos_double_click)
        

    def make_cas_tab(self):
        self.tab2 = QWidget()
        mainTabLayout = QVBoxLayout(self.tab2)
        self.gridCasamentos = QTableWidget()
        self.cas_anoCB = QComboBox()
        self.cas_anoCB.setEditable(True)
        self.cas_anoCB.addItems(pa.casamentos_anos)
        self.cas_anoCB.setEditText(str(pa.cas_year))

        self.cas_sort_byCB = QComboBox()
        self.cas_sort_byCB.addItems(self.cas_order_items)
        self.cas_sort_byCB.setCurrentIndex(0)
        mainTabLayout.addLayout(qlib.addHLayout(['Ano:',self.cas_anoCB,'Ordena por:',self.cas_sort_byCB, True]))
  
        mainTabLayout.addWidget(self.gridCasamentos)
        self.gridCasamentos.setSelectionBehavior(QTableWidget.SelectRows)
        self.gridCasamentos.setSelectionMode(QTableWidget.SingleSelection)
        self.gridCasamentos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.gridCasamentos.verticalHeader().setDefaultSectionSize(20)
        self.gridCasamentos.setAlternatingRowColors(True)
        self.gridCasamentos.verticalHeader().setVisible(False)
        self.update_gridCasamentos()
        mainTabLayout.addWidget(self.gridCasamentos)
        self.gridCasamentos.itemDoubleClicked.connect(self.gridCasamentos_double_click)

    def make_obi_tab(self):
        self.tab3 = QWidget()
        mainTabLayout = QVBoxLayout(self.tab3)
        self.gridObitos = QTableWidget()
        self.obi_anoCB = QComboBox()
        self.obi_anoCB.setEditable(True)
        self.obi_anoCB.addItems(pa.obitos_anos)
        self.obi_anoCB.setEditText(str(pa.obi_year))
        self.obi_sort_byCB = QComboBox()
        self.obi_sort_byCB.addItems(self.obi_order_items)
        self.obi_sort_byCB.setCurrentIndex(0)
        mainTabLayout.addLayout(qlib.addHLayout(['Ano:',self.obi_anoCB,'Ordena por:',self.obi_sort_byCB, True]))

        mainTabLayout.addWidget(self.gridObitos)
        self.gridObitos.setSelectionBehavior(QTableWidget.SelectRows)
        self.gridObitos.setSelectionMode(QTableWidget.SingleSelection)
        self.gridObitos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.gridObitos.verticalHeader().setDefaultSectionSize(20)
        self.gridObitos.setAlternatingRowColors(True)
        self.gridObitos.verticalHeader().setVisible(False)
        self.update_gridObitos()
        mainTabLayout.addWidget(self.gridObitos)

    def filter_click(self):
        tab =self.tabuladorTabWidget.currentIndex()
        form = filter.SearchEngine(tab)
        form.exec_()
        if form.toto[0]:
            tab = form.toto[1]
            self.tabuladorTabWidget.setCurrentIndex(tab)
            if form.toto[0]:
                if tab == 0:
                    ex_grid.ex_grid_update(self.gridNascimentos, {0: ['Int.', 'i'], 1: ['Ano', 'i'], 2: ['Registo', 'i'], 3: ['Data', 'sc'],
                                                   4: ['Nome', 's'], 5: ['Pai', 's'], 6: ['Mãe', 's'], 7: ['Avô Paterno', 's'],
                                                   8: ['Avó Paterna', 's'], 9: ['Avô Materno', 's'], 10: ['Avó Materna', 's']},
                                       libpg.output_query_many(form.toto[2], (True,)))
                elif tab == 1:
                    ex_grid.ex_grid_update(self.gridCasamentos, {0: ['Int.', 'i'], 1: ['Ano', 'i'], 2: ['Registo', 'i'], 3: ['Data', 'd'],
                                                   4: ['Noivo', 's'], 5: ['Noiva', 's'], 6: ['Pai do Noivo', 's'], 7: ['Mãe do Noivo', 's'],
                                                   8: ['Pai da Noiva', 's'], 9: ['Mãe da Noiva', 's']},
                                       libpg.output_query_many(form.toto[2], (True,)))
                elif tab == 2:
                    ex_grid.ex_grid_update(self.gridObitos, {0: ['Int.', 'i'], 1: ['Ano', 'i'], 2: ['Registo', 'i'], 3: ['Data', 'd'],
                                                   4: ['Nome', 's'], 5:['Conjugue', 's'], 6: ['Pai', 's'], 7: ['Mãe', 's']},
                                       libpg.output_query_many(form.toto[2], (True,)))

    def insert_record_click(self):
        form = insert_record.NewRecord()
        form.exec_()
        toto = form.toto
        if toto['ano'] == -1:
            pass
        else:
            # 'cria o registo'
            # 'abre form apontando para esse registo'
            # QObject.disconnect(self.nas_anoCB, SIGNAL("currentIndexChanged(QString)"), self.nas_anoCB_change)
            libpg.execute_query('INSERT into nascimentos (nas_ano, nas_registo, nas_folha,nas_data_baptismo,nas_local) VALUES (%s, %s, %s,%s,%s)',
                                (toto['ano'], toto['reg'], toto['folha'], '01-01-' + str(toto['ano']), 76))
            pa.last_year = toto['ano']
            pa.current_index = -1
            pa.current_dataset_limit = -99999
            pa.current_record = lib_paroquia.get_max_record('nascimentos', 'nas_id')[0]
            pa.nascimentos_rec = lib_paroquia.get_nascimentos_data(pa.current_record)
            form = nas_ficha.Dialog(pa.current_record)
            form.exec_()
            if not pa.last_year in pa.nascimentos_anos:
                self.nas_anoCB.clear()
                pa.nascimentos_anos.append(str(pa.last_year))
                self.nas_anoCB.addItems(pa.nascimentos_anos)
                self.nas_anoCB.setEditText(str(pa.last_year))
                self.nas_anoCB_change(pa.last_year)
            else:
                self.nas_anoCB_change(pa.last_year)
            self.nas_anoCB.currentIndexChanged.connect(self.nas_anoCB)
            

    def gridNascimentos_double_click(self):
        nas_id = int(self.gridNascimentos.item(self.gridNascimentos.currentRow(), 0).text())
        pa.current_record = nas_id
        form = nas_ficha.Dialog(nas_id)
        form.exec_()
        self.view_as_gridNascimentos()
    
    def gridCasamentos_double_click(self):
        index = int(self.gridCasamentos.item(self.gridCasamentos.currentRow(), 0).text())
        nas_id = index
        form = cas_ficha.Dialog(index)
        form.exec_()
        self.view_as_gridNascimentos()

    def view_as_HTML(self):
        # self.gridNascimentos_to_html()
        h = []
        cols = self.gridNascimentos.columnCount()
        for n in range(0, cols):
            h.append(str(self.gridNascimentos.horizontalHeaderItem(n).text()))
        # print (h)
        ds = []
        for linha in range(0, self.gridNascimentos.rowCount()-1):
            dum = ()
            for c in range(0,cols):
                if self.gridNascimentos.item(linha, c) is not None:
                    dum = dum + (str(self.gridNascimentos.item(linha, c).text()).encode('utf-8'),)
                    # ds.append(self.gridNascimentos.item(linha, c).text())
                else:
                    dum = dum + (' ',)
                    # ds.append((''))

            ds.append(dum)
        # print ds

        import libreports
        toto = libreports.buildReport()
        toto.set_css()
        #
        toto.table(ds, h)
        # ds = []
        # ds.append((u'Versão da db', str(settings.read(0)[1])))
        # ds.append((u'Versão do exe ', str(settings.read(3)[1])))
        # ds.append((u'Registos de Nascimentos:', stdio.int_format(lib_paroquia.get_max_record('nascimentos', 'nas_id')[0])))
        # ds.append(( u'Registos de Casamentos:', stdio.int_format(lib_paroquia.get_max_record('casamentos', 'cas_id')[0])))
        # ds.append(( u'Registos de Óbitos:', stdio.int_format(lib_paroquia.get_max_record('obitos', 'obi_id')[0])))
        # ds.append(( u'Total de locais:', stdio.int_format(lib_paroquia.get_max_record('locais', 'id')[0])))
        # ds.append(( u'Total de profissões:', stdio.int_format(lib_paroquia.get_max_record('profissoes', 'prof_id')[0])))
        # ds.append(( u'Total de parocos:', stdio.int_format(lib_paroquia.get_max_record('padres', 'pa_id')[0])))
        # toto.vertical_grid(ds)
        toto.close()
        # stdio.print2file('test.html', toto.output)
        import browser
        form = browser.Browser(toto.output,'Acentos')
        form.exec_()


    def update_gridNascimentos(self):
        ds = make_dataset(lib_paroquia.nascimentos_filtro(self.nas_order_dict[self.nas_sort_byCB.currentIndex()] ,self.nas_anoCB.currentText()))
        ex_grid.ex_grid_update(self.gridNascimentos, {0: ['Int.', 'i'], 1: ['Registo', 'i'], 2: ['Folha', 's'], 3: ['Data', 'sc'], 4: ['Baptismo', 'd'],
                               5: ['Nome', 's'], 6: ['Filho', 'i'], 7: ['Sexo', 's'], 8: ['Pai', 's'], 9: ['Mãe', 's']},ds)

    def update_gridCasamentos(self):
        ds = make_dataset(lib_paroquia.casamentos_filtro(self.cas_order_dict[self.cas_sort_byCB.currentIndex()] ,
                                                         self.cas_anoCB.currentText()))
        ex_grid.ex_grid_update(self.gridCasamentos, {0: ['Int.', 'i'], 1: ['Registo', 'i'], 2: ['Folha', 's'], 3: ['Data', 'd'],
                      4: ['Noivo', 's'],5: ['Noiva', 's'], 6: ['Pai do Noivo', 's'], 7: ['Mãe do Noivo', 's'], 8: ['Pai da Noiva', 's'], 9: ['Mãe da noiva', 's']},ds)

    def update_gridObitos(self):
        ds = make_dataset(lib_paroquia.obitos_filtro(self.obi_order_dict[self.obi_sort_byCB.currentIndex()],
                                                     self.obi_anoCB.currentText()))
        ex_grid.ex_grid_update(self.gridObitos, {0: ['Int.', 'i'], 1: ['Registo', 'i'], 2: ['Folha', 's'], 3: ['Data', 'd'],
                      4: ['Nome', 's'],5: ['Conjuge', 's'], 6: ['Pai', 's'], 7: ['Mãe', 's']},ds)

    def nas_anoCB_change(self, t):
        self.update_gridNascimentos()
        settings.write(1, int(self.nas_anoCB.currentText()))
        pa.nas_year = int(self.nas_anoCB.currentText())

    def cas_anoCB_change(self, t):
        self.update_gridCasamentos()
        settings.write(2, int(self.cas_anoCB.currentText()))
        pa.cas_year = int(self.cas_anoCB.currentText())

    def obi_anoCB_change(self, t):
        self.update_gridObitos()
        settings.write(3, int(self.obi_anoCB.currentText()))
        pa.obi_year = int(self.obi_anoCB.currentText())

    def view_as_gridNascimentos(self):
        if self.gridNascimentos == None:
            self.mainLayout.removeWidget(self.html_view)
            self.html_view.deleteLater()
            self.html_view = None
            self.make_gridNascimentos(0)
            self.mainLayout.addWidget(self.gridNascimentos)
            # self.connect(self.gridNascimentos, SIGNAL("itemDoubleClicked(QTableWidgetItem*)"), self.gridNascimentos_double_click)
            self.refresh_gridNascimentos(make_dataset(lib_paroquia.nascimentos_filtro('', self.nas_anoCB.currentText())))
        self.current_output = 0

    def make_gridNascimentos(self, tipo=0):
        """ type:0 nascimentos"""
        self.gridNascimentos = QTableWidget(self)
        # if tipo == 0:
        #     ex_grid.ex_grid_update(self.gridNascimentos, {0: ['ID', 'i'], 1: ['Nome', 's']}, ds)
        #     lineHeaders = ['Int.', 'Ano', 'Registo', 'Folha', 'Data', 'Baptismo', 'Nome', 'Filho', 'Sexo', 'Pai', 'Mãe']
        # colCount = len(lineHeaders)
        # self.gridNascimentos.setColumnCount(len(lineHeaders))
        self.gridNascimentos.setSelectionBehavior(QTableWidget.SelectRows)
        self.gridNascimentos.setSelectionMode(QTableWidget.SingleSelection)
        self.gridNascimentos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.gridNascimentos.verticalHeader().setDefaultSectionSize(20)
        self.gridNascimentos.setAlternatingRowColors(True)
        self.gridNascimentos.verticalHeader().setVisible(False)
        # self.gridNascimentos.setHorizontalHeaderLabels(lineHeaders)


    def refresh_gridNascimentos(self, data_set):
        self.gridNascimentos.setRowCount(len(data_set))
        linha = 0
        pa.current_dataset = []
        for n in data_set:
            pa.current_dataset.append(n[0])
            self.format_cell(n[0], linha, 0)
            self.format_cell(n[1], linha, 1)
            self.format_cell(n[2], linha, 2)
            self.format_cell(n[3], linha, 3)
            self.format_cell(n[4], linha, 4)
            self.format_cell(n[5], linha, 5)
            self.format_cell(n[6], linha, 6)
            self.format_cell(n[7], linha, 7)
            self.format_cell(n[8], linha, 8)
            self.format_cell(n[9], linha, 9)
            self.format_cell(n[10], linha, 10)
            linha += 1
        self.gridNascimentos.resizeColumnsToContents()

    def format_cell(self, cell_data, linha, col):
        """ forma cell v1 21DEZ2013 """
        self.item = QTableWidgetItem()
        self.gridNascimentos.setItem(linha, col, self.item)

        if type(cell_data) == int:
            self.item.setText(cell_data)
            self.item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        elif type(cell_data) == datetime.datetime:
            self.item.setText("%02d.%02d.%02d" % (cell_data.day, cell_data.month, cell_data.year))
            # cell_data.strftime('%Y-%m-%d'))
        elif cell_data == None:
            self.item.setText('-')
        else:
            self.item.setText(cell_data)

    def backup_c_click(self):
        tdate = stdio.time_format_militar(datetime.datetime.now())
        backup_file = 'c:\\backup\\' + pa.config['dbname'] + '_' + tdate + '.backup'

        # run_normal('c://programas//postgresql//8.1//bin//' + 'pg_dump.exe -U "sysdba" --format custom --blobs --inserts --column-inserts --verbose  --file ' + backup_file + ' "registos_paroquiais"')
        run_normal(pa.pg_dump + 'pg_dump.exe -U "sysdba" --format custom --blobs --inserts --column-inserts --verbose  --file ' + backup_file + ' "registos_paroquiais"')
        file_ftp = backup_file
        file_name = file_ftp[file_ftp.rfind('\\') + 1:]
        # toto += 'contacta servidor<br>'
        # self.html_view.setHtml(toto)
        # self.html_view.repaint()

        # session = ftplib.FTP('espiridiao.net','gerencia@espiridiao.net','1697fo__')
        session = ftplib.FTP(base64.b64decode('ZXNwaXJpZGlhby5uZXQ='),
                             base64.b64decode('Z2VyZW5jaWFAZXNwaXJpZGlhby5uZXQ='),
                             base64.b64decode('MTY5N2ZvX18='))
        myfile = open(file_ftp, 'rb')
        session.storbinary('STOR ' + file_name, myfile)
        myfile.close()
        session.quit()
        reply = QMessageBox.information(self,
                "Backup efectuado com sucesso","Backup efectuado com sucesso" )
        # toto += 'backup efectuado com sucesso<br> ' + file_name
        # self.html_view.setHtml(toto)
        # self.html_view.repaint()

    # def info_click(self):
    #     if not self.gridNascimentos == None:
    #         self.mainLayout.removeWidget(self.gridNascimentos)
    #         self.gridNascimentos.deleteLater()
    #         self.gridNascimentos = None
    #         self.html_view = QWebView()
    #         self.mainLayout.addWidget(self.html_view)
    #     ds = []
    #     ds.append(('Versão da db', settings.read(0)[1]))
    #     ds.append(('Versão do exe ', settings.read(3)[1]))
    #     ds.append(('Registos de Nascimentos:', stdio.int_format(lib_paroquia.get_max_record('nascimentos', 'nas_id')[0])))
    #     ds.append(( 'Registos de Casamentos:', stdio.int_format(lib_paroquia.get_max_record('casamentos', 'cas_id')[0])))
    #     ds.append(( 'Registos de Óbitos:', stdio.int_format(lib_paroquia.get_max_record('obitos', 'obi_id')[0])))
    #     ds.append(( 'Total de locais:', stdio.int_format(lib_paroquia.get_max_record('locais', 'id')[0])))
    #     ds.append(( 'Total de profissões:', stdio.int_format(lib_paroquia.get_max_record('profissoes', 'prof_id')[0])))
    #     ds.append(( 'Total de parocos:', stdio.int_format(lib_paroquia.get_max_record('padres', 'pa_id')[0])))
    #     import libreports
    #     toto = libreports.buildReport()
    #     toto.vertical_gridNascimentos(ds)
    #     toto.close()
    #
    #     self.html_view.setHtml(toto.output)  #, u)
    #     self.html_view.repaint()
    #     # print str(settings.read(0)[1])

    def exit_click(self):
        self.close()

    def addHDumLayout(self, listobj1, label_size=90, align=Qt.AlignVCenter | Qt.AlignRight):
        """ v 2.0 SET2012"""
        dumLayout = QHBoxLayout()
        for n in listobj1:
            if (type(n) == str) or (type(n) == str):
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

    def addVDumLayout(self, listobj1, label_size=120, align=Qt.AlignVCenter | Qt.AlignRight):
        """ v 2.0 SET2012"""
        dumLayout = QVBoxLayout()
        for n in listobj1:
            if (type(n) == str) or (type(n) == str):
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


def make_records_year():
    series = {}

    obi_por_ano = libpg.output_query_many('''SELECT obi_ano, count(obi_id) contagem
             from obitos
             GROUP by obi_ano
             order by obi_ano desc''', (True,))
    for n in obi_por_ano:
        if n[0] in series:
            dum = series[n[0]]
            series.update({n[0]: (dum[0], dum[1], n[1])})
        else:
            series[n[0]] = (0, 0, n[1])

    nas_por_ano = libpg.output_query_many('''SELECT nas_ano, count(nas_id) contagem
             from nascimentos
             GROUP by nas_ano
             order by nas_ano desc''', (True,))
    for n in nas_por_ano:
        if n[0] in series:
            dum = series[n[0]]
            series.update({n[0]: (n[1], dum[1], dum[2])})
        else:
            series[n[0]] = (n[1], 0, 0)
    cas_por_ano = libpg.output_query_many('''SELECT cas_ano, count(cas_id) contagem
             from casamentos
             GROUP by cas_ano
             order by cas_ano desc''', (True,))
    for n in cas_por_ano:
        if n[0] in series:
            dum = series[n[0]]
            series.update({n[0]: (dum[0], n[1], dum[2])})
        else:
            series[n[0]] = (0, n[1], 0)

    y = ''
    nas = ''
    cas = ''
    obi = ''
    for key, value in series.items():
        y += str(key) + ','
        nas += str(value[0]) + ','
        cas += str(value[1]) + ','
        obi += str(value[2]) + ','

    return y, nas, cas, obi


def run_normal(command):
    os.system(command)


def run_silent(command):
    try:
        toto = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = toto.stdout.readlines()
        return True
    except Exception as err:
        stdio.log_write('error.log', str(err) + '\n')
        return False


def make_dataset(sql):
    data = libpg.output_query_many(sql, (True,))

    return data


def main():
    pa.config = settings.ini_file_to_dic(settings.read_config_file('config.ini'))
    pa.conn_string = "host=" + pa.config['host'] + " dbname=" + pa.config['dbname'] + " user=root " + " password=" + pa.config['password']
    pa.nas_year = settings.read(1)[1]
    pa.cas_year = settings.read(2)[1]
    pa.obi_year = settings.read(3)[1]
    pa.pg_dump = settings.read(4)[1]
    pa.current_dataset = []
    pa.javascript_path = settings.read(4)[1]
    pa.dsSexo = ['Masculino', 'Feminino']
    pa.sexo_dict = {'Masculino': 1, 'Feminino': 2}
    pa.nascimentos_anos = lib_paroquia.get_nascimentos_anos()
    pa.casamentos_anos = lib_paroquia.get_casamentos_anos()
    pa.obitos_anos = lib_paroquia.get_obitos_anos()
    lib_paroquia.get_estados()
    lib_paroquia.get_locais()
    lib_paroquia.get_profissoes()
    lib_paroquia.get_padres()
    lib_paroquia.get_causas()

    # make_records_year()
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


main()
