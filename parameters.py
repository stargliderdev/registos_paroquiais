#!/usr/bin/python
# -*- coding: utf-8 -*-
VERSIO = '21-01-2019'
nas_year = 0
cas_year = 0
obi_year = 0
nas_filter = {}
cas_filter = {}
obi_filter = {}
nascimentos_anos = []
casamentos_anos = []
obitos_anos = []
last_year = 0
pg_dump = ''
config = ''
current_record =0
nas_order_dic = {0: 'nas_nome', 1:'nas_pai',2:'nas_mae',3:'nas_avo_paterno',4:'nas_avo_paterna',5:'nas_avo_materno',6:'nas_avo_materna',
                           7:'nas_ano'}
nas_order_items =['Nome','Pai','Mãe','Avô Paterno','Avó Paterna','Avô Materno',
            'Avó Materna','Ano']
cas_order_dic = {0: 'cas_noivo', 1:'cas_noiva',2:'cas_noivo_pai',3:'cas_noivo_mae',4:'cas_noiva_pai',5:'cas_noiva_mae',6:'cas_ano'}
cas_order_items =['Noivo','Noiva','Pai do Noivo','Mãe do Noivo','Pai da Noiva','Mãe da Noiva','Ano']
obi_order_dic = {0: 'obi_nome', 1:'obi_conj',2:'obi_pai',3:'obi_mae',4:'obi_ano'}
obi_order_items =['Nome','Conjugue','Pai','Mãe','Ano']