"""
 Γράψτε ένα πρόγραμμα που να εμπεριέχει μια κλάση Lexicon που να διαβάζει τα περιεχόμενα ενός αρχείου με λέξεις της αγγλικής γλώσσας (το αρχείο θα περιέχει μια λέξη ανά σειρά).
  Το πρόγραμμα να προσφέρει μέσω ενός μενού επιλογών τις ακόλουθες λειτουργίες:
-Nα εμφανίζει το πλήθος και εφόσον ο χρήστης επιθυμεί όλες τις λέξεις που έχουν το πλήθος γραμμάτων που θα δίνει ο χρήστης.
-Nα εμφανίζει το πλήθος και εφόσον ο χρήστης επιθυμεί όλες τις λέξεις που ξεκινούν με μια ακολουθία γραμμάτων που θα δίνει ο χρήστης.
-Nα εμφανίζει το πλήθος και εφόσον ο χρήστης επιθυμεί όλες τις λέξεις που τελειώνουν με μια ακολουθία γραμμάτων που θα δίνει ο χρήστης.
-Nα εμφανίζει το πλήθος και εφόσον ο χρήστης επιθυμεί όλες τις λέξεις που περιέχουν μια ακολουθία γραμμάτων που θα 
δίνει ο χρήστης τόσες συνεχόμενες φορές όσες επίσης θα δίνει ο χρήστης.
-Nα εμφανίζει το πλήθος και εφόσον ο χρήστης επιθυμεί όλες τις λέξεις που περιέχουν σε θέσεις που θα επιλέγει 
ο χρήστης συγκεκριμένα γράμματα (για παράδειγμα ba-a-a σημαίνει ότι αναζητείται οποιαδήποτε λέξη 
που περιέχει σε οποιοδήποτε θέση τη σειρά γραμμάτων ba-a-a με το - να σημαίνει οποιοδήποτε γράμμα, οπότε τέτοιες λέξεις είναι οι bahamas και banana).
-Το πρόγραμμα να διαβάζει το αρχείο εισόδου ως παράμετρο γραμμής εντολών (χρησιμοποιήστε ως αρχείο που περιέχει λέξεις της αγγλικής γλώσσας, το αρχείο "wordlist.10000.txt" 
που μπορείτε να μεταφορτώσετε από το https://www.mit.edu/~ecprice/wordlist.10000).
"""

import bs4
import xml
import pip._vendor.requests as req
import re

class Lexicon:
    def __init__(self):
        self.words=[]
    
    def openFile(self,filename):
        self.words.clear()
        with open(filename,'r',encoding="utf-8") as f:
            for x in f:
                self.words.append(x.strip())

    def scap(self):
       self.words.clear()
       url=input('Give your url:')
       page=None
       try:
        page=req.get(url)
       except:
           print('invallid url')
       self.words=page.text.split('\n')
    
    def wordLength(self):
        length=int(input('Give word Length:'))
        return [x for x in self.words if len(x)>length]
    
    def StartsWith(self):
        startstr=input('Give Start Sequence:')
        return [x for x in self.words if x.startswith(startstr)]
    
    def endswith(self):
        endstr=input('Give end sequence string:')
        return [y for y in self.words if y.endswith(endstr)]
    
    def replaysequence(self):
        result=[]
        strn=input('Give word you want to replay:')
        times=int(input('Give times of apperence:'))
        return [x for x in self.words if re.search('.*['+strn+']{'+str(times)+'}.*',x)]

    def sequence(self):
        k=input('Give your selected sequence:')
        return [x for x in self.words if re.match('.*'+k.replace('-','.')+'.*',x)]


l=Lexicon()
l.scap()
print('Words:'+str(len(l.StartsWith())))
print('Words:'+str(len(l.endswith())))
print('Words:'+str(len(l.wordLength())))
print('Words:'+str(len(l.sequence())))
print('Words:'+str(len(l.replaysequence())))
