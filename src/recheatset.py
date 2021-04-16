import re

#Exercises Retrieve from:https://www.w3resource.com/python-exercises/re/
#Maitence By:Nastos Vasileios
#Department of informatics and Telecommunications


def one():
    #Write a Python program to search a literals 
    #string in a string and also find the location within the original string where the pattern occurs.
    inp='The quick brown fox jumps over the lazy dog.'
    searchtext='fox'
    pattern=re.compile('fox')
    data=pattern.findall(inp)
    print('fox occurences:'+str(len(data)))
    index=inp.find('fox')

def two():
    import requests as r
    import termcolor as tm
    text='ing'
    data=[x for y in r.get('https://www.gutenberg.org/cache/epub/61213/pg61213.txt').text.split('\n') for x in y.splt()]
    for k in data:
        if re.match(f'.*{text}$',k):
            tm.cprint(f'Matched found:{k}','green')
        else:
            tm.cprint(f'Word:{k}','red')

def three():
    inputtable=['apo','abbbb','a','m','ab','b','abn']
    import termcolor as tm
    for x in inputtable:
        if re.match('ab?$',x):
            tm.cprint('Match Found:'+str(x),'green')
        else:
            tm.cprint('Word:'+str(x),'red')

def four():
    import termcolor as tm
    with open('ips.data','r') as f:
        pattern='[1][9][2-9]|[2]([01][0-9]|[2][0-2])\.([1-9][0-9]?|[1][0-9][0-9]|2([0-4][0-9]|5[0-5])\.([1-9][0-9]?|[1][0-9][0-9]|2([0-4][0-9]|5[0-5])\.([1-9][0-9]?|[1][0-9][0-9]|2([0-4][0-9]|5[0-5])'
        data=[x.strip() for x in f.readlines()]
        for x in data:
            if re.match(pattern,x):
                tm.cprint(f'Class c:{x}','green')
    
def five():
    pattern='([0-9][a-zA-Z]){5}'
    for x in ['1y6r7t8U9P','a^78IOPl','8t9i7l5r4t','2b9n0m8v7b','asdfg7jk9','as567w2rt4','alkso0981','aw3456yuiq','1a2b3c4d5E','sgkdghasfdasd']:
        if re.match(pattern,x):
            print(x)

def six()


