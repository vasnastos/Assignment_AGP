# 2η Εργαστηριακή Άσκηση Αρχές Γλωσσών Προγραμματισμού<a href="https://github.com/chgogos/dituoi_agp/blob/main/resources/agp_assignment20210329.pdf"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Red_information_icon_with_gradient_background.svg/768px-Red_information_icon_with_gradient_background.svg.png" width="20px" height="20px"></a>
<br><br>
## ΖΗΤΟΥΜΕΝΑ ΕΡΓΑΣΙΑΣ
1. Άνοιγμα και περιήγηση στον φάκελο oop-master 
    * Φάκελος oop-master:[oop-master](https://github.com/chgogos/oop/archive/refs/heads/master.zip)
    * Εύρεση αρχείων από φάκελο και υποφακέλους με χρήση os.walk:[code](https://github.com/vasnastos/Assignment_AGP/blob/master/file_walk.py)
       ```
         def file_parser():
             print(os.getcwd())
             allfiles=[]
            try:
                for path,_,file in os.walk(top=parentroot,topdown=True):
                      allfiles+=[path+'/'+l for l in file if l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
            except:
                  print('Can not open folder oop-master')
                  return list([])
             return allfiles
        
       ```
    * Κώδικας με χρήση αναδρομικής συνάρτησης για εύρεση όλων των αρχείων από τον φάκελο oop-master:[code](https://github.com/vasnastos/Assignment_AGP/tree/master/File_Detector)
        ```
        
         def print_Dirs(masterpath):
            global pathfiles
            files=os.listdir(masterpath)
            for x in files:
                if os.path.isdir(masterpath+'/'+x):
                    print_Dirs(masterpath+'/'+x)
                else:
                    pathfiles.append(masterpath+'//'+x)
        
        ```
        <br>
2. Εύρεση αρχείων .c,.cpp,.h,.hpp<br>
3. Εύρεση Συμβόλων,Χαρακτήρων,Ψηφίων<br>
4. Εύρεση όλων των γραμμών κώδικα(εκτός κενών γραμμών)<br>
5. Πλήθος Εντολών if με συνθήκη ισότητας
      * Source Code:[code](https://github.com/vasnastos/Assignment_AGP/tree/master/4.Calculate_If_Statement)
      ```
         def equality_statements():
             counter=0
             fls=[]
             pattern=re.compile('if\s*\(.+==.+\)$')
             for x in files:
                 with open(x,'r',encoding='utf-8',errors='ignore') as f:
                     #counter+=len([m for m in f if(r.match('.*if(.+==.+).*',m))])
                     for k in f:
                         fls+=pattern.findall(k)
             tm.cprint('\t If equality Statements found','blue')
             tm.cprint('==='*30,'red')
             id=1
             for k in fls:
                 k=k.replace(' ','').replace('\t','')
                 tm.cprint(str(id)+'.'+str(k),'green')
                 id+=1
             print('\n\n')
             return len(fls)
      ```
6. For Loops με μέγεθος 12 χαρακτήρες<br>
7. Εύρεση 3 κοινών ονομάτων μεταβλητών


## GIT VERSION CONTROL
<iframe width="100%" height="615" src="https://www.youtube.com/embed/RGOj5yH7evk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
