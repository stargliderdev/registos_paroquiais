#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import psycopg2
import psycopg2.extras

import json
import collections
import pickle

import parameters as pa
import libpg

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

def read(index):
    a = libpg.output_query_one('select pa_description,pa_dict_values from param where id=%s',(index,))
    return a
def params_get():
    a = libpg.output_query_many('select pa_desciption, pa_dict_values from param ')
    toto = {}
    for n in a:
        toto[n[0]] = n[1]
    return toto

def write(index,value):
    sql = 'UPDATE param set pa_dict_values = %s where id = %s'
    libpg.execute_query(sql,(value,index))

if __name__ == '__main__':
    pa.conn_string = "host=192.168.0.98 dbname=registos_paroquiais_sandbox user=root password=masterkey"
    write(1,1900)
    print(read(0))
    pa.last_year = read(0)[1]
    pa.pg_dump = read(2)[1]
    print(pa.last_year)
    print('S.O.')

