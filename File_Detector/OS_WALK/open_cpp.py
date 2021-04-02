import os
filepath='../oop-master/lc/final.cpp'
y=open(filepath,'r')
for x in y:
    print(x)
y.close()

"""
  list=[]
  with open(filepath,'r') as f:
      list=f.readlines()
  if len(list)==0:
      print('No in line detected on file')
  for x in list:
      print(x)
"""