while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multipliction")
    print("4.division")
    print("5.power")
    print("6.modulus")
    choice=input("enter choice(1/2/3/4/5/6):")
    if choice in ('1','2','3','4','5','6'):
        a=int(input("enter the value of a:"))
        b=int(input("enter the value of b"))
        match choice:
            case'1':print("result:",a+b)
            case'2':print("result:",a-b)
            case'3':print("result:",a*b)
            case'4':print("result:",a/b)
            case'5':print("result:",a**b)
            case'6':print("result:",a%b)
    else:
       print("invalid choice")
