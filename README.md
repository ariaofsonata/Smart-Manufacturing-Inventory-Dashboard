# 🏭 智慧製造庫存監控系統 
### Smart Manufacturing Inventory Dashboard

這是一個結合 **前後端分離架構** 與 **容器化技術(Docker)** 的工業零件監控專案。

透過 Python 生態系，實現了從資料庫存取、API 數據提供到前端網頁視覺化的完整流程。

---

## 🌟 專案亮點
* **容器化部署**：使用 Docker 快速配置 MySQL 環境，解決跨平台環境差異問題。
* **三層式架構**：實現了資料庫 (MySQL)、後端 (FastAPI) 與前端 (Streamlit) 的分層架構。
* **真實數據同步**：API 伺服器直接串接 MySQL，確保儀表板數據與資料庫即時同步。
* **互動式分析**：前端提供價格篩選拉桿與動態統計圖表，輔助廠務決策。

---

## 🛠️ 技術棧 (Tech Stack)
| 類別 | 技術 | 說明 |
| :--- | :--- | :--- |
| **虛擬化** | Docker / WSL2 | 容器化資料庫環境部署 |
| **語言** | Python 3.x | 所使用的程式語言與版本 |
| **後端框架** | FastAPI | 高效能 RESTful API 接口開發 |
| **前端框架** | Streamlit | 快速架設互動式數據看板 |
| **資料庫** | MySQL | 結構化數據存儲 |
| **數據處理** | Pandas / Requests | 資料清理與非同步請求處理 |
| **版本控制** | Git / GitHub | 版本管理|

---

## 📂 檔案結構說明
* `api_server.py`: 後端核心，負責連接 MySQL 並提供 RESTful API 接口。
* `app.py`: 前端程式，透過 `requests` 向 API 請求數據並呈現視覺化結果。
* `init_db.py`: 初始化資料庫結構（Schema）。
* `insert_data.py`: 匯入智慧製造相關測試數據。
* `requirements.txt`: 專案所需之 Python 套件清單。

---

## 📊 系統數據流
1. **Storage**: **MySQL** 儲存原始零件資訊（如：CNC 控制器、伺服馬達）。
2. **Delivery**: **FastAPI** 讀取資料庫並轉化為 **JSON** 格式發佈至 `/api/inventory`。
3. **Display**: **Streamlit** 透過 API 領取數據並生成視覺化圖表。

---

## 🚀 快速啟動
請按照以下三個階段完成環境建置與服務啟動：

### Step 1. 環境準備 (Docker & Packages)
首先啟動資料庫容器，並安裝必要的 Python 套件：

```bash
# 1. 啟動 MySQL 容器 (使用 Port 3307 避免衝突)
docker run --name my-db -e MYSQL_ROOT_PASSWORD=jiujk000 -p 3307:3306 -d mysql:8.0

# 2. 安裝 Python 套件依賴

```bash
pip install -r requirements.txt


### Step 2. 資料庫初始化
執行以下指令建立資料表並匯入預設的測試數據：

```bash
# 建立資料庫結構
python init_db.py

# 匯入測試零件資料
```bash
python insert_data.py


### Step 3. 啟動監控服務
請開啟 兩個 終端機視窗，分別執行後端與前端服務：

終端機 A (後端 API)

```bash
uvicorn api_server:app --reload
終端機 B (前端看板)

```bash
streamlit run app.py