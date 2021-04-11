import os
import re

parentroot='../oop-master'

def file_parser():
    print(os.getcwd())
    allfiles=[]
    try:
        for path,_,file in os.walk(top=parentroot,topdown=True):
            allfiles+=[path+'/'+l for l in file if l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
    except Exception:
        print('Can not open folder oop-master')
        return list([])
    return allfiles

files=file_parser()


def filesbycategory():
    counter={'cpp':0,'hpp':0,'h':0,'c':0}
    for x in files:
        if re.match('.+\.cpp$',x): 
            #if x.endswith('.cpp'):
            counter['cpp']+=1
        elif x.endswith('.hpp'):
            counter['hpp']+=1
        elif x.endswith('.h'):
            counter['h']+=1
        else:
            counter['c']+=1
    
    for key in counter:
        print(str(key)+'-->'+str(counter[key]))


def codelines():
    linecounter=0
    for i in files:
        with open(i,'r') as f:
            for j in f:
                if len(j.strip())!=0:
                    linecounter+=1
    print('Lines of code:'+str(linecounter))



  
filesbycategory()
codelines()
print('=='*30)

