#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import psycopg2
import psycopg2.extras

#note that we have to import the Psycopg2 extras library!


import parameters as pa

def output_query_one(sql, data):
        try:
            conn = psycopg2.connect(pa.conn_string)
            cur = conn.cursor()
            conn.set_client_encoding('UTF8')
            
            #print 'mogrify:', cur.mogrify(sql, data)
            cur.execute(sql, data)      
            return cur.fetchone()

            
        except Exception as e:
            print(str(e) ,  '\n -- SQL Error --\n')
            print(sql)
            exit(1)

def output_query_many(sql,data):
     
    try:
        conn = psycopg2.connect(pa.conn_string)
        cur = conn.cursor()
        conn.set_client_encoding('UTF8')
        
        #print 'mogrify:', cur.mogrify(sql, data)
        cur.execute(sql, data)      
        return cur.fetchall()
        
    except Exception as e:
        print(str(e) ,  '\n -- SQL Error --\n','\n' , sql)
        sys.exit(1)

def execute_query(sql, data):
    try:
        conn = psycopg2.connect(pa.conn_string)
        cur = conn.cursor()
        conn.set_client_encoding('UTF8')

        #print 'mogrify:', cur.mogrify(sql, data)
        cur.execute(sql, data)      
        conn.commit()
        cur.close()
        conn.close()
        
    except Exception as e: 
        print('-------------------------------------------------------')          
        print('ERROR:',str(e))
        print('  SQL:',sql)
        print(' DATA:',data)
        exit(1)

def add_record_to_table(table, field, value):
    value = str(value)
    execute_query('insert into ' + table + ' ( ' + field + ') values(%s); ', (value,))


def get_record_dic(sql, id):
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(pa.conn_string)
    dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    dict_cur.execute(sql, id)
    rec = dict_cur.fetchone()
    return rec
        
if __name__ == "__main__":
    pass
