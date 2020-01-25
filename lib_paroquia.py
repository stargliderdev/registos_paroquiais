#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parameters as pa
import libpg

def get_nascimentos_anos():
    sql = 'select nas_ano from nascimentos\
        GROUP by nas_ano order by nas_ano desc'
    d = libpg.output_query_many(sql,(True,))
    toto = []
    for n in d:
        toto.append(str(n[0]))

    return toto

def nascimentos_filtro(order_by,ano):
    sql = '''SELECT
          nas_id ,
          nas_registo,
          nas_folha,
          nas_data ,
          nas_data_baptismo ,
          nas_nome,
          nas_numero_filho ,
          (select sexo from sexo where id=nas_sexo) as nas_sexo ,
          nas_pai,
          nas_mae
          from nascimentos '''

    sql += ' where nas_ano = ' + str(ano)
    sql += ' order by ' + order_by

    return sql

def get_casamentos_anos():
    sql = '''select cas_ano from casamentos
        GROUP by cas_ano order by cas_ano desc'''
    d = libpg.output_query_many(sql,(True,))
    toto = []
    for n in d:
        toto.append(str(n[0]))
    return toto

def casamentos_filtro(order_by,ano):
    sql = '''SELECT
          cas_id ,
          cas_registo,
          cas_folha,
          cas_data,
          cas_noivo,
          cas_noiva,
          cas_noivo_pai,
          cas_noivo_mae,
         cas_noiva_pai,
          cas_noiva_mae
          from casamentos '''

    sql += ' where cas_ano = ' + str(ano)
    sql += ' order by ' + order_by
    return sql

def obitos_filtro(order_by,ano):
    sql = '''SELECT
          obi_id ,
          obi_registo,
          obi_folha,
          obi_data,
          obi_nome,
          obi_conj,
          obi_pai,
          obi_mae
          from obitos'''

    sql += ' where obi_ano = ' + str(ano)
    sql += ' order by ' + order_by
    return sql

def get_obitos_anos():
    sql = '''select obi_ano from obitos
        GROUP by obi_ano order by obi_ano desc'''
    d = libpg.output_query_many(sql,(True,))
    toto = []
    for n in d:
        toto.append(str(n[0]))
    return toto

def get_locais():
    a = libpg.output_query_many('select id,local from locais order by local',(True,))
    pa.dsLocais = []
    pa.locais_dict = {}
    for n  in a:
        pa.locais_dict[n[1]] = n[0]
        pa.dsLocais.append(n[1])

def get_profissoes():
    a = libpg.output_query_many('select prof_id,prof from profissoes order by prof',(True,))
    pa.dsProfissoes = []
    pa.profissoes_dict = {}
    for n  in a:
        pa.profissoes_dict[n[1]] = n[0]
        pa.dsProfissoes.append(n[1])
def get_padres():
    a = libpg.output_query_many('select pa_id,pa_nome from padres order by pa_nome',(True,))
    pa.dsPadres = []
    pa.padres_dict = {}
    for n  in a:
        pa.padres_dict[n[1]] = n[0]
        pa.dsPadres.append(n[1])
def get_causas():
    a = libpg.output_query_many('select cm_id,cm_causa_morte from causasmorte',(True,))
    pa.dsCausas = []
    pa.causas_dict = {}
    for n  in a:
        pa.causas_dict[n[1]] = n[0]
        pa.dsCausas.append(n[1])
def get_estados():
    a = libpg.output_query_many('select id,estado from estados',(True,))
    pa.dsEstados = []
    pa.estados_dict = {}
    for n  in a:
        pa.estados_dict[n[1]] = n[0]
        pa.dsEstados.append(n[1])
       
def get_max_record(table,field):
    sql = 'select max(' + field + ') from ' + table
    return libpg.output_query_one(sql,(True,))




