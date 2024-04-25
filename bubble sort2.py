l=[2,5,8,9,4,7]
n=5
for i in range(n):
   for j in range(n-i-1):
    if l[j]>l[j+1]:
         l[j],l[j+1]=l[j+1],l[j]
print(l)