from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from cgi import test
import sqlite3
from unittest import result
import mysql.connector 
from mysql.connector import errorcode
from pydoc import render_doc
import PyPDF2
import re
from pathlib import Path 
import json 
import os



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
            



#arq = "00254652"
#arq = int(arq)
#arq = str(arq)
arrayfile = []
arraycdfile = []
cdcategoria = 26
#print(arq)
#print(type(arq))


def lerCategory():
    
    arrayfile = []
    cursor.execute("SELECT idcategory, cdcategory FROM `pan_categoria` ")
    result = cursor.fetchall()
    arquivo = open("./arqtxt/categoria.txt", "a")
    for x in result:
        print(x, "\n")
        arrayfile.append( ' {}, \n'.format(x))
        arquivo.writelines(arrayfile)
    print("resultados:",cursor.rowcount)
                
def lerfilepagevazio():
    # cursor.execute("SELECT id, cdfile FROM `pan_documentos` WHERE categoria_cdcategory = {} AND filenumeropaginas is NULL".format(cdcategoria))
    cursor.execute("SELECT cdfile FROM `pan_documentos` WHERE categoria_cdcategory = {} AND filenumeropaginas = 0".format(cdcategoria))
    result = cursor.fetchall()
    for x in result:
        arrayfile.append(x[0])
        #print(x)
    print("pagina vazias:",len(result))
    #print(type(arrayfile[2]))
    #print(arrayfile)
    insereZeroNoFile() #chamada da função para inerir os arquivos cdfile tratados no array "arraycdfile"
    testLerpagInserpage()
    #print(arrayfile)

def insereZeroNoFile():
    for file in arrayfile:
        file = "00" + file 
        arraycdfile.append(file)
    #print(arrayfile)
    #print(arraycdfile) saida do tipo 00+arrayfile

def testLerpagInserpage():
    cd_category = 72
    #arq = r"344870"
    #file = r"\00344870.pdf"
    
    #print(pdf_file)

    for arq in arrayfile:
        
        cdfile = arq
        print(cdfile)
        # arq = "0000" + arq + ".pdf" #para dados trazidos direto da base 
        # arq =  arq + ".pdf" #para dados trazidos direto da base 
        #arq = "00" + arq + ".pdf"  #as vezes são três zeros (tifconvertido, por exemplo)
        #arq = "000" + arq + ".pdf"  #as vezes são três zeros (tifconvertido, por exemplo)

        p = r"D:\var\www\html\paneiro\diretoriocontrolado\dadostratados\pagamentosmensais" #diretorio onde serão lidos os pdf

        print("{}\{}".format(p,arq)) 

        try:
            pdf_file = open(os.path.join(p, arq) , 'rb')#bre o arquivo
            read_pdf = PyPDF2.PdfFileReader(pdf_file) # lÊ o arquivo
            number_of_pages = read_pdf.getNumPages() #nmero de págin
            print("numpage = ", number_of_pages) #printa o númro de páginas

            cursor.execute("SELECT *  FROM `pan_documentos` WHERE `categoria_cdcategory` = {} AND `cdfile` LIKE '{}'".format(cdcategoria, cdfile)  )
            result = cursor.fetchall()
            num_page_query = result[0][14]
            file_descompactado = result[0][15]

            if(num_page_query == 0 and file_descompactado == 1): # se o numero de páginas for zero será feito o update
                sql = "UPDATE `pan_documentos` SET filenumeropaginas = {} , filedescompactado = 1 WHERE `categoria_cdcategory` = {} AND `cdfile` LIKE '{}'".format(number_of_pages, cdcategoria , cdfile)
                print(sql)    
                cursor.execute(sql)
                db_connection.commit()
                print(cursor.rowcount, "record inserted.")
                print("\n----------------------------------------\n")
        except:
            print("houve erro")
        

        #print(result[0][14])
        #for x in result:
            # print("numPagBusca:",x[14])

    '''
   
    cursor.execute("SELECT *  FROM `pan_documentos` WHERE `categoria_cdcategory` = {} AND `cdfile` LIKE '{}'".format(cd_category, arq)  )
 #  cursor.execute("SELECT *  FROM `pan_documentos` WHERE `categoria_cdcategory` = {} AND `documentoid` LIKE '{}'".format(cd_category, arq)  )
 #print("resultados:", cursor.rowcount)
    result = cursor.fetchall()
    for x in result:
        print("numPagBusca:",x[14])
    
    #print("resultados:",cursor.rowcount)
    if result[14] == 0:
        sql = "UPDATE `pan_documentos` SET filenumeropaginas = {} WHERE `categoria_cdcategory` = {} AND `cdfile` LIKE '{}'".format(number_of_pages, cd_category , arq)
        print(sql)    
    '''
#lerCategory()
lerfilepagevazio()
#testLerpagInserpage()

