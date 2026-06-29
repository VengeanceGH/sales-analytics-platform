import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = "Sales Analysis", layout = "wide")

df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

st.markdown("<h1 style='text-align: center;'>Sales Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analyze sales data to gain insights into revenue trends, product performance, and regional sales distribution.</p>", unsafe_allow_html=True)


total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
avg_order_value = total_revenue / total_orders

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Average Order Value", f"${avg_order_value:,.2f}")

st.subheader("Filter by Region")
selected_region = st.selectbox("Choose a region:", ["All"] + list(df["region"].unique()))

if selected_region != "All":
    filtered_df = df[df["region"] == selected_region]
else:
    filtered_df = df    

col1, col2 = st.columns(2)

with col1:
    product_revenue = filtered_df.groupby("product")["revenue"].sum().reset_index()
    fig1 = px.bar(product_revenue, x="product", y="revenue", title="Revenue by Product")
    st.plotly_chart(fig1, use_container_width = True)

with col2:
    region_revenue = filtered_df.groupby("region")["revenue"].sum().reset_index()
    fig2 = px.bar(region_revenue, x="region", y="revenue", title = "Revenue by Region",  color = "region")
    st.plotly_chart(fig2, use_container_width = True)

filtered_df["month"] = filtered_df["date"].dt.to_period("M").astype(str)
monthly_revenue = filtered_df.groupby("month")["revenue"].sum().reset_index()
fig3 = px.line(monthly_revenue, x= "month", y = "revenue", title = "Monthly Revenue Trend", markers = True)
st.plotly_chart(fig3, use_container_width = True)