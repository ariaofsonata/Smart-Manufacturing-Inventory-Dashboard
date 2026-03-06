# 🏭 智慧製造庫存監控系統 
### Smart Manufacturing Inventory Dashboard

這是一個結合 **前後端分離架構** 的工業零件監控專案。
透過 Python 生態系，實現了從資料庫存取、API 數據提供到前端網頁視覺化的完整流程。

---

## 🌟 專案亮點
* **三層式架構**：實現了資料庫 (MySQL)、後端 (FastAPI) 與前端 (Streamlit) 的分層架構。
* **真實數據同步**：API 伺服器直接串接 MySQL，確保儀表板數據與資料庫即時同步。
* **互動式分析**：前端提供價格篩選拉桿與動態統計圖表，輔助廠務決策。

---

## 🛠️ 技術棧 (Tech Stack)
| 類別 | 技術 |
| :--- | :--- |
| **語言** | Python 3.x |
| **後端框架** | FastAPI (高效能、非同步支援) |
| **前端框架** | Streamlit (快速架設數據看板) |
| **資料庫** | MySQL (結構化數據存儲) |
| **版本控制** | Git / GitHub |

---

## 📂 檔案結構說明
* `api_server.py`: 後端核心，負責連接 MySQL 並提供 RESTful API 接口。
* `app.py`: 前端程式，透過 `requests` 向 API 請求數據並呈現視覺化結果。
* `insert_data.py`: 資料庫初始化工具，負責匯入範例零件數據。

---

## 📊 系統數據流
1. **Storage**: **MySQL** 儲存原始零件資訊（如：CNC 控制器、伺服馬達）。
2. **Delivery**: **FastAPI** 讀取資料庫並轉化為 **JSON** 格式發佈至 `/api/inventory`。
3. **Display**: **Streamlit** 透過 API 領取數據並生成視覺化圖表。

\## 🚀 快速啟動

1\. 安裝環境：`pip install -r requirements.txt`

2\. 初始化資料庫：`python init\_db.py`

3\. 匯入範例數據：`python insert\_data.py`

4\. 啟動後端 API：`python -m uvicorn api_server:app --reload`

5\. 啟動網頁：`streamlit run app.py`

> \*\*注意\*\*：請在程式碼中將 `password` 修改為您的 MySQL 密碼。
