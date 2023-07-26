# 打印1-100中的奇数
# for i in range(1, 101, 2):  # 2表示步长
#     print("loop:", i)

__username = "zhang"
__passwd = "zhang123"

# # 方法一
# login_success = False
# for i in range(3):
#     username = input("username:")
#     password = input("password:")
#     if username == __username and password == __passwd:
#         print("welcome %s login...." % username)
#         login_success = True
#         break
#     else:
#         print("用户名或密码错误")
# if not login_success:
#     print("错误次数过多，本次服务到此结束")
#
# 方法二
for i in range(3):
    username = input("username:")
    password = input("password:")
    if username == __username and password == __passwd:
        print("welcome %s login...." % username)
        break
    else:
        print("用户名或密码错误")
else:  # 只要for循环正常执行完毕，中间没有被打断，就会执行else语句
    print("错误次数过多，本次服务到此结束")


