l=[2,7,6,3,8,1]
n=len(l)
for i in range(n):
    min=i
    for k in range(i+1,n):
       if l[min]>l[k]:
         min=k

    l[i],l[min]=l[min],l[i]
print(l)