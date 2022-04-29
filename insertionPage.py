import mysql.connector 
from mysql.connector import errorcode

from ctypes.wintypes import PINT
from multiprocessing.reduction import duplicate
import os
from pydoc import render_doc
import PyPDF2
import re
from pathlib import Path 
import json 



try:
    db_connection = mysql.connector.connect(host="127.0.0.1", user ="root",  password="admin", database = "paneiro")
   
    print(db_connection)
    print("Database Connect Made!")
    #db_connection.close()
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)
else:
    cursor = db_connection.cursor()
            

#--------------------------------------------------------------------#
cd_category = 72
i = 0
dictfile = []
arrayfile = []

def files_path05(*args): #funçãoprincipal
    for item in args: # for das pastas 
        for p, _, files in os.walk(os.path.abspath(item)): #laço para verificar os arquvos no array (files)
            global i, arrayfile
            
            arquivo = open("./arqtxt/frequencia.txt", "a")           
            for file in files: # laço no array de arquivos
                file_name = Path(file).stem
                #print(file_name)
                # print(type(file))
                
                arq = int(file_name)
                arq = str(arq)
                #arq = str(file_name)
                # arq = "FIC_FUN00"+arq
                print(arq)
                #print(arq)

                i = i + 1
                print("Item " + str(i) )
                print( "Diretório: " + os.path.join(p, file)) #imprin
                print(" Arquivo: " + file) #imprime o nome do arquivo
                pdf_file = open(os.path.join(p, file) , 'rb')#bre o arquivo
                print(pdf_file) #imprime o nome do arquivo
                read_pdf = PyPDF2.PdfFileReader(pdf_file) # lÊ o arquivo
                number_of_pages = read_pdf.getNumPages() #nmero de páginas
                print("Número de Páginas: " + str(number_of_pages))
                byte = float((Path(os.path.join(p, file)).stat().st_size))/1048576
                print( "Tamanho: " +   str(byte) + "MB")
                
                
                cursor.execute("SELECT *  FROM `pan_documentos` WHERE `categoria_cdcategory` = {} AND `cdfile` LIKE '{}'".format(cd_category, arq)  )
                # cursor.execute("SELECT *  FROM `pan_documentos` WHERE `categoria_cdcategory` = {} AND `documentoid` LIKE '{}'".format(cd_category, arq)  )
                #print("resultados:", cursor.rowcount)
                result = cursor.fetchall()
                for x in result:
                    print("numPagBusca:",x[14])
                    arrayfile.append( ' documentoref(base): {}  arquivo: {} Numpage: {} Tamanho: {} \n'.format(x[2], file, number_of_pages, byte))
                    arquivo.writelines(arrayfile)
                #print("resultados:",cursor.rowcount)
                #if result[14] === 0:
                sql = "UPDATE `pan_documentos` SET filenumeropaginas = {} WHERE `categoria_cdcategory` = {} AND `cdfile` LIKE '{}'".format(number_of_pages, cd_category , arq)
                print(sql)
                cursor.execute(sql)
                db_connection.commit()
                print(cursor.rowcount, "record inserted.")
                print("\n----------------------------------------\n")

                #dictfile[i]   = json.dumps('"arquivo": {}, "Numpage:" {}, "Tamanho:" {}'.format(file, number_of_pages, byte), indent = 3 )
            arquivo.close()    
    return arrayfile

#--------------------------------------------------------------------#

files_path05(r"D:\var\www\html\paneiro\diretoriocontrolado\dadostratados\gratificacaoprodutividade")
#--------------------------------------------------------------------#






#consulta
#cursor.execute("SELECT * FROM `pan_documentos` WHERE `categoria_cdcategory` = 42 AND `filedescompactado` = 1 AND `filenumeropaginas`=0")
#result = cursor.fetchall()
#for x in result:
#   print(x)
#print("resultados:",cursor.rowcount)
#print("usuarios",cursor.rowcount) mostra quantas linhas foram retornadas com exito


