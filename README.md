# 🏭 智慧製造庫存監控系統 
### Smart Manufacturing Inventory Dashboard

這是一個結合 **前後端分離架構** 與 **容器化技術 (Docker Compose)** 的工業零件監控專案。本系統模擬工廠端的零件庫存管理流程，展現了從底層資料庫存取、API 數據分發到前端視覺化看板的完整開發流程。

---

## 🌟 專案亮點
* **雙運行模式**：程式碼具備自動環境偵測，可在 **本地 (Local Host)** 與 **Docker 容器** 內部無縫切換連線參數。
* **容器化一鍵部署**：利用 Docker Compose 封裝資料庫、API 與前端看板，解決跨平台環境配置差異。
* **API 啟動自動化**：後端 FastAPI 整合了啟動偵測邏輯，系統開啟時會自動檢查並確保 MySQL 資料庫結構 (Schema) 完整。
* **智慧監控看板**：前端 Streamlit 透過 RESTful API 異步獲取數據，提供動態過濾與統計圖表。

---

## 🛠️ 技術棧 (Tech Stack)
| 類別 | 技術 | 說明 |
| :--- | :--- | :--- |
| **虛擬化** | **Docker / Docker Compose** | 負責 MySQL、API、Dashboard 的環境編排與隔離 |
| **後端框架** | **FastAPI (Python)** | 高效能非同步 API 接口，負責數據處理與庫存邏輯 |
| **前端框架** | **Streamlit** | 快速構建工業級數據視覺化介面 |
| **資料庫** | **MySQL 8.0** | 儲存結構化零件數據，具備資料持久化 (Volumes) 能力 |
| **數據處理** | **Pandas / Requests** | 資料清理、轉換與服務間通訊 |

---

## 📂 檔案結構說明
* `api_server.py`: 後端核心，具備 **Startup Event**，能自動初始化資料庫。
* `app.py`: 前端程式，透過 `requests` 向 API 請求數據，實現前後端解耦。
* `init_db.py`: 具備環境偵測功能的資料庫初始化腳本。
* `insert_data.py`: 匯入智慧製造相關測試零件數據（支援本地/容器執行）。
* `docker-compose.yml`: 定義三層架構（db, api, dashboard）的運作邏輯。
* `Dockerfile`: 定義 Python 執行環境的構建流程。

---

## 🚀 快速啟動 (Quick Start)

本專案支援兩種運行模式，請根據您的需求選擇：

### 模式一：Docker 容器化部署 (推薦，一鍵啟動)
1. **啟動全服務**：
   ```bash
   docker-compose up -d --build
   ```

### 2. 匯入測試資料
當容器啟動後，你可以選擇在 Docker 內部或本機環境匯入範例零件數據：

* **透過 Docker 執行 (推薦)**：
    ```bash
    docker exec -it my-api python insert_data.py
    ```

### 3. 訪問服務門戶
系統啟動後，可透過瀏覽器訪問以下位址：

* 📊 **數據視覺化看板**：[http://localhost:8501](http://localhost:8501)
* 🔌 **RESTful API 接口**：[http://localhost:8000/api/inventory](http://localhost:8000/api/inventory)
---
### 模式二：本地開發模式 (Local Development)

1. **啟動 MySQL 容器**：
   確保 Docker Desktop 已開啟，並啟動資料庫服務。
2. **安裝 Python 套件**：
   ```bash
   pip install -r requirements.txt
3. **初始化與啟動**：
   ```bash
   python init_db.py     # 建立資料表
   python insert_data.py # 匯入資料
   ```

   #### 開啟終端機 A 啟動 API
   ```bash
   uvicorn api_server:app --reload
   ```

   #### 開啟終端機 B 啟動看板
   ```bash
   streamlit run app.py
   ```

---

## 📊 數據流架構 (Data Flow)

本專案採用標準的 **三層式架構 (3-Tier Architecture)**：

1.  **Storage Layer (MySQL)**：儲存工業零件的名稱、價格與唯一識別碼，並透過 Docker Volume 實現數據持久化。
2.  **Delivery Layer (FastAPI)**：後端負責邏輯處理，並將資料轉換為 JSON 格式，提供給前端或其他第三方系統。
3.  **Display Layer (Streamlit)**：前端向 API 領取數據後，利用 Pandas 進行即時統計並渲染成互動式圖表。

---

## 👤 作者資訊
**Liao Yuan-shi (廖元獅)**
* **專業背景**：11 年資深/主任機構工程師 (Senior/Supervisor Mechanical Engineer)
* **轉型領域**：數據分析 (Data Analysis) / AI 工程
* **技術核心**：Python, SQL, Docker, Creo Parametric