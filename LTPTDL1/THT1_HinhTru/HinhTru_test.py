import HinhTru_Model as ht
import sqlite3
menu ={
    1:'1- Đọc dữ liệu từ file HinhTru.db' ,
    2:'2- Thêm mới hình trụ',
    3:'3- Hiển thị danh sách hình trụ',
    4:'4- Lưu danh sách hình trụ xuống file HinhTru.db',
    5:'5- Tính tổng thể tích các hình trụ',
    6:'6- Hiển thị hình trụ có thể tích lớn nhất',
    7:'7- Hiển thị 3 hình trụ có thể tính nhỏ nhất',
    8:'8- Lưu ds vào file outputHinhTru.db',
    'Others':'Thoát'
}

def print_menu():
    for key in menu.keys():
        print (menu[key])
#Khai báo biến lưu trữ hình trụ
listHinhTru = []
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
        fr=sqlite3.connect('D:\Education\Code\Python\LTPTDL1\THT1_HinhTru\HinhTru.db')
        data = fr.execute('''SELECT * FROM HinhTru''')
        for record in data: 
         r = record[0]
         h = record[1]
         hinhtru1 = ht.HinhTru_Model(r,h)
         listHinhTru.append(hinhtru1)

        fr.close()
        for item in listHinhTru:
            item.display()
    elif chon ==2:
        # 2- Thêm mới hình trụ
        r =int(input("Nhập bán kính dáy:"))
        h =int(input("Nhập chiều cao h:"))
        htru =ht.HinhTru_Model(r,h)
        listHinhTru.append(htru)
    elif chon ==3:
        #3- Hiển thị danh sách hình trụ
        if listHinhTru.count ==0:
            print('Danh sách rỗng')
        else:
            for item in listHinhTru:
                item.display()
    elif chon ==4:
        # 4- Lưu danh sách hình trụ xuống file HinhTru.db
        fw =sqlite3.connect('D:\Education\Code\Python\LTPTDL1\THT1_HinhTru\HinhTru.db')
        
        fw.execute('''
        CREATE TABLE IF NOT EXISTS Detail_HinhTru(
            ban_kinh_day INTEGER,
            chieu_cao INTEGER,
            dien_tich_xq FLOAT,
            dien_tich_tp FLOAT,
            the_tich FLOAT
                   
        )
        ''')
        for item in listHinhTru:
            fw.execute('''
            INSERT INTO Detail_HinhTru (ban_kinh_day, chieu_cao, dien_tich_xq, dien_tich_tp, the_tich) 
            VALUES (?, ?, ?, ?, ?)
            ''', (item.r, item.h, item.area_xq(), item.area_tp(), item.theTich()))

        fw.commit()
        fw.close() 
    elif chon ==5:
        t = "{t:.2f}"
        sum_thetich = 0
        #5- Tính tổng thể tích các hình trụ
        for item in listHinhTru:
            sum_thetich = sum_thetich + item.theTich()
        print("Tổng thể tích các hình trụ là: " + t.format(t=sum_thetich))
    elif chon ==6:
        #6- Hiển thị hình trụ có thể tích lớn nhất
        print("Hình Trụ có thể tích lớn nhất là: ")
        max_thetich = 0
        for item in listHinhTru:
            if item.theTich() > max_thetich:
                max_thetich = item.theTich() 
        for item2 in listHinhTru:
            if max_thetich == item2.theTich():
                item2.display()
        
    elif chon ==7:
        #7- Hiển thị 3 hình trụ có thể tính nhỏ nhất
        min = 999999999
        min1 = 999999999
        min2 = 99999999
        for item in listHinhTru:
            if item.theTich() < min:
                min = item.theTich() 
        for item1 in listHinhTru:
            if item1.theTich() < min1 and min < item1.theTich():
                min1 = item1.theTich() 
        for item2 in listHinhTru:
            if item2.theTich() < min2 and min1 < item2.theTich():
                min2 = item2.theTich() 
        for item3 in listHinhTru:
            if min == item3.theTich():
                print("Hình Trụ có thể tích nhỏ nhất là: ")
                item3.display()
            if min1 == item3.theTich():
                print("Hình Trụ có thể tích nhỏ nhì là: ")
                item3.display()
            if min2 == item3.theTich():
                print("Hình Trụ có thể tích nhỏ ba là: ")
                item3.display()
    elif chon ==8:
            fw =open('D:\Education\Code\Python\LTPTDL1\THT1_HinhTru\outputHinhTru.db',mode='w',encoding ='utf-8')
            for item in listHinhTru:
                fw.write(f'{item.r}-{item.h}-{item.area_xq()}-{item.area_tp()}-{item.theTich()}\n')
            fw.close() 
    else:
        print('Kết thúc chương trình') 
        break