import re
import sys 
from time import time
import termcolor as tm
import file_walk as fw
from functools import reduce

files=fw.file_parser()

#Εύρεση όλων των ακέραιων μεταβλητών
def commonvars():
    vars={}
    start_time=time()

    #Τρια Μοτίβα μεταβλητών
    #int a;-->int\s+\w+;
    #int a=10;-->int\s+\w+\s*([=]\s*\w+\s*)+;
    #int a,b,c;-->int\s+\w+\s*([,]\s*\w+\s*)*;
    #Μη αποδεκτό-->const int a=10;
   
   #(int\s+\w+\s*([,]\s*\w+\s*)*[;]|\s*int\s+\w+\s*([=]\s*\w+\s*)+[;])
    patternf=re.compile('(int\s+\w+\s*([,]\s*\w+\s*)*[;]|(int\s+\w+\s*([=]\s*\w+\s*)[;])|\s*int\s+\w+\s*([=]\s*\w+\s*)+[;])')
    constpattern=re.compile('(const\s+int\s*\w+\s*([=]\s*\w+\s*)+[;])')
    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as L:
            for k in L:
                cleanconst=k
                for l in constpattern.findall(k):
                    cleanconst=k.replace(l[0],'')
                for t in patternf.findall(cleanconst):
                    ln=t[0].strip().replace(';','').replace('int','')
                    if '=' in ln and ',' not in ln:
                        data=ln.split('=')
                        j=data[0].strip()
                        if j.isdigit():
                            continue
                        else:
                            if j in vars:
                                vars[j]+=1
                            else:
                                vars.update({j:1})
                    elif ',' in ln:
                        data=ln.split(',')
                        for m in data:
                            if '=' in m:
                                data1=m.split('=')
                                checkstr=data1[0].strip()
                                if checkstr in vars:
                                    vars[checkstr]+=1
                                else:
                                    vars.update({checkstr:1})
                            else:
                                if m.strip() in vars:
                                    vars[m.strip()]+=1
                                else:
                                    vars.update({m.strip():1})
                    else:
                        if j.strip() in vars:
                            vars[j.strip()]+=1
                        else:
                            vars.update({j.strip():1})
    sortedmap=sorted(vars.items(),key=lambda item:item[1])
    end_time=time()
    tm.cprint('=='*30,'red')
    tm.cprint('\tMost Common Integer Vars','red')
    for i in range(len(sortedmap)-1,len(sortedmap)-4,-1):
        tm.cprint(f'\t{sortedmap[i][0]}-->{sortedmap[i][1]}','green')
    tm.cprint('=='*30,'red') 
    tm.cprint('\tRuntime total chrono','blue')   
    tm.cprint(f'Lapsed Time:{end_time-start_time} \'s','blue')
    print('\n\n')
       
commonvars()