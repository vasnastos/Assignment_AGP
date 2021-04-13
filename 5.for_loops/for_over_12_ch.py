import sys
sys.path.append('..')
import file_walk as fw 
import re
import os
import termcolor as tm

files=fw.file_parser()

def over_12_characters():
    found=0
    print(len(files))
    print(os.getcwd())
    #for regex
    pattern=re.compile('for\s*\(.*\s*;.*\s*;.*\s*\)|for\s*\(.+\s*:.+\s*\)')
    for x in files:
        with open(x,'r',encoding='ISO-8859-1') as f:
           for k in f:
               fnd=0
               for l in pattern.findall(k):
                   fnd=1
                   current=l[int(l.find('('))+1:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         found+=1
                        
               tm.cprint(k,'green') if fnd==1 and 'for' in k else tm.cprint(k,'red') if 'for' in k else print(end='')
    
    print(f'for loops with over 12 characters:{found}')
   
over_12_characters()