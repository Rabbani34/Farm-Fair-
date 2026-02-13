🌾 FarmFair – Smart Farmer Marketplace

FarmFair is a role-based marketplace web application built using Flask + SQLAlchemy.
It connects Farmers and Buyers on a single digital platform — similar to an Amazon-style marketplace for agricultural crops.

Farmers can list crops with price and quantity, while buyers can browse, add items to cart, and purchase using an integrated wallet system. Payments are automatically credited to farmers.

🚀 Key Features
👨‍🌾 Farmer Portal

Add crop listings (price, quantity, location)

Delete existing listings

View active crop listings

Wallet balance tracking

Automatic wallet credit after successful purchase

🛒 Buyer Portal

Dynamic marketplace with product cards

Add-to-cart functionality

Wallet-based checkout system

Automatic stock deduction after purchase

Order creation and transaction tracking

👨‍💼 Admin Portal

Dashboard with total users, crops, and orders

Update crop price

Change crop availability status

🔐 Authentication System

OTP-based login (console generated for demo)

Role-based access control (Farmer / Buyer / Admin)

Session management

🛠 Tech Stack
Technology	Usage
Python 3.x	Backend
Flask	Web Framework
SQLAlchemy	ORM
SQLite	Database (Development)
HTML / CSS	Frontend
Jinja2	Template Engine
📂 Project Structure
FarmFair/
│
├── app.py
├── model.py
├── farmfair.db
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── otp.html
│   ├── buyer_home.html
│   ├── farmer_home.html
│   ├── marketplace.html
│   ├── sell.html
│   ├── admin.html
│
└── static/
    ├── css/
    └── images/

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/Rabbani34/FarmFair.git
cd FarmFair

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt is missing:

pip install flask flask_sqlalchemy flask_cors

4️⃣ Run the Application
python app.py


Application will start at:

http://127.0.0.1:10000

🧪 How It Works

Login using mobile number + role

OTP is generated in the console (demo mode)

Enter OTP for verification

Redirect based on role:

Role	Route
Farmer	/farmer-home
Buyer	/buyer-home
Admin	/admin-home
💰 Payment Flow

Buyer adds items to cart

Buyer checks out using wallet balance

Buyer wallet is deducted

Farmer wallet is automatically credited

Crop stock is reduced

Order record is created

🗄 Database Models
User

id

phone

role

wallet_balance

Crop

id

name

price

quantity

location

farmer_id

status

Order

id

buyer_id

crop_id

quantity

total_price

status

🔒 Security Notes

OTP is console-generated (for development/demo only)

Not production-ready authentication

SQLite used for development purposes

No payment gateway integration (wallet simulation only)

📈 Future Improvements

Real SMS OTP integration

Razorpay / Stripe payment integration

Image upload support for crops

Rating & review system

REST API version

Deployment on Render / Railway / AWS

Docker containerization

Admin analytics dashboard

🌍 Use Case

FarmFair can be extended into:

A rural farmer empowerment platform

Direct farm-to-consumer marketplace

Local mandi digitization system

Agricultural supply chain solution

⭐ License

This project is developed for educational purposes and project exhibitions.

👨‍💻 Author

Rabbani
