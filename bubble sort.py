l=[2,7,6,3,8,1]
n=6
for i in range(n):
    for j in range(n-i-1):
       if l[j]>l[j+1]:
         l[j],l[j+1]=l[j+1],l[j]
print(l)