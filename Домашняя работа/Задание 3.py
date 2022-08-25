#не получилось:(
x = int(input().split())
o = -1
for i in range(1,len(x)):
    o = o+1
    if x[o]<x[o-1]:
        print(x[o])