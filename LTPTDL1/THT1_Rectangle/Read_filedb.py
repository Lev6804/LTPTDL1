import Rectangle as rect
import sqlite3 

fr=sqlite3.connect('D:\Education\Code\Python\LTPTDL1\HCN.db')
listRectangle = []



 # from math import * 
data = fr.execute('''SELECT * FROM HCN''') 
for record in data: 
    cr = record[0]
    cd = record[1]
    hcn = rect.Rectangle(cr,cd)
    listRectangle.append(hcn)

fr.close()
for item in listRectangle:
    item.display()