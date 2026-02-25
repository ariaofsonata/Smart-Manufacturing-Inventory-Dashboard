import mysql.connector

def insert():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='my_practice',
        port=3306
    )
    cursor = conn.cursor()
    
    # 先清空舊資料，避免重複插入
    cursor.execute("TRUNCATE TABLE products")
    
    test_data = [
        ('CNC 控制器', 45000),
        ('工業機械手臂軸承', 12500),
        ('液壓泵浦', 28000),
        ('伺服馬達', 35000),
        ('光學感測模組', 8500),
        ('精密導軌', 15000)
    ]
    
    cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", test_data)

    conn.commit()
    print(f"✅ [搬運工] 成功匯入 {cursor.rowcount} 筆資料！")
    conn.close()

if __name__ == "__main__":
    insert()