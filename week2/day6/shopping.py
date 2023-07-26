product_list = [
    ('mac', 9000),
    ('kindle', 800),
    ('tesla', 900000),
    ('python book', 105),
    ('bike', 2000)
]
saving = input('please your saving:')  # saving本金
li = []
if saving.isdigit():
    saving = int(saving)
    while True:
        for i, v in enumerate(product_list):  # enumerate加编号
            print(i, v)
        product_number = input('请输入要选择的商品编号，退出[q]：')
        if product_number.isdigit():
            product_number = int(product_number)
            if 0 <= product_number < len(product_list):
                product_price = product_list[product_number][1]
                product = product_list[product_number]
                if product_price < saving:
                    saving = saving - product_price
                    print('添加%s成功，还剩余%d元钱' % (product, saving))
                    li.append(product)
                else:
                    print('余额不足，请选择其他商品')
            else:
                print('超过范围，请重新选择')
        elif product_number == 'q':
            print('您已成功购买以下商品：')

            for i in set(li):
                # 需对i进行去重
                print(i, '共'+str(li.count(i))+'份')
            print('您还剩余%s元钱，欢迎下次光临！' % saving)
            break
        else:
            print('输入有误，请重新输入')
else:
    print('输入有误，请重新输入！！！')

