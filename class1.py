class A:
    class B:
        class C:
          a=10
    obj=A()
    obj1=obj.B()
    obj2=obj1.C()
    print(obj2.a)
    