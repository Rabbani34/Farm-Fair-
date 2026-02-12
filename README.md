# 🌾 FarmFair – Smart Farmer Marketplace

FarmFair is a role-based web application built using **Flask + SQLAlchemy** that connects Farmers and Buyers in a marketplace-style platform (similar to Amazon for crops).

Farmers can list crops, set price & location.
Buyers can browse products, add to cart, and pay using wallet.
Payments are automatically credited to farmers.

---

## 🚀 Features

### 👨‍🌾 Farmer Portal
- Add crops with quantity, price & location
- Delete crop listings
- View current listings
- Wallet balance system
- Auto credit when buyer purchases

### 🛒 Buyer Portal
- Dynamic marketplace (Amazon-style product cards)
- Add to cart system
- Wallet-based payment
- Order creation & stock deduction
- Auto credit to farmer wallet

### 👨‍💼 Admin Portal
- View total users
- View total crops
- View total orders
- Update crop price & status

### 🔐 Authentication
- OTP-based login
- Role-based access (Farmer / Buyer / Admin)
- Session management

---

## 🛠 Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML, CSS
- Jinja2
- Flask-CORS

---

## 📂 Project Structure