# -*- coding: utf-8 -*-
import sys
import stdio
import datetime

def make_table_html(dataset,header = '', css = '', stripes = True,close_html = False):
    print(dataset)
    html = '</head>'
    if css == '':
        css_table_header = ''
    else:
        print('load css')
        html += stdio.read_file(css + '.css',2)
        
        css_table_header = 'custom'
    if header == '':
        row_header = '<table id="' + css_table_header + '"> '
    else:
        row_header = create_header(css_table_header,header) 
        
    html_data = create_lines(dataset,stripes)
    
    #toto = html_header + css + '<body>' + row_header + listToHtml + '</table></body></html>'
    toto = '<body>' + html + row_header + html_data + '</table>'
    if close_html == True:
        '</body></html>'
    return toto

def make_table(css_name,title,dataset,header=''):   
    if css_name == 'green':
        css = '<style type="text/css">#customers\
            {font-family:"Tahoma", Arial, Helvetica, sans-serif;width:100%;border-collapse:collapse;}\
            #customers td, #customers th {font-size:1em;border:1px solid #98bf21;padding:3px 7px 2px 7px;}\
            #customers th {font-size:14px;font-weight:bold;text-align:center;padding-top:1px;padding-bottom:1px;background-color:#A7C942;color:#000000;}\
            #customers tr.alt td {color:#0000px00;background-color:#EAF2D3;}\
            #customers tr:hover { background: #FCF; }\
            #right-cell {text-align: right;}</style></head>'
    elif css_name == 'green_small':
        css = '<style type="text/css">#customers\
            {font-family:"Tahoma", Arial, Helvetica, sans-serif;width:100%;border-collapse:collapse;}\
            #customers td, #customers th {font-size:10px;border:1px solid #98bf21;padding:1px 1px 1px 1px;}\
            #customers th {font-size:8px;font-weight:bold;text-align:center;padding-top:1px;padding-bottom:1px;background-color:#A7C942;color:#000000;}\
            #customers tr.alt td {color:#0000px00;background-color:#EAF2D3;}\
            #right-cell {text-align: right;}</style></head>'
    css_table_header = 'customers'

    #html_header = '<!DOCTYPE html><html lang="pt_pt"><head><meta charset="utf-8"><title>' + title + '</title>'
    listToHtml = ''

    if header == '':
    	row_header = '<table id="' + css_table_header + '"> '
    else:
    	row_header = create_header(css_table_header,header) 
    	
    listToHtml = create_lines(dataset)
    
    #toto = html_header + css + '<body>' + row_header + listToHtml + '</table></body></html>'
    toto = css + '<body>' + row_header + listToHtml + '</table></body></html>'

    return toto
def create_header(css_style,header):
    toto = '<table id="' + css_style + '"> <tr>' 
    for n in header: #['<th>id</th>', '<th>Nome da Feira ^</th>','<th>Freguesia</th>','<th>Concelho</th>','<th>Distrito</th>']:
        toto +=  '<th>' +  n  +'</th>' #pply_style('#customers th', n)
    toto += '</tr>'
    return toto

def create_lines(dataset, stripes = True):
    toto = ''
    NEWLINE = '\n'
    odd = True
    col1 = True
    if len(dataset[0]) <3:
        autoclean = True
    else:
        autoclean = False

    for n in dataset:
        if odd:
          dum =  '<tr class="alt">' + NEWLINE
        else:
            dum =  '<tr>' + NEWLINE
        for tr in n: # dados
            if type(tr) == int:
                foo = '<td id="right-cell">' + str(tr) + '</td>' + NEWLINE
            elif type(tr) == float:
                foo = '<td id="right-cell">' + "{0:.2f}".format(tr) + '</td>' + NEWLINE
            elif type(tr) == datetime.datetime:
                foo = '<td>' + "%02d.%02d.%02d" % (tr.day,tr.month,tr.year) + '</td>' + NEWLINE
            elif tr == None :
                foo = '<td>- </td> \n' 
            else:
                foo = '<td>'+ tr + '</td>'  + NEWLINE
            if autoclean == True:
                foo = foo.replace('td><','')
            dum += foo
        if stripes : odd = not(odd)
        toto += dum + '</tr>' + NEWLINE
    return toto


def format_report(texto):
    toto = texto.replace('\n','<br>')
    return toto

if __name__ == '__main__':
    print('SO')