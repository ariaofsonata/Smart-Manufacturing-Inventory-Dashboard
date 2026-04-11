from init_db import init
import os
import mysql.connector

# 先確保資料庫與表格存在
init()

def insert():
    # 🕵️ 自動偵測環境
    # 如果是在 Docker 跑，OS 會提供 DB_HOST='db'
    # 如果是在本機跑，os.getenv 會回傳預設值 '127.0.0.1'
    db_host = os.getenv('DB_HOST', '127.0.0.1')
    db_port = os.getenv('DB_PORT', '3307') # Docker 內部通常用 3306，本機對外是 3307

    print(f"📡 偵測到環境，準備連線至: {db_host}:{db_port}")

    try:
        conn = mysql.connector.connect(
            host=db_host,
            port=int(db_port),
            user='root',
            password='jiujk000',
            database='my_practice'
        )
        cursor = conn.cursor()
        
        cursor.execute("TRUNCATE TABLE products")
        
        test_data = [
            ('CNC 控制器', 45000), ('工業機械手臂軸承', 12500),
            ('液壓泵浦', 28000), ('伺服馬達', 35000),
            ('光學感測模組', 8500), ('精密導軌', 15000)
        ]
        
        cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", test_data)
        conn.commit()
        print(f"✅ [搬運工] 成功匯入 {cursor.rowcount} 筆資料！")
        conn.close()

    except Exception as e:
        print(f"❌ 連線失敗！如果你在本機跑，請確認 MySQL 容器是否有啟動。錯誤訊息：{e}")

if __name__ == "__main__":
    insert()