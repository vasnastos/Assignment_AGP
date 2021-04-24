import sys
sys.path.append('..')
import file_walk as fw
import re 
import termcolor as tm

files=fw.file_parser()
#files=['sample.cpp'];
tm.cprint('\t\tFiles found:'+str(len(files)),'green')

def equality_statements():
    counter=0
    fls=[]
    pattern=re.compile('\s+if\s*\(\s*.+\s*==\s*.+\)|^if\s*\(.+==.+\)|.*if\s*\(\s*\w+\s*\)')
    #if(x==5)-->NAI
    #std::count_if(v.begin(),v.end(),[](int &l) {return l==5})
    #patternB=re.compile("\s*if\s*\(\s*\w+\s*\)")
    #|if\s*\(\s*(\w|\d)+\s*\)
    #if\s*\(\s*(\w|\d)+\s*\)-->if(k) αν k είναι boolean μεταβλητή η ένας αριθμός
    for x in files:
        with open(x,'r',encoding='utf-8',errors='ignore') as f:
            #counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
            for k in f:
                #print(patternB.findall(k))
                fls+=pattern.findall(k)
                #fls+=patternB.findall(k)
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