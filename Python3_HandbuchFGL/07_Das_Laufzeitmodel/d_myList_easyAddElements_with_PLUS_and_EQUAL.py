'''
Created on 17.10.2026

@author: Fritz Lindhauer
'''

a=[1,2]
b=a
print(a)
idA=id(a)
idB=id(b)

a+=[3,4]
print(a)
idA=id(a)

if idA==idB:
    print("ids von a und b bleiben gleich, Überraschung. Anders als bei Strings wird mit += bei Listen keine neue Instanz angelegt")
    print("darum ist auch b von der Manipulation in a betroffen")
    print(b)
else:
    print("ids von a und b sind nicht mehr(!) gleich... das ist nicht erwartbar")


