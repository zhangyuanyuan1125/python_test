_user = "zhang"
_passwd = "zhang123"

counter = 0
while counter < 3:

    username = input("username:")
    password = input("password:")
    if _user == username and _passwd == password:
        print("welcome %s login...." % username)
        break
    else:
        print("用户名或密码错误")
    counter += 1
    if counter == 3:
        choice_again = input("请选择是否继续：【y/n】")
        if choice_again == "y":
            counter = 0

else:  # 只要while循环正常执行完毕，中间没有被打断，就会执行else语句
    print("错误次数过多，本次服务结束")
