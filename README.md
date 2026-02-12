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

FarmFair/ │ ├── app.py ├── model.py ├── farmfair.db ├── requirements.txt │ ├── templates/ │   ├── login.html │   ├── otp.html │   ├── buyer_home.html │   ├── farmer_home.html │   ├── marketplace.html │   ├── sell.html │   ├── admin.html │ └── static/ ├── css/ └── images/

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rabbani34/FarmFair.git
cd FarmFair

2️⃣ Create Virtual Environment (Recommended)

python -m venv venv

Activate:

venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

If requirements file is missing, install manually:
pip install flask flask_sqlalchemy flask_cors

4️⃣ Run the Application
python app.py

App will run at:
http://127.0.0.1:10000

🧪 How It Works
Login using mobile number + role
OTP is generated in console
Enter OTP
Role-based redirection:
Farmer → /farmer-home
Buyer → /buyer-home
Admin → /admin-home

💰 Payment Flow
Buyer adds items to cart
Buyer checks out using wallet
Buyer wallet is deducted
Farmer wallet is credited
Crop stock is reduced
Order is created

🗄 Database Models
User
id
phone
role
wallet

Crop
id
farmer_phone
crop_name
quantity
price
location
status

Order
id
buyer_phone
farmer_phone
crop_id
quantity
total_price
status

🔒 Security Notes
OTP is console-generated (for demo purposes)
Not production-ready authentication
SQLite used for development only

📈 Future Improvements
Real SMS OTP integration
Razorpay / Stripe payment integration
Image upload for crops
Order tracking system
Rating & review system
REST API version
Deployment on Render / Railway / AWS

⭐ License
This project is for educational use.

