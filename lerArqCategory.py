import os
import pathlib 
import re

arq = open("./arqtxt/categoria.txt")
linhas = arq.readlines()
for linha in linhas:
    string = linha
    characters = "() '!?"
    string = ''.join( x for x in string if x not in characters)
    arr = string.split(",")
    print(string)
    print(arr)