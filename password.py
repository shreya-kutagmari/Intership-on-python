user_name="shreya"
user_password=1234

name=input("enter your name :")
if name==user_name:
    for i in range(1,4):
        password =int(input("enter your password"))
        if password==user_password:
            print("welcome")
            break
        else:print(f"{i}attempts is done\n {3-i}attempts is done")
        if i==3:print("accout block")
        else:("invalid username")