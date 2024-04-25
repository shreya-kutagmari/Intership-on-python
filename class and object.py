class A:
    def __init__(self):
        self.b=self.A.()
        #  self.c=self.b.C()
           # self.c.fan()
    class B:
        def __init__(self):
             self.c=self.b.C()
             self.c.fan()
        class C:
            def __init__(self):
                print("c")
            def fan(self):
                print("fan run")

A()