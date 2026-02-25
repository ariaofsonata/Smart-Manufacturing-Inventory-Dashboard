import mysql.connector

def init():
    # 連線時先不指定 database，因為我們要親手蓋它
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        port=3306
    )
     # 開始使用
    cursor = conn.cursor()
    
    # 建立資料庫與表格
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_practice")
    cursor.execute("USE my_practice")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            price INT
        )
    """)
    
    # 提交指令並且生效執行
    conn.commit()
    print("✅ [建築師] 資料庫與表格已準備就緒！")
    
    # 連線關閉
    conn.close()

if __name__ == "__main__":
    init()