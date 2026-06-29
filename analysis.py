import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_data.csv")

#Plotly Bar Chart Revenue By Product
product_revenue = df.groupby("product")['revenue'].sum().reset_index()

fig = px.bar(product_revenue, x="product", y="revenue", title="Revenue by Product")
fig.write_image("revenue_by_product.png")

#Revenue By Region pie chart
region_revenue = df.groupby('region')["revenue"].sum().reset_index()
fig = px.bar(region_revenue, x="region", y="revenue", title="Revenue by Region", color="region")
fig.write_image("revenue_by_region.png")

#Monthly Revenue Trend Line Chart
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)
monthly_revenue = df.groupby("month")["revenue"].sum().reset_index()
fig = px.line(monthly_revenue, x="month", y="revenue", title="Monthly Revenue Trend", markers=True)
fig.write_image("monthly_revenue_trend.png")