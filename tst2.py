from pathlib import Path
import os
import gzip
import shutil

path1 = r"D:\var\www\html\paneiro\diretoriocontrolado\dadosbrutos\pagamentosmensais" #dadbrutos
path2 = r"D:\var\www\html\paneiro\diretoriocontrolado\dadostratados\pagamentosmensais" #dadostrtados

list = []


def trataextencaobruto(array):
    arrayaux = []
    for iten in array:
        iten = str(iten)
        iten = Path(iten).stem
        #iten = Path(iten).stem
        arrayaux.append(iten)
    return arrayaux    

def trataextencaoratado(array):
    arrayaux = []
    for iten in array:
        iten = str(iten)
        iten = Path(iten).stem
        arrayaux.append(iten)
    return arrayaux 

filescompactado = os.listdir(path1)
filescompactado = trataextencaobruto(filescompactado)

filesdescompactados = os.listdir(path2)
#filesdescompactados = trataextencaoratado(filesdescompactados)

#print(filescompactado)
#print(filesdescompactados)


'''
print(Path(file_path)) #caminho completo 
file_name = Path(file_path).stem #nome do arquivo
print(file_name)
'''

for filecomp in filescompactado: 
     if filecomp in filesdescompactados:
         pass
     else:
         print(filecomp)
         
         with gzip.open(path1 + "\\" + filecomp.lower() + ".gz" , 'rb') as entrada:
            with open( path2 + "\\" + filecomp.lower() , 'wb') as saida:
                shutil.copyfileobj(entrada, saida)
            
            