def get_nascimentos_data(index):
    # get a connection, if a connect cannot be made an exception will be raised here
    # conn = psycopg2.connect(pa.conn_string)
    # dict_cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    sql = '''SELECT
          nas_id ,
          nas_num ,
          nas_ano,
          nas_registo,
          nas_folha,
          nas_data_baptismo ,
          nas_data_nascimento ,
          nas_data ,
          (select local from locais where id = nas_local) as nas_local ,
          nas_nome,
          nas_numero_filho ,
          (select sexo from sexo where id=nas_sexo) as nas_sexo ,
          nas_pais_casados ,
          nas_pai,
          nas_pai_idade ,
          (select estado from estados where id=nas_pai_estado) as nas_pai_estado ,
          (select local from locais where id = nas_pai_nat) as nas_pai_nat ,
          (select local from locais where id = nas_pai_res) as nas_pai_res ,
          (select prof from profissoes where prof_id = nas_pai_prof) as nas_pai_prof ,
          nas_mae,
          (select local from locais where id = nas_mae_nat) as nas_mae_nat ,
          (select local from locais where id = nas_mae_res) as nas_mae_res ,
          (select prof from profissoes where prof_id = nas_mae_prof) as nas_mae_prof ,
          nas_avo_paterno ,
          (select prof from profissoes where prof_id = nas_avo_paterno_prof) as nas_avo_paterno_prof ,
          (select local from locais where id = nas_avo_paterno_nat) as nas_avo_paterno_nat ,
          (select local from locais where id = nas_avo_paterno_res) as nas_avo_paterno_res ,
          nas_avo_paterna ,
          (select prof from profissoes where prof_id = nas_avo_paterna_prof) as nas_avo_paterna_prof ,
          (select local from locais where id = nas_avo_paterna_nat) as nas_avo_paterna_nat ,
          (select local from locais where id = nas_avo_paterna_res) as nas_avo_paterna_res ,
          nas_avo_materno,
          (select prof from profissoes where prof_id = nas_avo_materno_prof) as nas_avo_materno_prof ,
          (select local from locais where id = nas_avo_materno_nat) as nas_avo_materno_nat ,
          (select local from locais where id = nas_avo_materno_res) as nas_avo_materno_res ,
          nas_avo_materna,
          (select prof from profissoes where prof_id = nas_avo_materna_prof) as nas_avo_materna_prof ,
          (select local from locais where id = nas_avo_materna_nat) as nas_avo_materna_nat ,
          (select local from locais where id = nas_avo_materna_res) as nas_avo_materna_res ,
          nas_padrinho,
          (select estado from estados where id=nas_padrinho_estado) as nas_padrinho_estado ,
          (select prof from profissoes where prof_id = nas_padrinho_prof) as nas_padrinho_prof ,
          (select local from locais where id = nas_padrinho_res) as nas_padrinho_res ,
          nas_padrinho_assinou ,
          nas_madrinha,
          (select estado from estados where id=nas_madrinha_estado) as nas_madrinha_estado ,
          (select prof from profissoes where prof_id = nas_madrinha_prof) as nas_madrinha_prof ,
          (select local from locais where id = nas_madrinha_res) as nas_madrinha_res ,
          nas_madrinha_assinou ,
          nas_t1,
          (select prof from profissoes where prof_id = nas_t1_prof) as nas_t1_prof ,
          (select local from locais where id = nas_t1_res) as nas_t1_res ,
          (select estado from estados where id=nas_t1_estado) as nas_t1_estado ,
          nas_t2,
          (select prof from profissoes where prof_id = nas_t2_prof) as nas_t2_prof ,
          (select local from locais where id = nas_t2_res) as nas_t2_res ,
          (select estado from estados where id=nas_t2_estado) as nas_t2_estado ,
          nas_t3,
          (select prof from profissoes where prof_id = nas_t3_prof) as nas_t3_prof ,
          (select local from locais where id = nas_t3_res) as nas_t3_res ,
          (select estado from estados where id=nas_t3_estado) as nas_t3_estado ,
          nas_t4,
          (select prof from profissoes where prof_id = nas_t4_prof) as nas_t4_prof ,
          (select local from locais where id = nas_t4_res) as nas_t4_res ,
          (select estado from estados where id=nas_t4_estado) as nas_t4_estado ,
          nas_t5,
          (select prof from profissoes where prof_id = nas_t5_prof) as nas_t5_prof ,
          (select local from locais where id = nas_t5_res) as nas_t5_res ,
          (select estado from estados where id=nas_t5_estado) as nas_t5_estado ,
          (select pa_nome from padres where pa_id = nas_padre) nas_padre ,
          (select local from locais where id = nas_padre_res) as nas_padre_res ,
          nas_selos,
          nas_obs,
          nas_mae_idade,
          (select estado from estados where id=nas_mae_estado) as nas_mae_estado
          from nascimentos
          where nas_id = %s'''

    rec = libpg.get_record_dic(sql,(index,))
    return rec
def get_casamento(index):
    sql = '''SELECT
          cas_id,
          cas_num,
          cas_ano,
          cas_registo,
          cas_folha,
          cas_data,
          cas_noivo,
          cas_noivo_idade,
          (select estado from estados where id=cas_noivo_estado) as cas_noivo_estado,
          (select prof from profissoes where prof_id=cas_noivo_profissao) as cas_noivo_profissao,
          (select local from locais where id = cas_noivo_residencia) as cas_noivo_residencia,
          (select local from locais where id = cas_noivo_naturalidade) as cas_noivo_naturalidade,
          cas_noivo_assinou,
          cas_noiva,
          cas_noiva_idade,
          (select estado from estados where id=cas_noiva_estado) as cas_noiva_estado,
          (select prof from profissoes where prof_id=cas_noiva_profissao) as cas_noiva_profissao,
          (select local from locais where id = cas_noiva_naturalidade) as cas_noiva_naturalidade,
          (select local from locais where id = cas_noiva_residencia) as cas_noiva_residencia,
          cas_noiva_assinou,
          cas_noivo_pai,
          (select prof from profissoes where prof_id=cas_noivo_pai_profissao) as cas_noivo_pai_profissao,
          (select local from locais where id = cas_noivo_pai_naturalidade) as cas_noivo_pai_naturalidade,
          (select local from locais where id = cas_noivo_pai_residencia) as cas_noivo_pai_residencia,
          cas_noivo_pai_falecido,
          cas_noivo_mae,
          (select prof from profissoes where prof_id=cas_noivo_mae_profissao) as cas_noivo_mae_profissao,
          (select local from locais where id = cas_noivo_mae_naturalidade) as cas_noivo_mae_naturalidade,
          (select local from locais where id = cas_noivo_mae_residencia) as cas_noivo_mae_residencia,
          cas_noivo_mae_falecido,
          cas_noiva_pai,
          (select prof from profissoes where prof_id=cas_noiva_pai_profissao) as cas_noiva_pai_profissao,
          (select local from locais where id = cas_noiva_pai_naturalidade) as cas_noiva_pai_naturalidade,
          (select local from locais where id = cas_noiva_pai_residencia) as cas_noiva_pai_residencia,
          cas_noiva_pai_falecido,
          cas_noiva_mae,
          (select prof from profissoes where prof_id=cas_noiva_mae_profissao) as cas_noiva_mae_profissao,
          (select local from locais where id = cas_noiva_mae_naturalidade) as cas_noiva_mae_naturalidade,
          (select local from locais where id = cas_noiva_mae_residencia) as cas_noiva_mae_residencia,
          cas_noiva_mae_falecido,
          cas_t1,
          (select estado from estados where id=cas_t1_estado) as cas_t1_estado,
          (select prof from profissoes where prof_id=cas_t1_profissao) as cas_t1_profissao,
          (select local from locais where id = cas_t1_naturalidade) as cas_t1_naturalidade,
          (select local from locais where id = cas_t1_residencia) as cas_t1_residencia,
          cas_t1_assinou,
          cas_t2,
          (select estado from estados where id=cas_t2_estado) as cas_t2_estado,
          (select prof from profissoes where prof_id=cas_t2_profissao) as cas_t2_profissao,
          (select local from locais where id = cas_t2_naturalidade) as cas_t2_naturalidade,
          (select local from locais where id = cas_t2_residencia) as cas_t2_residencia,
          cas_t2_assinou,
          cas_t3,
          (select estado from estados where id=cas_t3_estado) as cas_t3_estado,
          (select prof from profissoes where prof_id=cas_t3_profissao) as cas_t3_profissao,
          (select local from locais where id = cas_t3_naturalidade) as cas_t3_naturalidade,
          (select local from locais where id = cas_t3_residencia) as cas_t3_residencia,
          cas_t3_assinou,
          cas_t4,
          (select estado from estados where id=cas_t4_estado) as cas_t4_estado,
          (select prof from profissoes where prof_id=cas_t4_profissao) as cas_t4_profissao,
          (select local from locais where id = cas_t4_naturalidade) as cas_t4_naturalidade,
          (select local from locais where id = cas_t4_residencia) as cas_t4_residencia,
          cas_t4_assinou,
          cas_t5,
          (select estado from estados where id=cas_t5_estado) as cas_t5_estado,
          (select prof from profissoes where prof_id=cas_t5_profissao) as cas_t5_profissao,
          (select local from locais where id = cas_t5_naturalidade) as cas_t5_naturalidade,
          (select local from locais where id = cas_t5_residencia) as cas_t5_residencia,
          cas_t5_assinou,
          (select pa_nome from padres where pa_id = cas_padre ) as cas_padre,
          casamentos.cas_obs
        FROM
          casamentos
        WHERE
          cas_id = %s'''
    rec = libpg.get_record_dic(sql,(index,))
    return rec
def get_obito(index):
    sql = '''SELECT
         obi_id,
         obi_num,
         obi_ano,
         obi_registo,
         obi_folha,
         obi_data,
         obi_hora,
         obi_data_part,
         obi_local,
         obi_nome,
         obi_idade,
         (select local from locais where id = obi_naturalidade) as obi_naturalidade,
         (select local from locais where id = obi_residencia) as obi_residencia,
         (select prof from profissoes where prof_id=obi_profissao) as obi_profissao,
         obi_ilegitimo,
         obi_exposto,
         (select sexo from sexo where id=obi_sexo) as obi_sexo,
         (select estado from estados where id=obi_estado) as obi_estado,
         obi_conj,
         obi_conj_idade,
         (select local from locais where id = obi_conj_naturalidade) as obi_conj_naturalidade,
         obi_conj_data_falecimento,
         (select prof from profissoes where prof_id=obi_conj_profissao) as obi_conj_profissao,
         (select local from locais where id = obi_conj_residencia) as obi_conj_residencia,
         obi_num_filhos,
         obi_pai,
         (select prof from profissoes where prof_id=obi_pai_profissao) as obi_pai_profissao,
         (select local from locais where id = obi_pai_naturalidade) as obi_pai_naturalidade,
         (select local from locais where id = obi_pai_residencia) as obi_pai_residencia,
         (select estado from estados where id=obi_pai_estado) as obi_pai_estado,
         obi_pai_falecido,
         obi_mae,
         (select prof from profissoes where prof_id=obi_mae_profissao) as obi_mae_profissao,
         (select local from locais where id = obi_mae_naturalidade) as obi_mae_naturalidade,
         (select local from locais where id = obi_mae_residencia) as obi_mae_residencia,
         (select estado from estados where id=obi_mae_estado) as obi_mae_estado,
         obi_mae_falecida,
         (select causa from causasmorte  where cm_id=obi_sexo) as obi_causa,
         obi_emu,
         obi_declarante,
         (select local from locais where id = obi_dec_naturalidade) as obi_dec_naturalidade,
         (select local from locais where id = obi_dec_residencia) as obi_dec_residencia,
         (select prof from profissoes where prof_id=obi_dec_profissao) as obi_dec_profissao,
         (select estado from estados where id=obi_dec_estado) as obi_dec_estado,
         obi_t1,
         (select local from locais where id = obi_t1_naturalidade) as obi_t1_naturalidade,
         (select local from locais where id = obi_t1_residencia) as obi_t1_residencia,
         (select prof from profissoes where prof_id=obi_t1_profissao) as obi_t1_profissao,
         (select estado from estados where id=obi_t1_estado) as obi_t1_estado,
         obi_t2,
         (select local from locais where id = obi_t2_naturalidade) as obi_t2_naturalidade,
         (select local from locais where id = obi_t2_residencia) as obi_t2_residencia,
         (select prof from profissoes where prof_id = obi_t2_profissao) as obi_t2_profissao,
         (select estado from estados where id = obi_t2_estado) as obi_t2_estado,
         obi_paroco,
         obi_sacramentos,
         obi_testamento,
        obi_obs
        FROM
          obitos
          where obi_id = 45'''
    rec = libpg.get_record_dic(sql,(index,))
    return rec

if __name__ == '__main__':
  pa.conn_string = "host=192.168.0.98 dbname=registos_paroquiais user=root password=masterkey"
  print(get_max_record('nascimentos','nas_id'))
  print(get_max_record('casamentos','cas_id'))
  print(get_max_record('obitos','obi_id'))