import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Demo App", page_icon="📊", layout="wide")

st.title("📊 Streamlit Demo App")
st.markdown("Streamlit Community Cloudのデプロイサンプルです。")

# --- サイドバー ---
st.sidebar.header("設定")
num_points = st.sidebar.slider("データ点数", 50, 500, 200)
chart_type = st.sidebar.selectbox("グラフタイプ", ["散布図", "折れ線", "ヒストグラム"])

# --- データ生成 ---
np.random.seed(42)
df = pd.DataFrame({
    "x": np.random.randn(num_points),
    "y": np.random.randn(num_points),
    "category": np.random.choice(["A", "B", "C"], num_points)
})

# --- グラフ表示 ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("データ可視化")
    if chart_type == "散布図":
        fig = px.scatter(df, x="x", y="y", color="category")
    elif chart_type == "折れ線":
        fig = px.line(df.reset_index(), x="index", y="x", color="category")
    else:
        fig = px.histogram(df, x="x", color="category", barmode="overlay")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("統計情報")
    st.dataframe(df.describe().round(3), use_container_width=True)

# --- データダウンロード ---
st.subheader("データエクスポート")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("CSVダウンロード", csv, "data.csv", "text/csv")

