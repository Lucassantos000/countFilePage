import re
from pathlib import Path 
import os

item = r"C:\Users\aa\Downloads"
file = r"Modelo - Fichamento de artigo científico (PucMinas).pdf"
p = r"C:\Users\aa\Downloads"
#pesquisar mais afundo o que faz a função walk da biblioteca OS

def listafile():
        for p, meio, files in os.walk(os.path.abspath(item)): #laço para verificar os arquvos no array (files)
            print("p= ", p) #diretório passado em item
            print("meio= ", meio) # meio é uma lista vazia (neste contexto)
            for file in files:
                print("file= ", file) #imprime todos os arquivos no diretório (item)

def abrirfile():
    #pdf_file = open(os.path.join(p, file) , 'rb')#bre o arquivo (rb -> para leitura em modo binário)
    #print(pdf_file)# io.BufferReader 
    #print(pdf_file.read()) #impressão em binário de todo documento

    pdf_file = open(os.path.join(p, file) , 'rt')#bre o arquivo (rb -> para leitura em modo binário)
    print(pdf_file)# io.BufferReader 
    print(pdf_file.read()) #impressão em binário de todo documento


'''
Método open(file, mode)
mode: {
    r -> Apenas Leitura
    w -> SobreEscrita em Arquivos, se não existir, é criado um novo
    a -> Escrita(adiciona abaixo do conteudo antigo) em Arquivos, se não existir, é criado um novo
    x -> Apenas criação, e acusa falha se o arquivo existir
    b -> Abre em modo Binário
    t -> abre em modo de texto
    + -> abre um arquivo no disco para autalização (leitura e escrita)
}
'''


#listafile()
abrirfile()