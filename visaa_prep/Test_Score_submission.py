x,y,z=map(int,input().split(' '))
l=[]
for i in range(1,x+1):
    l.append(i*y)
if z in l:
    print("YES")
else:
    print("NO")
