l=list(map(int,input("enter the list values").split(" ")))
key=int(input("enter the key value: "))
for i in range(len(l)):
    if l[i]==key:
        print(f"the value found at {i}th index")
        break
if i==len(l)-1:
    print("not found")
