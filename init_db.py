import os
import mysql.connector

def init():
    # 🕵️ 強制偵測：確保本機跑的時候抓 127.0.0.1，Docker 跑的時候抓變數
    db_host = os.getenv('DB_HOST', '127.0.0.1')
    db_port = os.getenv('DB_PORT', '3307')

    print(f"🏗️  [環境連線中] 目標：{db_host}:{db_port}")

    try:
        # 💡 核心修正：連線參數必須保持「極簡」，絕對不帶 database
        conn = mysql.connector.connect(
            host=db_host,
            port=int(db_port),
            user='root',
            password='jiujk000'
            # 這裡絕對不要加 database 參數
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            print("✅ 已成功接入 MySQL 伺服器")

            # 🛠️ 執行指令
            print("🛠️  正在確保資料庫 'my_practice' 存在...")
            cursor.execute("CREATE DATABASE IF NOT EXISTS my_practice")
            
            print("🛠️  切換至 'my_practice'...")
            cursor.execute("USE my_practice")
            
            print("🛠️  建立表格 products...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50),
                    price INT
                )
            """)
            
            conn.commit()
            print("✨ [建築師] 初始化全部完成！")
            
            cursor.close()
            conn.close()

    except Exception as e:
        print(f"❌ 初始化 NG：{e}")
        print("\n💡 如果看到 Access Denied，請嘗試執行這行指令：")
        print(f"   docker exec -it my-db mysql -uroot -pjiujk000 -e \"CREATE DATABASE IF NOT EXISTS my_practice;\"")

if __name__ == "__main__":
    init()