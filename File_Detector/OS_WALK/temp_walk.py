import os

parentroot='../oop-master'

def show_tuples():
    for x in os.walk(top=parentroot,topdown=True):
        print(x)

#('oop-master\\various\\OPENEDG\\ch4', [], ['copy.cpp', 'fill_n.cpp', 'replace.cpp', 'transform.cpp'])
#oop-master\various\OPENEDG\ch4

#('oop-master\\various\\STL', [],
# ['accumulate.cpp', 'all_any_none.cpp', 'compare_collections.cpp', 'const_iterator.cpp', 'copy.cpp', 'count1.cpp',
#  'countif1.cpp', 'countif2.cpp', 'fill.cpp', 'find1.cpp', 'find2.cpp', 'find3.cpp', 'find4.cpp', 'for_each.cpp', 
# 'insert_iterators.cpp', 'partial_sort.cpp', 'partition.cpp', 'random.cpp', 'remove.cpp', 'remove_duplicates.cpp',
# .cpp', 'reverse.cpp', 'reverse_iterator.cpp', 'rotate.cpp', 'sort1.cpp', 'sort2.cpp', 'swap.cpp', 
# 'tempCodeRunnerFile.cpp', 'transform.cpp'])

"""
  Στοιχεία εγγραφής-->3
  Όνομα Φακέλου-->STL
  Φάκελοι ενσωματωμένοι στον φάκελο STL-->0
  Aρχεια ενσωματωμένα στον φάκελο STL-->accumulate.cpp--transform.cpp
"""

def show_List():
    for x in os.walk(top=parentroot,topdown=True):
        print(x[0])
        print('\tNext Folders')
        print('*******************************************')
        for j in x[1]:
           print(j)
        print('\t Files')
        print('*******************************************')
        for  l in x[2]:
            print(l)
        print('\n\n')

show_tuples()
print('\n')
show_List()



