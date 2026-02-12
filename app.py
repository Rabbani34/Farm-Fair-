from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from functools import wraps
import random
from model import db, User, Crop, Order

def login_required(role=None):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if not session.get("logged_in"):
                return redirect("/login")

            if role and session.get("role") != role:
                return redirect("/login")

            return func(*args, **kwargs)

        return wrapper

    return decorator

# CREATE APP FIRST
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmfair.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.secret_key = "farmfair_secret_key"
app.config["SESSION_PERMANENT"] = True

OTP_STORE = {}


# ---------------- API DATA ----------------

farmers_crops = []

# ---------------- PAGE ROUTES ----------------

@app.route("/")
def role():
    return render_template("role.html")




@app.route("/buyer-home")
@login_required("buyer")
def buyer_home():

    available_products = Crop.query.filter_by(status="Available").count()

    orders = Order.query.filter_by(buyer_phone=session["phone"]).all()

    orders_count = len(orders)

    total_spend = sum(o.total_price for o in orders)

    return render_template(
        "buyer_home.html",
        available_products=available_products,
        orders_count=orders_count,
        total_spend=total_spend
    )


@app.route("/admin")
def admin():

    if not session.get("logged_in"):
        return redirect("/login")

    return render_template("admin.html")

@app.route("/admin-home")
def admin_home():

    if not session.get("logged_in") or session.get("role") != "admin":
        return redirect("/login")

    total_users = User.query.count()
    total_crops = Crop.query.count()
    total_orders = Order.query.count()

    crops = Crop.query.all()

    return render_template(
        "admin.html",
        users=total_users,
        crops_count=total_crops,
        orders=total_orders,
        crops=crops
    )

@app.route("/admin/update-crop/<int:crop_id>", methods=["POST"])
def admin_update_crop(crop_id):

    if session.get("role") != "admin":
        return redirect("/login")

    crop = Crop.query.get(crop_id)

    crop.price = int(request.form["price"])
    crop.status = request.form["status"]

    db.session.commit()

    return redirect("/admin-home")


@app.route("/language")
def language():
    return render_template("language.html")


@app.route("/buyers")
def buyers():
    return render_template("buyers.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/make-payment")
@login_required("buyer")
def make_payment():

    cart_items = Cart.query.filter_by(buyer_phone=session["phone"]).all()

    total = 0

    for item in cart_items:

        crop = Crop.query.get(item.crop_id)

        if item.quantity > crop.quantity:
            return "Not enough stock"

        amount = item.quantity * crop.price
        total += amount

        # Create order
        new_order = Order(
            buyer_phone=session["phone"],
            farmer_phone=crop.farmer_phone,
            crop_id=crop.id,
            quantity=item.quantity,
            total_price=amount,
            status="Paid"
        )

        # Reduce stock
        crop.quantity -= item.quantity

        if crop.quantity == 0:
            crop.status = "Sold"

        # Credit farmer wallet
        farmer = User.query.filter_by(phone=crop.farmer_phone).first()
        farmer.wallet += amount

        db.session.add(new_order)

    # Clear cart
    Cart.query.filter_by(buyer_phone=session["phone"]).delete()

    db.session.commit()

    return redirect("/buyer-home")


@app.route("/marketplace")
@login_required("buyer")
def marketplace():

    crops = Crop.query.filter_by(status="Available").all()

    return render_template("marketplace.html", crops=crops)


# ---------------- API ROUTES ----------------

@app.route("/add_crop_db", methods=["POST"])
def add_crop_db():

    data = request.json

    new_crop = Crop(
        farmer_phone=session.get("phone"),
        crop_name=data["name"],
        quantity=int(data["quantity"]),
        price=int(data["price"]),
        location=data["location"]
    )

    db.session.add(new_crop)
    db.session.commit()

    return jsonify({"message": "Crop Added"})

@app.route('/get_crops')
def get_crops():
    return jsonify(farmers_crops)


@app.route('/predict_price', methods=['POST'])
def predict_price():

    crop = request.json['crop']

    price = model.predict_crop_price(crop)

    return jsonify({"price": price})


@app.route("/add-to-cart", methods=["POST"])
@login_required("buyer")
def add_to_cart():

    crop_id = request.form.get("crop_id")
    qty = int(request.form.get("quantity"))

    crop = Crop.query.get(crop_id)

    if qty > crop.quantity:
        return "Not enough stock"

    cart = session.get("cart", [])

    cart.append({
        "crop_id": crop.id,
        "name": crop.crop_name,
        "price": crop.price,
        "quantity": qty,
        "farmer_phone": crop.farmer_phone
    })

    session["cart"] = cart

    return redirect("/cart")

@app.route("/cart")
@login_required("buyer")
def cart():

    cart = session.get("cart", [])
    total = sum(item["price"] * item["quantity"] for item in cart)

    return render_template("cart.html", cart=cart, total=total)

