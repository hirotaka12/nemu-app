import streamlit as st
from supabase import create_client, Client

# Supabase接続情報（← ここにあなたの情報を貼ってあります）
SUPABASE_URL = "https://rfdjbrkeebewoiugnoil.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJmZGpicmtlZWJld29pdWdub2lsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA1ODg1OTcsImV4cCI6MjA2NjE2NDU5N30.sb73kPypc8dJ0uWUjOBX2T7n6MOMHJyrEcQk3l9fDSs"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# UI：アプリのタイトル
st.title("🍽️ 献立共有アプリ（Supabase連携）")

# 入力欄
day = st.selectbox("曜日を選んでください", ["月", "火", "水", "木", "金", "土", "日"])
dish = st.text_input("料理名")
ingredients = st.text_area("材料（カンマ区切り）")

if st.button("✅ 献立を追加"):
    if dish:
        data = {"day": day, "dish": dish, "ingredients": ingredients}
        supabase.table("menus").insert(data).execute()
        st.success(f"{day} の献立を追加しました！")
    else:
        st.error("料理名は必須です。")

st.markdown("---")
st.subheader("📋 登録済みの献立")

# 登録データの取得と表示
res = supabase.table("menus").select("*").order("id", desc=False).execute()
menus = res.data

if menus:
    for row in menus:
        st.write(f"**{row['day']}曜日**：{row['dish']}（材料：{row['ingredients']}）")
else:
    st.info("まだ献立が登録されていません。")
