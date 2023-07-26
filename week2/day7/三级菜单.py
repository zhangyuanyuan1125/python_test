'''
三级菜单
1.打印省，市，县三级菜单
2.可以一层一层的进入到所有层
3.可返回上一级
4.可随时退出
'''

menu = {
    '山西省':
        {'运城市': {'垣曲县': {}},
         '太原市': {'小店区': {}},
         '晋城市': {'阳城县': {}}}
    ,
    '河北省':

        {'石家庄': {'长安区': {}},
         '唐山市': {'路南区': {}},
         '邯郸市': {'邯山区': {}}}
}

current_layer = menu
parent_layer = []
while True:
    for key in current_layer:
        print(key)
    choice = input('>>>:').strip()
    # if len(choice) == 0:
    #     continue
    if choice in current_layer:
        parent_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layer:
            current_layer = parent_layer.pop()
    else:
        print('查无此项')
