#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-"*len(Belgium))

print(Belgium.replace(",", ":"))

x = Belgium.split(",")
print((int(x[1]))+(int(x[3])))
