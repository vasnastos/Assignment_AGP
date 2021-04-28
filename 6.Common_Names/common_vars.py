import sys
sys.path.append('..')
import file_walk as fw
import re

files=fw.file_parser()

def Strip_Semicolon(string):
    return string.replace(';','')

def CommonVars():
    commonvars=dict({})
    #commonvars={}
    #commonvars.add(strn)-->set
    #key:value

    #Pattern for variables 
    unacceptable=re.compile('((const|static|static\s+const)\s+int\s+\w+\s*[=]\s*\w+\s*[;])')
    pattern=re.compile('\s*int\s+\w+[;]')
    #int a;
    #int    b;
    patternA=re.compile('(\s*int\s+\w+([,]\w+)+[;])')
    patternB=re.compile('(\s*int\s+\w+([=]\w+)+[;])')
    #int a=2;
    patternC=re.compile('(\s*int\s+\w+\s*[=]\s*\w+\s*([,]\s*\w+\s*[=]\s*\w+\s*)+[;])')
    #int a=1,b=3;
    for x in files:
        with open(x,'r',encoding='utf8',errors='ignore') as f:
            lines=f.readlines()
            for k in lines:
                word=k
                if word.startswith('//') or word.startswith('#'):
                    continue
                #    -->k  const int b=0; int h;
                for l in unacceptable.finditer(k):
                    word=k[0:l.start()]+k[l.end():]


                for n1 in pattern.findall(word):
                   if len(n1)==0: continue
                   w=n1.replace(';','').strip()
                   spdat=re.split('\s+',w)
                   #0-->int 1-->a
                   if spdat[1] in commonvars:
                       commonvars[spdat[1]]+=1
                   else:
                       commonvars.update({spdat[1]:1})

                for n2 in [l[0] for l in patternA.findall(word)]:
                    word=n2.replace(';',' ').strip()
                    data2=re.split('[,\s]',word)
                    for j in data2:
                        if j.strip()=='int': 
                            continue
                        if j.strip() in commonvars:
                           commonvars[j.strip()]+=1
                        else:
                           commonvars.update({j.strip():1}) 
                for n3 in [l[0] for l in patternB.findall(word)]:
                    word=n3.strip().replace(';','')
                    data3=[x for x in re.split('[\s=]',word) if x.strip()!=';' and re.search('^\s+$',x)==None]
                    counter=0
                    for j in data3:
                       counter+=1
                       if len(data3)==int(counter):
                            continue
                       if j.strip()=='int':
                           continue
                       if j.strip() in commonvars:
                           commonvars[j.strip()]+=1
                       else:
                           commonvars.update({j.strip():1})

                for n4 in [l[0] for l in patternC.findall(k)]:
                    word=n4.strip().replace(';','')
                    #int a=2,b = 8,c =0
                    #inta=2|b=8|c=0
                    data4=[x.replace(' ','') for x in word.split(',')]
                    for j in data4:
                        checkstr=word.split('=')[0]
                        #checkstr=checkstr1.split(' ')[1]
                        if checkstr in commonvars:
                            commonvars[checkstr]+=1
                        else:
                            commonvars.update({checkstr:1})
                
    tops=sorted(commonvars.items(),key=lambda elem:elem[1])
    #print(commonvars['j'])
    for i in range(len(tops)-1,len(tops)-4,-1):
        print(f'{tops[i][0]}-->{tops[i][1]}')



CommonVars()
                

    