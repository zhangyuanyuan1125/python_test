product_list = [[0, 'iphone6s', 5800], [1, 'mac book', 9000], [2, 'coffee', 32], [3, 'python book', 80],
                [4, 'bicycle', 1500], [5, "quit", 0]]
print("商品列表：", product_list)
salary = int(input('请输入你的工资:'))

li = []
while True:
    product = int(input('请输入要选择的商品编号:'))

    if product < 5:
        if product_list[product][2] <= salary:
            a = product_list[product][1]
            salary = salary - product_list[product][2]
            print("添加%a成功，还剩余%d元钱" % (a, salary))
            li.append(a)
        else:
            balance = product_list[product][2] - salary
            print("余额不足,还差%d元" % balance)
    else:
        print("您已购买以下商品：")
        for i in li:
            print(i)
        print("您还剩余%d元钱,欢迎下次光临" % salary)
        break
