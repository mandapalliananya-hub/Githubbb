# app.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

.hero {
    background: linear-gradient(135deg, #ff7a59, #ffb347);
    padding: 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.product-card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    min-height: 260px;
}

.product-title {
    font-size: 22px;
    font-weight: bold;
    color: #333;
}

.price {
    font-size: 20px;
    font-weight: bold;
    color: #ff6f3c;
}

.category {
    background-color: #ffe4d6;
    color: #c45125;
    padding: 5px 10px;
    border-radius: 12px;
    font-size: 13px;
    display: inline-block;
    margin-bottom: 10px;
}

.desc {
    color: #555;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# Sample product data
products = [
    {
        "name": "Urban Sneakers",
        "price": 2499,
        "category": "Fashion",
        "description": "Comfortable everyday sneakers with a clean streetwear look."
    },
    {
        "name": "Wireless Earbuds",
        "price": 1799,
        "category": "Electronics",
        "description": "Bluetooth earbuds with clear sound and long battery life."
    },
    {
        "name": "Minimal Backpack",
        "price": 1299,
        "category": "Accessories",
        "description": "Lightweight backpack perfect for college, work, and travel."
    },
    {
        "name": "Smart Water Bottle",
        "price": 999,
        "category": "Lifestyle",
        "description": "Reusable bottle that helps you track your daily water intake."
    },
    {
        "name": "Cotton Oversized T-Shirt",
        "price": 699,
        "category": "Fashion",
        "description": "Soft cotton oversized T-shirt available in neutral colors."
    },
    {
        "name": "Desk Lamp Pro",
        "price": 1499,
        "category": "Home",
        "description": "Modern LED desk lamp with adjustable brightness levels."
    }
]

# Sidebar
st.sidebar.title("🛒 MiniStore")
st.sidebar.subheader("Categories")

categories = ["All"] + sorted(list(set(product["category"] for product in products)))
selected_category = st.sidebar.radio("Choose category", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart Summary")
st.sidebar.write("Items in cart: 0")
st.sidebar.write("Total: ₹0")
st.sidebar.info("Cart functionality can be added later.")

# Homepage hero section
st.markdown("""
<div class="hero">
    <h1>Welcome to MiniStore</h1>
    <p>Your one-stop demo e-commerce store for fashion, electronics, lifestyle, and home products.</p>
</div>
""", unsafe_allow_html=True)

# Welcome section
st.title("🛍️ MiniStore")
st.write(
    "Discover trending products at affordable prices. "
    "This demo website is built using Streamlit with a modern product-card layout."
)

# Filter products by category
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

# Featured products section
st.header("Featured Products")

# Display products using responsive columns
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div class="category">{product["category"]}</div>
            <div class="product-title">{product["name"]}</div>
            <p class="desc">{product["description"]}</p>
            <p class="price">₹{product["price"]}</p>
        </div>
        """, unsafe_allow_html=True)

        # Demo button
        if st.button(f"Add to Cart", key=product["name"]):
            st.success(f"{product['name']} added to cart!")
    