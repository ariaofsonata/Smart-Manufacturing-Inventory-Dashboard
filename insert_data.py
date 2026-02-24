import mysql.connector

def insert():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='設定的密碼',
        database='my_practice',
        port=3306
    )
    cursor = conn.cursor()
    
    # 先清空舊資料，避免重複插入
    cursor.execute("TRUNCATE TABLE products")
    
    test_data = [
        ('iPhone 15', 29900),
        ('iPad Air', 19900),
        ('Nike Shoes', 3500)
    ]
    
    cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", test_data)

    conn.commit()
    print(f"✅ [搬運工] 成功匯入 {cursor.rowcount} 筆資料！")
    conn.close()

if __name__ == "__main__":
    insert()