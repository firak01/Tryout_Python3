'''
Created on 18.10.2026

@author: Fritz Lindhauer
'''

# Ein Datentyp spezifiziert welche Werte eine Instanz haben kann
x="Hallo"
print(type(x)) 


# Es gibt die "Nichts" Instanz , wohl vergleichbar mit Java NULL
y=None
y
print(y)

# Ein wichtiger Unterschied zu Java
# In Python ist None selbst ein Objekt mit dem eigenen Typ NoneType:
print(type(y))