# 使用輕量級 Python 映像檔
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有程式碼
COPY . .

# 暴露 FastAPI (8000) 與 Streamlit (8501) 埠號
EXPOSE 8000 8501

# 啟動腳本 (實務上會用 docker-compose 同時啟動多個服務)
CMD ["sh", "-c", "uvicorn api_server:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]