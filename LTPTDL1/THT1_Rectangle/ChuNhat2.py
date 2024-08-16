import Rectangle as rect

menu_options = {
    1: 'Thêm hình chữ nhật mới',
    2: 'Hiển thị danh sách hình chữ nhật',
    3: 'Tính tổng diện tích các hình chữ nhật',
    4: 'Hiển thị cách hình chữ nhật có chu vi nhỏ nhất',
    'Other': 'Thoát chương trình'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

dsHCN =[]
while (True):
    print_menu()
    userChoice =''
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except: 
        print('Nhập sai định dạng hãy nhập lại........!')
        continue
    if userChoice == 1:
        cr = float(input("Nhập chiều rộng: "))
        cd = float(input("Nhập chiều dài: "))
        hcn = rect.Rectangle(cr,cd)
        dsHCN.append(hcn)   
    elif userChoice == 2:
        for item in dsHCN:
            item.display()
    elif userChoice == 3:
        dientich = 0.0
        for item in dsHCN:
            dientich = dientich + item.area()
        print(f'Tổng diện tích là: {dientich}') 
    elif userChoice == 4:
        if dsHCN.count == 0:
            print('Danh sách rỗng')
        else:
            chuvinn = dsHCN[0].perimeter()
            for item in dsHCN:
                if chuvinn > item.perimeter():
                    chuvinn = item.perimeter()
            for item in dsHCN:
                if item.perimeter() == chuvinn:
                    item.display()
    else:
        print('Thoát chương trình BYE BYE')
        break

