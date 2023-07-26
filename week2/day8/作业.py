'''
三级菜单
1.展示省市县（在文件中）
2.对菜单进行修改
'''

menu = {
    '山西省':
        {'运城市': {'垣曲县': {}},
         '太原市': {'小店区': {}},
         '晋城市': {'阳城县': {}}},
    '河北省':

        {'石家庄': {'长安区': {}},
         '唐山市': {'路南区': {}},
         '邯郸市': {'邯山区': {}}}
}

with open('三级菜单', 'w', encoding='utf8') as f:
    f.write(str(menu))

with open('三级菜单', 'r', encoding='utf8') as f_read, open('三级菜单副本', 'w', encoding='utf8') as f_write:
    first_flag = False
    second_flag = False
    while not first_flag and not second_flag:
        for key in menu:
            print(key)
        choice = input('>>:').strip()
        second_flag = True
    if choice in menu:
        while not first_flag and not second_flag:
            for key1 in menu[choice]:
                print(key1)
            choice1 = input('>>:').strip()
            if choice1 == 'q':
                second_flag = True
            elif choice1 == 'b':
                first_flag = True
            if choice1 in menu[choice]:
                while not first_flag and not second_flag:
                    for key2 in menu[choice][choice1]:
                        print(key2)
                    choice2 = input('>>:').strip()
                    print('last level')
                    if choice2 == 'q':
                        second_flag = True
                    elif choice2 == 'b':
                        first_flag = True
                else:
                    first_flag = False
        else:
            first_flag = False
