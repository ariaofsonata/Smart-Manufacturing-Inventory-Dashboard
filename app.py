# 專案運行順序：
# 1. 執行 init_db.py 建立資料庫結構
# 2. 執行 insert_data.py 匯入範例資料
# 3. 執行 streamlit run app.py 啟動此儀表板

import mysql.connector
import pandas as pd
import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="智慧製造看板", page_icon="📊")

def load_data():
    conn = mysql.connector.connect(
        host='localhost',  # 這是你本機電腦的地址
        port=3306,         # 這是 MySQL 的預設門牌號碼
        user='root',
        password='設定的密碼', # 安裝時設定的密碼
        database='my_practice'
    )
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()
    return df

st.title("🚀 我的第一個資料庫儀表板")

try:
    # 1. 執行函式並取得資料
    df = load_data()

    # --- 加入分析師的互動元件 ---
    st.sidebar.header("📊 篩選條件")
    # 建立一個拉桿，讓使用者選擇價格範圍
    min_price = st.sidebar.slider("最低價格篩選", 0, 50000, 10000)

    # 根據拉桿數值過濾資料
    filtered_df = df[df['price'] >= min_price]

    # 使用 columns 讓畫面更好看
    col1, col2 = st.columns(2)
    with col1:
        st.metric("顯示產品數", len(filtered_df))
    with col2:
        st.metric("平均售價", f"{filtered_df['price'].mean():,.0f} 元")

    st.dataframe(filtered_df, use_container_width=True)
    st.bar_chart(filtered_df.set_index("name")["price"])

    # 分析結論
    st.markdown(f"---")
    st.write(f"💡 **分析結論：** 目前高單價產品平均單價為 {filtered_df['price'].mean():,.0f} 元。")

except Exception as e:
    st.error(f"❌ 錯誤：無法讀取資料庫。請確認是否已執行 init_db.py。 (錯誤訊息: {e})")