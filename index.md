# 2η Εργαστηριακή Άσκηση Αρχές Γλωσσών Προγραμματισμού<a href="https://chgogos.github.io/dituoi_agp/resources/agp_assignment20210329.pdf"><img width="20px" height="20px" src="https://www.freeiconspng.com/thumbs/information-icon/information-icon-clip-art-at-clker-com-vector-clip-art-online--32.png"></a>
![Regex image](https://www.oreilly.com/content/wp-content/uploads/sites/2/2019/06/email-regex_crop-ae942dc427c8cebd3a83c52d17389123.jpg)
<hr>

## GIT VERSION CONTROL
<iframe width="100%" height="512px" src="https://www.youtube.com/embed/RGOj5yH7evk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## ΖΗΤΟΥΜΕΝΑ ΕΡΓΑΣΙΑΣ
<hr>
1. Άνοιγμα και περιήγηση στον φάκελο oop-master 
    *  Φάκελος oop-master:[oop-master](https://github.com/chgogos/oop/archive/refs/heads/master.zip)
    * Εύρεση αρχείων από φάκελο και υποφακέλους με χρήση os.walk
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
       
     <br>  
     * Κώδικας με χρήση αναδρομικής συνάρτησης για εύρεση όλων των αρχείων από τον φάκελο oop-master
     ```
     
        pathfiles=[]
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
2. Εύρεση αρχείων .c,.cpp,.h,.hpp
3. Εύρεση Συμβόλων,Χαρακτήρων,Ψηφίων
4. Εύρεση όλων των γραμμών κώδικα(εκτός κενών γραμμών)
5. Πλήθος Εντολών if με συνθήκη ισότητας
6. For Loops με μέγεθος 12 χαρακτήρες
7. Εύρεση 3 κοινών ονομάτων μεταβλητών
