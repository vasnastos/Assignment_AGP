import re
import os

def fileContent():
    files=[]
    #Try Sample Data hello_world.cpp
    #y=open("hello_world.cpp",'r',encoding="utf8",errors='ignore')
    y=open("sample_data.cpp",'r',encoding="utf8",errors='ignore')
    files=y.readlines()
    y.close()
    return files

def Symbols_letters_Digits():
    lines=fileContent()
    parser={'characters':0,'digits':0,'symbols':0}
    patternC=re.compile('[A-Za-z]')
    patternD=re.compile('\d')
    if len(lines)==0:
        print('No input Data!!!Please Check you file Data')
        return
    
    for x in lines:
       actualsd=x.replace(' ','').replace('\n','')
       #actualid=x.strip()
       chars=len(patternC.findall(actualsd))
       digits=len(patternD.findall(actualsd))
       parser['characters']+=chars
       parser['digits']+=digits
       parser['symbols']+=len(actualsd)-(chars+digits)
    
    print(parser)

Symbols_letters_Digits()
