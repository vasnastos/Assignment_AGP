import file_walk as fw
import re

files=fw.file_parser()
print('total files')
re.compile('[A-Z][a-z][0-9].*')

def Strip_Semicolon(string):
    return string.replace(';','')

def CommonVars():
    commonvars=dict({})
    for x in files:
        with open(x,'r',encoding='utf8',errors='ignore') as f:
            lines=f.readlines()
            for k in lines:
                if re.search('.*\s*int[\t]\s*\w+(;$|=\.w\s*;.*)',k):
                    print(k)
                    if k.startswith('//'): 
                        continue
                    if k.startswith('\s'):
                        i=0
                        while True:
                            if k[i]=='\t' or k[i]==' ':
                                i+=1
                            else:
                                break
                        #Έλεγχος για μεταβλητές τύπου int j = 0;
                        k=k[i:]
                    data=[]
                    if k.startswith('for\s*('):
                            data=k.split('=')
                            re.sub('for\s*(','',data[0])
                            if len(data)==2:
                                name=data[0]
                                name=name.replace('int','').replace('\t','')
                                if name in commonvars:
                                    commonvars[name]+=1
                                else:
                                    commonvars.update({name,1})
                    else:
                            data=k.split(';')
                            if len(data)==1:
                                data[0]=data[0].replace('int','').replace('\t','')
                                data1=data[0].split('=')
                                for var in data1:
                                    if not re.search('^\d+.*',var):
                                        if var in commonvars:
                                            commonvars[var]+=1
                                        else:
                                            commonvars.update({var:1})
    print(commonvars)

CommonVars()
                

    