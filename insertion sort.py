l=[3, 5, 7, 8, 1, 0]
for i in range(1,len(l)):
 key=l[i]
 j=i-1
while j>=0 and l[j]>key:
    l[j+1]=l[j]
    j=j-1
l[j+1]=key
print(l)