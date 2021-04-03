import file_walk as fw
import re as r
import termcolor as tm


files=fw.file_parser()
tm.cprint('\t\tFiles found:'+str(len(files)),'green')

def equality_statements():
    counter=0
    fls=[]
    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as f:
            #counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
            fls+=[m for m in f if r.match('.*\s*if\s*\(.+==.+\).*',m)]
    tm.cprint('\t If equality Statements found','blue')
    tm.cprint('==='*30,'red')
    id=1
    for k in fls:
        k=k.replace(' ','').replace('\t','')
        tm.cprint(str(id)+'.'+str(k),'green')
        id+=1
    print('\n\n')
    return len(fls)       


equals=equality_statements()
tm.cprint('\t  If Statements containing equality','red')
tm.cprint('==='*20,'blue')
tm.cprint('\tNumber of statements:'+str(equals),'green')