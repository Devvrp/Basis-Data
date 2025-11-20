import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        database="sales_db"
    )

def fetch_query(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def get_customers():
    return fetch_query("SELECT * FROM customers ORDER BY name ASC")

def get_products():
    return fetch_query("SELECT * FROM products ORDER BY name ASC")

def get_orders():
    query = """
    SELECT 
        o.order_id,
        o.order_date,
        c.name AS customer_name,
        o.total_amount
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    ORDER BY o.order_date DESC
    """
    return fetch_query(query)

def get_order_details():
    query = """
    SELECT 
        od.order_detail_id,
        o.order_date,
        c.name AS customer_name,
        p.name AS product_name,
        od.quantity,
        od.price,
        od.subtotal
    FROM order_details od
    JOIN orders o ON od.order_id = o.order_id
    JOIN products p ON od.product_id = p.product_id
    JOIN customers c ON o.customer_id = c.customer_id
    ORDER BY o.order_date DESC
    """
    return fetch_query(query)