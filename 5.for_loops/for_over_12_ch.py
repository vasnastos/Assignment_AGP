import sys
sys.path.append('..')
import file_walk as fw 
import re
import os

files=fw.file_parser()

def over_12_characters():
    found=0
    print(len(files))
    #for regex
    pattern=re.compile('for\(.*;.*;.*\)$|for\(.+:.+\)$')
    for x in files:
        with open(x,'r',encoding='ISO-8859-1') as f:
           for k in f:
               for l in pattern.findall(k):
                   current=l[int(l.find('('))+1:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         found+=1
    print(f'for loops with over 12 characters:{found}')
   
over_12_characters()