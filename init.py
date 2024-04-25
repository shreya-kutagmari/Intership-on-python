class ECE:
    def __init__(self,*marks):
        self.m1=marks[0]
        self.m2=marks[1]
        self.m3=marks[2]
        self.m4=marks[3]
        self.m5=marks[4]
        self.total()
    def total (self):
        self.total=self.m1+self.m2+self.m3+self.m4+self.m5
    def rank(*self):
        l=[]
        for i in self:
            l.append(i.total)
            sort=sorted(l)
            print(l)
bob=ECE(100,100,100,100,100)
alice=ECE(90,90,90,90,90)

ECE.rank(bob,alice)