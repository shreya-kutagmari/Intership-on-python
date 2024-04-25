a=int(input("enter the minimum number of stars:"))
b=int(input("enter the maximum number of stars:"))

rows=(b-a+1)
for i in range(rows):
    print(' '*(rows-i-1)+'* '*(i+a))
for j in range(rows-2,-1,-1):
    print(' '*(rows-j-1)+'* '*(j+a))