from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password', # 請確保與 insert_data.py 一致
        database='my_practice',
        port=3306
    )

@app.get("/")
def read_root():
    return {"message": "API 伺服器已連線至 MySQL 資料庫"}

@app.get("/api/inventory")
def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) # 💡 重要，自動幫你轉成 JSON 格式
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    conn.close()
    return data