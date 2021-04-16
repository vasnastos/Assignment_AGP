import re
import os
import sys 
#pip install termcolor
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
    #\w
    patternD=re.compile('\d')
    if len(files)==0:
        print('No input Data!!!Please Check you file Data')
        return

    start_time=time()

    for x in files:
      with open(x,'r',encoding="utf-8",errors='ignore') as f: 
        for k in f:
            """
            f.readline()
            while f.readline()!=None:
            """
            #actualsd=k.replace(' ','').replace('\n','')
            #actualsd=actualsd.strip()
            chars=len(patternC.findall(k))
            digits=len(patternD.findall(k))
            """
               for ch in k:#Προσπέλαση χαρακτήρων αλφαριθμητικού
                   if ch.isalpha():
                       parser['characters']+=1
                   elif ch.isdigit():
                       parser[digits']+=1
                   else:
                       parser['symbols']+=1
                       #parser.update('characters',parser['characters']+1)
                print(parser)
            """ 



            parser['characters']+=chars
            parser['digits']+=digits
            parser['symbols']+=len(k)-(chars+digits)
    end_time=time()
    for x in parser:
        tm.cprint(f'{x}-->{parser[x]}','green')
    tm.cprint('=='*30,'red')
    tm.cprint(f'Lapsed Time:{end_time-start_time} \'s','red')
    """
        for x in lines:
        actualsd=x.replace(' ','').replace('\n','')
        #actualid=x.strip()
        chars=len(patternC.findall(actualsd))
        digits=len(patternD.findall(actualsd))
        parser['characters']+=chars
        parser['digits']+=digits
        parser['symbols']+=len(actualsd)-(chars+digits)
    """
Symbols_letters_Digits()
