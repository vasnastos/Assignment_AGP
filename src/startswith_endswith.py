import requests
import bs4
from time import time

#use link-->https://www.gutenberg.org/cache/epub/20727/pg20727.txt


def source():
    inp=input('Give url:')
    startingtime=time()
    arequest=requests.get(inp)
    data=arequest.text
    tempdata=data.split('\n')
    return (startingtime,[x for y in tempdata for x in y.split()])


tup=source()
starttime=tup[0]
data=tup[1]
#Χρονομέτρηση κώδικα
opstart=0
ingend=0
for x in data:
    if x.startswith('op'):
        opstart+=1
    if x.endswith('ing'):
        ingend+=1
endtime=time()
k=input('Give filename you want to save the results:')
y=open(k,'w')
frmt='+--------------------------------------------+'
out1='| Words start with op:'
out2='| Words end with ing:'
y.write(frmt+'\n')
y.write(out1+str(opstart)+' '*(len(frmt)-(len(out1)+len(str(opstart))+1))+'|\n')
y.write(out2+str(ingend)+' '*(len(frmt)-(len(out2)+len(str(ingend))+1))+'|\n')
y.write('|'+'='*(len(frmt)-2)+'|\n')
y.write('| Lapsed Time:'+str(endtime-starttime)+' s'+' '*(len(frmt)-(len('| Lapsed Time:')+len(str(endtime-starttime))+len(' s')+1))+'|\n')
y.write(frmt)
y.close()

print('\t\tRESULTS')
print('=='*28)
with open(k,'r') as f:
    for l in f:
        print(l.replace('\n',''))
