import Rectangle as rect
import sqlite3
menu ={
    1:'1- Đọc dữ liệu từ file HCN.db' ,
    2:'2- Thêm mới hình chữ nhật',
    3:'3- Hiển thị danh sách hình chữ nhật',
    4:'4- Lưu danh sách hình chữ nhật xuống file demo4output.txt',
    'Others':'Thoát'
}
listRectangle = []
def print_menu():
    for key in menu.keys():
        print (menu[key])
#Khai báo biến lưu trữ hình chữ nhật
while(True):
    print_menu()
    chon=''
    try:
        chon =int(input('Nhập tùy chọn:'))
    except:
        print('Nhập sai định dạng, hãy nhập lại:')
        continue
    #Kiểm tra các lựa chọn
    if chon ==1:
    #1- Đọc dữ liệu từ file HCN.db
        fr=sqlite3.connect('D:\Education\Code\Python\LTPTDL1\THT1_Rectangle\HCN.db')
        data = fr.execute('''SELECT * FROM HCN''')
        for record in data: 
         cr = record[0]
         cd = record[1]
         hcn = rect.Rectangle(cr,cd)
         listRectangle.append(hcn)

        fr.close()
        for item in listRectangle:
            item.display()
    elif chon ==2:
        # 2- Thêm mới hình chữ nhật
        cr =int(input("Nhập chiều rộng:"))
        cd =int(input("Nhập chiều dài:"))
        hcn =rect.Rectangle(cr,cd)
        listRectangle.append(hcn)
    elif chon ==3:
        #3- Hiển thị danh sách hình chữ nhật
        if listRectangle.count ==0:
            print('Danh sách rỗng')
        else:
            for item in listRectangle:
                item.display()
    elif chon ==4:
        #4- Lưu danh sách hình chữ nhật xuống file demo4output.txt
        fw =open('D:\Education\Code\Python\LTPTDL1\THT1_Rectangle\outpudemo4.txt',mode='w',encoding ='utf-8')
        fw.write("width-length-perimeter-area\n")
        for item in listRectangle:
            fw.write(f'{item.width}-{item.length}-{item.perimeter()}-{item.area()}\n')
        fw.close() 
    else:
        print('Kết thúc chương trình') 
        break