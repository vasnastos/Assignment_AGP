import re


def forloop():
    #[abdfg]?
    #for\s*\(.*[;].*[;].*\)
    #for\s*\(.+[:].+\)
    expr='for\s*\(.+[:].+\)'
    pattern=re.compile(expr)
    with open('sample.cpp','r',encoding='utf-8',errors='ignore') as f:
        for l in f:
            for k in pattern.findall(l):
                #for(int i=0;i<10;i++)
                #str(k).index('(')+1-->ΘΕΣΗ ΕΚΚΙΝΗΣΗΣ
                #str(k).index(')')-1-->ΘΕΣΗ ΤΕΡΜΑΤΙΣΜΟΥ
                checkstring=k[str(k).index('(')+1:str(k).index(')')-1].replace(' ','')
                if len(checkstring)>=12:
                    print(k)


forloop()