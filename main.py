from flask import Flask, render_template, request
from qr2 import generateQRcode

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        data = request.form.get("dataInput")
        if data:
            generateQRcode(data, "./static/sample.png")
    return render_template("index.html", active="text")

@app.route("/url")
def url_page():
    return render_template("url.html", active="url")

@app.route("/email")
def email_page():
    return render_template("email.html", active="email")

@app.route("/contact")
def contact_page():
    return render_template("contact.html", active="contact")

@app.route("/wifi")
def wifi_page():
    return render_template("wifi.html", active="wifi")

@app.route("/image")
def image_page():
    return render_template("image.html", active="image")

@app.route("/social")
def social_page():
    return render_template("social.html", active="social")
##testing ..

