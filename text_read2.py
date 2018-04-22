from __future__ import print_function
file_in = open('sample.txt','r') 
a=file_in.read()
for e in a.split('\n'):
    print(e)
#print(a,end='')
file_in.close()
