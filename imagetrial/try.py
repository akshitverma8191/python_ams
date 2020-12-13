import sqlite3
data = sqlite3.connect("D:\\python codes\\gui\\bms.db")
pa = data.execute("select * from bms")
sa = sorted(pa)
for row in sa:
    print(row)
data.close()