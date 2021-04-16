import sys
sys.path.append('..')
import file_walk as fw 
import re
import os
import termcolor as tm

#Χρήση custom module file_walk:[https://github.com/vasnastos/Assignment_AGP/blob/master/file_walk.py]
#Απαραίτητος ο φάκελος oop-master
files=fw.file_parser()

def over_12_characters():
    found=0
    print(len(files))
    print(os.getcwd())
    #for regex
<<<<<<< HEAD
    pattern=re.compile('\s*for\s*\(\s*.*\s*;\s*.*\s*;\s*.*\s*\)|\s*for\s*\(\s*.+[:]\s*.+\s*\)')
=======
    pattern=re.compile('for\s*\(.*\s*;.*\s*;.*\s*\)|for\s*\(.+\s*:.+\s*\)')
>>>>>>> 4dd18feebcf5048df33754c6584a54a17aa2c6fb
    for x in files:
        with open(x,'r',encoding='ISO-8859-1') as f:
           for k in f:
               fnd=0
               for l in pattern.findall(k):
<<<<<<< HEAD
                   tm.cprint(l,'red')
=======
                   fnd=1
>>>>>>> 4dd18feebcf5048df33754c6584a54a17aa2c6fb
                   current=l[int(l.find('('))+1:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         tm.cprint(current,'green')
                         found+=1
<<<<<<< HEAD
                   print('')
    print(f'for loops with over 12 characters:{found}')

#Test σε αρχείο sample.cpp
def tester():
    found=0
    pattern=re.compile('for\s*\(.+;.+;.+\)|for\s*\(.+[:].+\)')
    with open("sample.cpp",'r',encoding='utf-8') as L:
        for x in L:
            for l in pattern.findall(x):
                   tm.cprint(l,'red')
                   current=l[int(l.find('for('))+4:len(l)-1]
                   if len(current.replace(' ',''))>=12:
                         tm.cprint(current,'green')
                         found+=1
                   print('')
    print(f'for loops with over 12 characters:{found}')

#Περίπτωση με εύρεση kαι inline εντολών for
#split based for
def tester1():
    found=0
    pattern=re.compile('\(.+;.+;.+\)|\(.+[:].+\)')
    with open('sample.cpp','r') as f:
        for x in f:
            data=[]
            if 'for' in x:
                data=x.split('for')
            if len(data)==0:
                continue
            for k in data:
               if pattern.match(k):
                   tm.cprint(k,'red')
                   for m in pattern.findall(k):
                       fixed=m[m.find('(')+1:len(m)-1]
                       fixed=fixed.strip().replace(' ','')
                       if len(fixed)>=12:
                           tm.cprint(len(fixed),'yellow')
                           tm.cprint(fixed,'green')
                           found+=1
               tm.cprint('============================================================','white') 
        tm.cprint(f'Matches Found:{found}','blue')

over_12_characters()
#tester()
#tester1()
=======
                        
               tm.cprint(k,'green') if fnd==1 and 'for' in k else tm.cprint(k,'red') if 'for' in k else print(end='')
    
    print(f'for loops with over 12 characters:{found}')
   
over_12_characters()
>>>>>>> 4dd18feebcf5048df33754c6584a54a17aa2c6fb
