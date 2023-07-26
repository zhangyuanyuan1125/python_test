name = input("name:")
age = input("age:")
job = input("job:")
salary = int(input("salary:"))

'''
if salary.isdigit():  # 长得像不像数字，比如‘200’
    salary = int(salary)
else:
    exit("must input digit")  # 退出程序并打印必须输入数字
'''

msg = '''
----info of %s -----
Name : %s
Age : %s
Job : %s
Salary : %d
------END-----------
''' % (name, name, age, job, salary)
print(msg)

