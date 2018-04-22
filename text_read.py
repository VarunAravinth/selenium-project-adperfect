from __future__ import print_function
file_in = open('sample.txt','r') 
a=file_in.readlines()

for e in a[:]:
    print(e,end='')
file_in.close()
