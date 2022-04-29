from ctypes.wintypes import PINT
from multiprocessing.reduction import duplicate
import os
from pydoc import render_doc
import PyPDF2
import re
from pathlib import Path 
import json 

i = 0
dictfile = []
arrayfile = []

def files_path05(*args): #funçãoprincipal
    for item in args: # for das pastas 
        for p, _, files in os.walk(os.path.abspath(item)): #laço para verificar os arquvos no array (files)
            global i, arrayfile
            
            arquivo = open("contratos.txt", "a")           
            for file in files: # laço no array de arquivos
                
                i = i + 1
                print("Item " + str(i) )
                print( "Diretório: " + os.path.join(p, file)) #imprin
                print(" Arquivo: " + file) #imprime o nome do arquivo
                pdf_file = open(os.path.join(p, file) , 'rb')#bre o arquivo
                #print(pdf_file) #imprime o nome do arquivo
                read_pdf = PyPDF2.PdfFileReader(pdf_file) # lÊ o arquivo
                number_of_pages = read_pdf.getNumPages() #nmero de páginas
                print("Número de Páginas: " + str(number_of_pages))
                byte = float((Path(os.path.join(p, file)).stat().st_size))/1048576
                print( "Tamanho: " +   str(byte) + "MB")
                arrayfile.append( 'arquivo: {} Numpage: {} Tamanho: {} \n'.format(file, number_of_pages, byte))
                arquivo.writelines(arrayfile)
                
                #dictfile[i]   = json.dumps('"arquivo": {}, "Numpage:" {}, "Tamanho:" {}'.format(file, number_of_pages, byte), indent = 3 )
            arquivo.close()    
    return arrayfile
                

lista = files_path05('C:/Users/aa/Desktop/controleadmuea')










# for i in lista:
#     print(i + "\n")


