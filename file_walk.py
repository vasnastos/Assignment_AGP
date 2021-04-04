import os

parentroot='../../oop-master'

def file_parser():
    allfiles=[]
    try:
        for path,_,file in os.walk(top=parentroot,topdown=True):
            allfiles+=[path+'/'+l for l in file if l.endswith('.cpp') or l.endswith('.c') or l.endswith('.hpp') or l.endswith('.h')]
    except FileNotFoundError:
        print('Can not open folder oop-master')
        return list([])
    return allfiles

