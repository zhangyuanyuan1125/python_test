'''
三级菜单
1.打印省，市，县三级菜单
2.可以一层一层的进入到所有层
3.可返回上一级
4.可随时退出
'''

menu = {
    '山西省':
        {'运城市': ['垣曲县', '闻喜县', '盐湖区', '永济'],
         '太原市': ['小店区', '万柏林区', '杏花岭区', '迎泽区'],
         '晋城市': ['阳城县', '陵川县', '泽州县', '高平市']}
    ,
    '河北省':

        {'石家庄': ['长安区', '桥西区', '新华区', '赵县'],
         '唐山市': ['路南区', '路北区', '丰南区', '遵化市'],
         '邯郸市': ['邯山区', '丛台区', '邯郸县', '永年县']}
}

back_flag = False
exit_flag = False
while not back_flag and not exit_flag:
    print(menu)
    choice1 = input('请输入choice1：').strip()
    if choice1 == 'q':
        exit_flag = True
    if choice1 in menu:
        while not back_flag and not exit_flag:  # 让程序停在第二层
            for key2 in menu[choice1]:
                print(key2)
            choice2 = input('请输入choice2：').strip()
            if choice2 == 'b':
                back_flag = True
            elif choice2 == 'q':
                exit_flag = True
            if choice2 in menu[choice1]:
                while not back_flag and not exit_flag:
                    for key3 in menu[choice1][choice2]:
                        print(key3)
                    choice3 = input('请输入choice3：').strip()
                    print('last level')
                    if choice3 == 'b':
                        back_flag = True
                    elif choice3 == 'q':
                        exit_flag = True
                else:
                    back_flag = False
        else:
            back_flag = False

