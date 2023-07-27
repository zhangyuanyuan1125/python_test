'''
death_age = 80

name = input("你的名字：")
age = input("你的年龄：")

print("名字：", name)
print("剩余年龄", death_age - int(age))

age_of_teacher = 33

guess_age = int(input('>>:'))

if guess_age == age_of_teacher:
    print('yes,you are right')
else:
    print("no,it's wrong")
'''
import sys

'''
score = int(input('score:'))

if score > 90:
    print('A')
elif score > 80:
    print('B')
elif score > 70:
    print('C')
else:
    print('D')
'''

'''
num1 = int(input('>>:'))
num2 = int(input('>>:'))
num3 = int(input('>>:'))

if num1 > num2:
    if num1 > num3:
        print("num1最大：", num1)
    else:
        print("num3最大：", num3)
elif num1 < num2:
    if num2 > num3:
        print("num2最大：", num2)
    else:
        print("num3最大：", num3)
else:
    print('其他情况')

max_num = max(num1, num2, num3)
print(max_num)
'''


# 九九乘法表
# a = 1
# while a <= 9:
#     b = 1
#     while b <= a:
#         print(str(b)+'*'+str(a)+"="+str(a * b), end="\t")
#         b += 1
#     print()
#     a += 1

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(i, '*', j, '=', i * j, ' ', end='')
#     print('')

# 阶梯

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1







