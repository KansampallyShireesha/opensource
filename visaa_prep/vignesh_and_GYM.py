x,y,z=map(int,input().split(" "))
if x>z:
    print(0)
elif x<z and x+y>z:
    print(1)
else:
    print(2)
    
