import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection(use_db=True):
    # 💡 這裡會根據環境自動切換地址與埠號
    db_host = os.getenv('DB_HOST', '127.0.0.1')
    db_port = int(os.getenv('DB_PORT', '3307'))
    
    config = {
        "host": db_host,
        "port": int(db_port),
        "user": 'root',
        "password": 'jiujk000'
    }
    if use_db:
        config["database"] = 'my_practice'
        
    return mysql.connector.connect(**config)

# 💡 自動化優化：啟動時自動檢查資料庫與表格

@app.on_event("startup")
def startup_event():
    for i in range(10):
        try:
            conn = get_db_connection(use_db=False)
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS my_practice")
            cursor.execute("USE my_practice")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50),
                    price INT
                )
            """)
            conn.commit()
            conn.close()
            print("✅ 資料庫初始化完成")
            break
        except Exception as e:
            print(f"⏳ 等待 MySQL 啟動中... ({i+1}/10)")
            time.sleep(5)

def startup_event():
    try:
        # 先連線但不指定 DB，確保 DB 存在
        conn = get_db_connection(use_db=False)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_practice")
        cursor.execute("USE my_practice")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                price INT
            )
        """)
        conn.commit()
        conn.close()
        print("✅ 自動化：資料庫與表格已檢查並準備就緒")
    except Exception as e:
        print(f"❌ 啟動初始化失敗: {e}")

@app.get("/")
def read_root():
    return {"message": "API 伺服器已啟動，環境變數讀取正常"}

@app.get("/api/inventory")
def get_inventory():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        return {"error": str(e)}