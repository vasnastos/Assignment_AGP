import re
import os
import sys 
import termcolor as tm
from time import time
sys.path.append('..')
import file_walk as fw

files=fw.file_parser()

#Testing files
def fileContent():
    files=[]
    #Try Sample Data hello_world.cpp
    #y=open("hello_world.cpp",'r',encoding="utf8",errors='ignore')
    y=open("sample_data.cpp",'r',encoding="utf8",errors='ignore')
    files=y.readlines()
    y.close()
    return files

def Symbols_letters_Digits():
    parser={'characters':0,'digits':0,'symbols':0}
    patternC=re.compile('[A-Za-z]')
    patternD=re.compile('\d')
    if len(files)==0:
        print('No input Data!!!Please Check you file Data')
        return
    
    start_time=time()

    for x in files:
      with open(x,'r',encoding="utf-8",errors='ignore') as f: 
        for k in f:
            actualsd=k.replace(' ','').replace('\n','')
            #actualsd=actualsd.strip()
            chars=len(patternC.findall(actualsd))
            digits=len(patternD.findall(actualsd))
            parser['characters']+=chars
            parser['digits']+=digits
            parser['symbols']+=len(actualsd)-(chars+digits)
    end_time=time()
    for x in parser:
        tm.cprint(f'{x}-->{parser[x]}','green')
    tm.cprint('=='*30,'red')
    tm.cprint(f'Lapsed Time:{end_time-start_time} \'s','red')
    

Symbols_letters_Digits()