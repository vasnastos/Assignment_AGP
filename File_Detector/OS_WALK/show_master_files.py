import os 

parentroot='../oop-master'

#Εκτύπωση αρχείων φακέλων
for x in os.walk(parentroot,topdown=True):
    print(f'Folder:{x[0]}')
    for k in x[2]:
        print('\t **'+str(k))
    print('=='*20)
