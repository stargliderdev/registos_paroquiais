#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

import parameters as pa
import stdio

def main():
	nascimentos = stdio.read_file('nascimentos.csv',1)
	linhas =  len(nascimentos)
	registos = linhas-2
	print('   linhas', "{0:10d}".format(linhas))
	print(' registos', "{0:10d}".format(registos))

	for n in range(0,len(nascimentos)):
		if n == 0:
			toto = nascimentos[0].split(';')
			fields_list = toto
		elif n == 1:
			pass
		else:
			print(' linha:',"{0:10d}".format(n))
			toto = nascimentos[n].split(';')
			for campo in range(0,len(toto)-1):
				try:
					#print fields_list[campo],toto[campo]
					if fields_list[campo].find('.'):
						print('campo realcionado',fields_list[campo])
					else:
						print('texto')
				except Exception as err:
					print(err)
					print('------------- dump')
					print(' linha:',"{0:10d}".format(n)) 
					print('len toto',len(toto))
					print('campo',campo)
					sys.exit(1)
			#print nascimentos[n]

if __name__ == '__main__':
    main()