@app.route("/checkout", methods=["POST"])
@login_required("buyer")
def checkout():

    cart = session.get("cart", [])
    buyer = User.query.filter_by(phone=session["phone"]).first()

    total = sum(item["price"] * item["quantity"] for item in cart)

    if buyer.wallet < total:
        return "Insufficient Balance"

    for item in cart:

        crop = Crop.query.get(item["crop_id"])

        order = Order(
            buyer_phone=buyer.phone,
            farmer_phone=item["farmer_phone"],
            crop_id=crop.id,
            quantity=item["quantity"],
            total_price=item["price"] * item["quantity"],
            status="Paid"
        )

        crop.quantity -= item["quantity"]
        if crop.quantity <= 0:
            crop.status = "Sold"

        farmer = User.query.filter_by(phone=item["farmer_phone"]).first()
        farmer.wallet += item["price"] * item["quantity"]

        db.session.add(order)

    buyer.wallet -= total

    db.session.commit()

    session["cart"] = []

    return redirect("/buyer-home")  


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        phone = request.form["phone"]
        role = request.form["role"].lower()   # IMPORTANT

        otp = random.randint(1000, 9999)

        session.clear()
        session["otp"] = str(otp)
        session["phone"] = phone
        session["role"] = role

        print("Generated OTP:", otp)

        return redirect(url_for("verify_otp"))

    return render_template("login.html")



@app.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():

    # If session expired
    if "otp" not in session:
        return redirect("/login")

    if request.method == "POST":

        entered_otp = request.form.get("otp", "").strip()
        session_otp = str(session.get("otp")).strip()

        if entered_otp == session_otp:

            phone = session.get("phone")
            role = session.get("role")

            # Mark user as logged in
            session["logged_in"] = True

            # Check if user already exists
            user = User.query.filter_by(phone=phone).first()

            if not user:
                # Create new user
                user = User(
                    phone=phone,
                    role=role,
                    wallet=0   # SAFE because wallet exists in model
                )
                db.session.add(user)
                db.session.commit()

            # Redirect properly based on role
            if role == "buyer":
                return redirect("/buyer-home")

            elif role == "farmer":
                return redirect("/farmer-home")

            elif role == "admin":
                return redirect("/admin-home")

            else:
                return redirect("/")

        else:
            return render_template(
                "otp.html",
                error="Invalid OTP",
                phone=session.get("phone"),
                otp=session.get("otp")
            )

    return render_template(
        "otp.html",
        phone=session.get("phone"),
        otp=session.get("otp")
    )


@app.route("/sell")
def sell():

    if not session.get("logged_in"):
        return redirect("/login")

    phone = session.get("phone")

    crops = Crop.query.filter_by(farmer_phone=phone).all()

    vegetables = [
    "Tomato","Potato","Onion","Carrot","Cabbage",
    "Spinach","Brinjal","Capsicum","Cauliflower",
    "Chilli","Beans","Pumpkin"
]

    return render_template(
        "sell.html",
        crops=crops,
        vegetables=vegetables
    )


@app.route("/add-crop", methods=["POST"])
def add_crop():

    if not session.get("logged_in"):
        return redirect("/login")

    phone = session.get("phone")

    crop_name = request.form["crop"]
    quantity = int(request.form["quantity"])
    price = int(request.form["price"])
    location = request.form["location"]

    new_crop = Crop(
        farmer_phone=phone,
        crop_name=crop_name,
        quantity=quantity,
        price=price,
        location=location
    )

    db.session.add(new_crop)
    db.session.commit()

    return redirect("/sell")


@app.route("/delete-crop/<int:id>")
def delete_crop(id):

    if not session.get("logged_in"):
        return redirect("/login")

    crop = Crop.query.get(id)

    db.session.delete(crop)
    db.session.commit()

    return redirect("/sell")


@app.route("/market")
def market():

    crops = Crop.query.filter_by(status="Available").all()

    return render_template("buyers.html", crops=crops)

@app.route("/resend-otp", methods=["POST"])
def resend_otp():

    otp = random.randint(1000, 9999)

    session["otp"] = otp

    print("Resent OTP:", otp)

    return {
        "status": "success",
        "otp": otp
    }

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

from datetime import datetime
from collections import defaultdict

@app.route("/farmer-home")
@login_required("farmer")
def farmer_home():

    crops = Crop.query.filter_by(farmer_phone=session["phone"]).all()

    farmer = User.query.filter_by(phone=session["phone"]).first()

    if not farmer:
        return redirect("/login")

    # Create chart data
    labels = [crop.crop_name for crop in crops]
    values = [crop.quantity for crop in crops]

    return render_template(
        "farmer_home.html",
        crops=crops,
        wallet=farmer.wallet,
        labels=labels,
        values=values
    )


@app.route("/place-order", methods=["POST"])
@login_required("buyer")
def place_order():

    crop_id = request.form.get("crop_id")
    qty = int(request.form.get("quantity"))

    crop = Crop.query.get(crop_id)

    if qty > crop.quantity:
        return "Not enough stock"

    total = qty * crop.price

    new_order = Order(
        buyer_phone=session["phone"],
        farmer_phone=crop.farmer_phone,
        crop_id=crop.id,
        quantity=qty,
        total_price=total
    )

    crop.quantity -= qty

    if crop.quantity == 0:
        crop.status = "Sold"

    db.session.add(new_order)
    db.session.commit()

    return redirect("/payment")


# ---------------- RUN SERVER ----------------
    
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
