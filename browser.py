# -*- coding: utf-8 -*-
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

# import lib.parameters as pa

__version__ = '0.0.1'

class Browser(QDialog):
    def __init__(self, html_data, title, size = 1, parent = None):
        super(Browser,  self).__init__(parent)
        if size == 1:
            self.resize(1024, 800)
        elif size == 2:
            self.resize(800,600)
        elif size == 3:
            self.resize(600,400)


        self.setWindowTitle(title) 
        #siteUrl = QUrl(website)

        self.browserWebView = QWebView(self)  
       
        layout = QVBoxLayout()
        layout.addWidget(self.browserWebView)
        
        self.printBtn = QPushButton('Print') 

        self.connect(self.printBtn, SIGNAL("clicked()"), self.print_preview_click)

        layout.addWidget(self.printBtn)
        self.setLayout(layout)

        self.impressor=QPrinter()
        self.dialogo=QPrintPreviewDialog()

        self.browserWebView.setHtml(html_data)
    
    def print_preview_click(self):
        print('pass')
        self.connect(self.dialogo, SIGNAL("paintRequested (QPrinter *)"),self.browserWebView.print_)
        self.connect(self.browserWebView,SIGNAL("loadFinished (bool)"),self.previaImpressao)
        self.previaImpressao(True)
    def previaImpressao(self,arg):
        self.dialogo.exec_() 


def main():
    app = QApplication(sys.argv)
    form = Browser('/home/zorze/python/mercados/output.html')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
