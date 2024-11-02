from flask import Flask, render_template, request
from qr2 import generateQRcode

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)


@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        data = request.form.get("textInput")
        if data:
            generateQRcode(data, "./static/sample.png")
    return render_template("index.html", active="text")

@app.route("/url", methods=["GET", "POST"])
def url_page():
    if request.method == "POST":
        data = request.form.get("urlInput")
        if data:
            generateQRcode(data, "./static/sample.png")
    return render_template("url.html", active="url")

@app.route("/email", methods=["GET", "POST"])
def email_page():
    if request.method == "POST":
        address = request.form.get("address")
        subject = request.form.get("subject")
        msg = request.form.get("msg")

        data = f"MATMSG:TO:{address};SUB:{subject};BODY:{msg};;"
        ##print(data)
        if address and subject and msg:
            generateQRcode(data, "./static/sample.png")
    return render_template("email.html", active="email")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        contactFname = request.form.get("contactFname")
        contactLname = request.form.get("contactLname")
        contactMobile = request.form.get("contactMobile")
        contactPhone = request.form.get("contactPhone")
        contactCompany = request.form.get("contactCompany")
        contactEmail = request.form.get("contactEmail")

        data = f""
        if data:
            generateQRcode(data, "./static/sample.png")
    return render_template("contact.html", active="contact")

@app.route("/wifi", methods=["GET", "POST"])
def wifi_page():
    if request.method == "POST":
        SSID = request.form.get("SSID")
        wifiPassword = request.form.get("wifiPassword")
        wifiRadio = request.form.get("wifiRadio")

        data = f"WIFI:S:{SSID};T:{wifiRadio};P:{wifiPassword};;"
        if SSID and wifiPassword and wifiRadio :
            generateQRcode(data, "./static/sample.png")
    return render_template("wifi.html", active="wifi")

@app.route("/image", methods=["GET", "POST"])
def image_page():
    if request.method == "POST":
        data = request.form.get("imgInput")
        if data:
            generateQRcode(data, "./static/sample.png")
    return render_template("image.html", active="image")

@app.route("/social", methods=["GET", "POST"])
def social_page():
    if request.method == "POST":
        if request.form.get("Twitter"):
            data = f"https://twitter.com/{request.form.get('TwitterHandle')}"
        elif request.form.get("Facebook"):
            data = f"https://www.facebook.com/{request.form.get('FacebookUsername')}"
        elif request.form.get("Whatsapp"):
            data = f"https://wa.me/{request.form.get('WhatsappNumber')}"
        elif request.form.get("Snapchat"):
            data = f"https://www.snapchat.com/add/{request.form.get('SnapchatUsername')}"
        elif request.form.get("Instagram"):
            data = f"https://www.instagram.com/{request.form.get('InstagramUsername')}"
        elif request.form.get("Telegram"):
            data = f"https://t.me/{request.form.get('TelegramUsername')}"
        else:
            data = None

        if data:
            generateQRcode(data, "./static/sample.png")
    
    return render_template("social.html", active="social")
##testing ..

