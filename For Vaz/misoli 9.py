raq=input()
max1=-1  
max2=-1 
for ch in raq:
    d=int(ch)
    if d>max1:
        max2=max1   
        max1=d 
    elif d!=max1 and d>max2:
        max2=d 
if max2==-1:
    print()
else:
    print(max2)