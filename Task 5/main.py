import streamlit as st
import pandas as pd
import plotly.express as px
from config import get_customers, get_products, get_orders, get_order_details

st.set_page_config(page_title="Sales Dashboard", layout="wide")

def format_idr(nilai):
    return f"Rp {nilai:,.0f}".replace(",", ".")

def load_data():
    customers = pd.DataFrame(get_customers(), columns=['id', 'name', 'email', 'phone', 'address', 'birthdate'])
    products = pd.DataFrame(get_products(), columns=['id', 'name', 'description', 'price', 'stock'])
    products['price'] = products['price'].astype(float)
    products['stock'] = products['stock'].astype(int)
    orders = pd.DataFrame(get_orders(), columns=['id', 'date', 'customer', 'total'])
    orders['total'] = orders['total'].astype(float)
    orders['date'] = pd.to_datetime(orders['date'])
    details = pd.DataFrame(get_order_details(), columns=['id', 'date', 'customer', 'product', 'qty', 'price', 'subtotal'])
    details['qty'] = details['qty'].astype(int)
    details['price'] = details['price'].astype(float)
    details['subtotal'] = details['subtotal'].astype(float)
    return customers, products, orders, details

try:
    df_cust, df_prod, df_ord, df_det = load_data()
except Exception as e:
    st.error(e)
    st.stop()

st.sidebar.title("Menu")
page = st.sidebar.radio("", ["Ringkasan", "Pelanggan", "Stok Barang", "Transaksi"])

if page == "Ringkasan":
    st.title("Ringkasan Bisnis")
    c1, c2, c3 = st.columns(3)
    c1.metric("Omzet", format_idr(df_ord['total'].sum()))
    c2.metric("Transaksi", df_ord.shape[0])
    c3.metric("Barang Terjual", df_det['qty'].sum())
    st.divider()
    col_grafik1, col_grafik2 = st.columns(2)
    with col_grafik1:
        st.subheader("Tren Penjualan")
        daily = df_ord.groupby(df_ord['date'].dt.date)['total'].sum().reset_index()
        fig = px.line(daily, x='date', y='total')
        st.plotly_chart(fig, use_container_width=True)
    with col_grafik2:
        st.subheader("Top Produk")
        top = df_det.groupby('product')['qty'].sum().reset_index().sort_values(by='qty', ascending=True)
        fig = px.bar(top, x='qty', y='product', orientation='h')
        st.plotly_chart(fig, use_container_width=True)

elif page == "Pelanggan":
    st.title("Data Pelanggan")
    kota = st.selectbox("Filter Kota", ["Semua"] + list(df_cust['address'].unique()))
    if kota != "Semua":
        view = df_cust[df_cust['address'] == kota]
    else:
        view = df_cust
    st.dataframe(view, use_container_width=True)

elif page == "Stok Barang":
    st.title("Stok Barang")
    st.subheader("Grafik Stok")
    fig = px.bar(df_prod, x='name', y='stock', color='stock')
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Detail Produk")
    df_prod_show = df_prod.copy()
    df_prod_show['price'] = df_prod_show['price'].apply(format_idr)
    st.dataframe(df_prod_show, use_container_width=True)

elif page == "Transaksi":
    st.title("Data Transaksi")
    tab1, tab2 = st.tabs(["Pesanan Masuk", "Rincian Barang"])
    with tab1:
        df_ord_show = df_ord.copy()
        df_ord_show['total'] = df_ord_show['total'].apply(format_idr)
        st.dataframe(df_ord_show, use_container_width=True)
    with tab2:
        df_det_show = df_det.copy()
        df_det_show['price'] = df_det_show['price'].apply(format_idr)
        df_det_show['subtotal'] = df_det_show['subtotal'].apply(format_idr)
        st.dataframe(df_det_show, use_container_width=True)