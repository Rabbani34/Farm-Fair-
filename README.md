<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f1f0f,50:0a2e0a,100:0d1f0d&height=220&section=header&text=FarmFair%20%E2%80%94%20Smart%20Agriculture%20Marketplace&fontSize=34&fontColor=ffffff&fontAlignY=42&desc=Role-Based%20Platform%20%E2%80%A2%20OTP%20Auth%20%E2%80%A2%20Sales%20Workflow%20%E2%80%A2%20Analytics%20Dashboard&descAlignY=62&descSize=14&descColor=86efac&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0f1f0f)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=0f1f0f)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white&labelColor=0f1f0f)](https://sqlite.org)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black&labelColor=0f1f0f)](https://javascript.info)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white&labelColor=0f1f0f)](https://getbootstrap.com)

<br/>

> **A full-stack web marketplace that directly connects farmers and buyers — with role-based portals, OTP authentication, a complete crop sales workflow, and an admin analytics dashboard.**

</div>

---

## 👥 User Roles

<div align="center">

| Role | Capabilities |
|---|---|
| 🌾 **Farmer** | List crops · Set prices · Manage inventory · View orders |
| 🛒 **Buyer** | Browse listings · Place orders · Track purchases · Rate sellers |
| 🛡️ **Admin** | Full platform control · User management · Analytics · Dispute resolution |

</div>

---

## ✨ Features

- 🔐 **OTP-based authentication** — secure one-time password login for all user types
- 🌾 **Crop listing system** — farmers can add, edit, and manage produce listings
- 🛒 **Complete sales workflow** — browsing → cart → order → payment simulation → confirmation
- 💳 **Payment simulation** — integrated mock payment gateway for end-to-end flow testing
- 📊 **Admin analytics dashboard** — animated statistics, chart-based insights, and marketplace KPIs
- 🔒 **Secure session management** — role-based access control throughout
- 📱 **Responsive design** — Bootstrap-powered UI across all screen sizes

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python · Flask · REST APIs |
| **Database** | SQLite · Relational schema design |
| **Frontend** | HTML5 · CSS3 · JavaScript · Bootstrap |
| **Auth** | OTP system · Flask Sessions |
| **Data Viz** | Chart.js · Animated statistics |

---

## 🚀 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/Rabbani34/Farm-Fair-.git
cd Farm-Fair-

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialise the database
python init_db.py

# 5. Run the app
flask run

# 6. Open in browser
# http://localhost:5000
```

---

## 📁 Project Structure

```
Farm-Fair-/
│
├── app.py                  # Flask app + route registration
├── auth/
│   ├── otp.py              # OTP generation & verification
│   └── routes.py           # Login / register routes
├── farmer/
│   └── routes.py           # Crop listing & management
├── buyer/
│   └── routes.py           # Browse, cart & orders
├── admin/
│   ├── routes.py           # Admin panel
│   └── analytics.py        # Dashboard statistics
├── database/
│   ├── schema.sql           # DB schema
│   └── models.py
├── static/                 # CSS · JS · images
├── templates/              # Jinja2 HTML templates
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Mohammed Rabbani**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rabbani-mohammed-57653b333/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rabbani34)
[![Portfolio](https://img.shields.io/badge/Portfolio-7c3aed?style=flat-square&logo=vercel&logoColor=white)](https://portfolio-sigma-seven-x81lwlz28v.vercel.app/?_vercel_share=49IHQNbb2vXxh0Dx10qyqqvCWZpu7VYo)

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f1f0f,100:0a2e0a&height=100&section=footer&animation=fadeIn" width="100%"/>
</div>
