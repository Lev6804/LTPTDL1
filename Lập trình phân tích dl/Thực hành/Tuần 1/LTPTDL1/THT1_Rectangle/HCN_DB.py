import sqlite3

# Kết nối đến cơ sở dữ liệu (tạo tệp nếu chưa tồn tại)
conn = sqlite3.connect('HCN.db')

# Tạo đối tượng con trỏ
cursor = conn.cursor()

# Tạo bảng
cursor.execute('''
CREATE TABLE IF NOT EXISTS HCN (
    width INTEGER,
    length INTEGER
)
''')

# Chèn dữ liệu vào bảng
cursor.execute('''
INSERT INTO HCN (width, length) VALUES (2, 4), (4,5)
''')

# Lưu thay đổi
conn.commit()

# Đóng kết nối
conn.close()
