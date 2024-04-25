
def merge(list):
    if len(list)>1:
        mid=len(list)//2
        Left=list[ :mid]
        Right=list[mid: ]
        merge(Left)
        merge(Right)
        L=0
        R=0
        K=0 
        
        while L<len(Left) and R<len(Right):
            if Left[L]>Right[R]:
                list[K]=Right[R]
                R=R+1
            else:
                list[K]=Left[L]
                L=L+1
            K=K+1
        while L<len(Left):
            list[K]=Left[L]
            L=L+1
            K=K+1
        while R<len(Right):
            list[K]=Right[R]
            R=R+1
            K=K+1
list=[4, 3, 8, 7, 1, 2]
merge(list)
print(list)
