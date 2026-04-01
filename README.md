# 🏭 智慧製造庫存監控系統 
### Smart Manufacturing Inventory Dashboard

這是一個結合 **前後端分離架構** 與 **容器化技術(Docker)**的工業零件監控專案。

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

\## 🚀 快速啟動

1\. 啟動資料庫 (Docker)：啟動 Docker 容器

請確保您的 Docker Desktop 已啟動，並執行以下指令架設 MySQL 環境：

`docker run --name my-db -e MYSQL_ROOT_PASSWORD=jiujk000 -p 3307:3306 -d mysql:8.0`

註：本專案使用 3307 埠號以避開本機預設衝突。

2\. 安裝依賴環境：`pip install -r requirements.txt`

3\. 初始化資料庫與數據：

依序執行以下指令以建立表格並匯入測試資料：

`python init_db.py`

`python insert\_data.py`

4\. 啟動服務：

開啟兩個終端機分別執行：

 後端 API : `python init_db.py`
 
 前端介面 : `streamlit run app.py`