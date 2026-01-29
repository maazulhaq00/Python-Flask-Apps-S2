from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/hello/<name>")
def greet(name):
    
    return f"<h3>Hello, {name}</h3>"


@app.route("/aboutcompany")
def about_us():
    return render_template("about.html")

@app.route("/contact")
def contact_us():
    return render_template("contact.html")

@app.route("/shop")
def shop():
    # products = ["T Shirt", "Jeans", "Trousers", "Shirts"]
    products = [
        {
            "name": "T Shirt",
            "price": 350,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "imgUrl": "https://image.made-in-china.com/202f0j00RfYvhGkCHoqn/Oversize-T-Shirt-High-Quality-Cotton-T-Shrit-OEM-Logo.webp",
            "onSale": True
        },
        {
            "name": "Jeans",
            "price": 670,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "imgUrl": "https://image.made-in-china.com/202f0j00RfYvhGkCHoqn/Oversize-T-Shirt-High-Quality-Cotton-T-Shrit-OEM-Logo.webp",
            "onSale": True
        },
        {
            "name": "Trousers",
            "price": 1000,
            "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            "imgUrl": "https://image.made-in-china.com/202f0j00RfYvhGkCHoqn/Oversize-T-Shirt-High-Quality-Cotton-T-Shrit-OEM-Logo.webp",
            "onSale": False
        }
    ]
    return render_template("shop.html", my_products=products)

if __name__ == "__main__":
    app.run(debug=True, port=5004)