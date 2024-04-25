list=[1,3,4,6,8,4]
key=9
l=0
r=len(list)-1
while l<=r:
    mid=(l+r)//2
    if list[mid]==key:
        print(f"key find at the index of {mid}")
        break
    elif list[mid]>key:r=mid-1
    else:l=mid+1
if key not in list:
    print("value not found")