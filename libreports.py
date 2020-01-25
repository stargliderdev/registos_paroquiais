#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

class buildReport:
    def __init__(self,):
        self.output = '''<!DOCTYPE html><html lang="pt_pt"><head><meta charset="utf-8">'''

    def set_css(self):
        css = '''<style>
            .std{ border-bottom: solid #000 2.0pt; font-family: Arial;
            font-size: 15px; color: #333333; height: 18px; }</style> '''
        self.output += css
        self.output += '<html><body>'

    def table(self, dataset, header='' ):
        css_table_header = 'std'
        self.output += '<table class="' + css_table_header + '"> '
        self.create_header('std', header)
        self.create_lines(dataset,True)
        self.output += '</table> '

    def create_header(self, css_style, header):
        # toto = '<table "' + css_style + '"> <tr>'
        toto = ''
        for n in header: #['<th>id</th>', '<th>Nome da Feira ^</th>','<th>Freguesia</th>','<th>Concelho</th>','<th>Distrito</th>']:
            toto +=  '<th>' +  n  +'</th>' #pply_style('#customers th', n)
        toto += '</tr>'
        self.output +=toto


    def create_lines(self, dataset, stripes = True):
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
              dum =  '<tr>' + NEWLINE
            else:
                dum =  '<tr>' + NEWLINE
            for tr in n: # dados
                if type(tr) == int:
                    foo = '<td align="right">' + str(tr) + '</td>' + NEWLINE
                elif type(tr) == float:
                    foo = '<td align="right">' + "{0:.2f}".format(tr) + '</td>' + NEWLINE
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
        self.output +=toto


    def vertical_grid(self, dataset):
        # input 2 dimension tuple: [0]: label, [1]:data
        div_end = '''</h3></div>\n'''
        td_caixa= '<tr><td id="label">'
        td_data = '<td style="color: #000080 ; font-family:Verdana; font-size:14px">'
        td_end = '</td></tr>\n'
        self.output += ''' <table>
                '''
        for n in dataset:
            self.output += td_caixa + n[0] + td_data + n[1] + td_end
        self.output += '</table>'

    def close(self):
        self.output += '</html></body></head>'




if __name__ == '__main__':
    print(vertical_grid([('db version', '1.9'),('psql version', '9.3')]))