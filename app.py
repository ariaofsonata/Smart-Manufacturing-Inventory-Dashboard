# 專案運行順序：
# 1. 執行 init_db.py 建立資料庫結構
# 2. 執行 insert_data.py 匯入範例資料
# 3. 執行 streamlit run app.py 啟動此儀表板

import mysql.connector
import pandas as pd
import streamlit as st

# 用來向 API 領取數據
import requests

# 設定網頁標題
st.set_page_config(page_title="智慧製造看板", page_icon="📊")

def load_data_from_api():
    try:
        # 💡 向你的 FastAPI 領取真實的 MySQL 數據
        response = requests.get("http://127.0.0.1:8000/api/inventory")
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        else:
            st.error("API 回傳錯誤")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"連不到 API 伺服器：{e}")
        return pd.DataFrame()

st.title("🏭 智慧工廠：關鍵設備零組件監控系統(API 串接版)")

df = load_data_from_api()

if not df.empty:
    # --- 互動元件 ---
    st.sidebar.header("📊 篩選條件")
    min_price = st.sidebar.slider("篩選高單價組件 (元)", 0, 50000, 10000)
    
    filtered_df = df[df['price'] >= min_price]

    col1, col2 = st.columns(2)
    with col1:
        st.metric("待檢核組件數", len(filtered_df))
    with col2:
        st.metric("組件平均成本", f"{filtered_df['price'].mean():,.0f} 元")

    st.dataframe(filtered_df, use_container_width=True)
    st.bar_chart(filtered_df.set_index("name")["price"])
else:
    st.warning("目前沒有數據，請確認 FastAPI 已經啟動！")