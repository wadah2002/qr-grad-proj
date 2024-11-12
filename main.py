from flask import Flask, render_template, request, flash, redirect, url_for
import re
from qr2 import generateQRcode

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True)
app.secret_key = 'your_secret_key'


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

        app.logger.debug(f"FN: {contactFname}, LN: {contactLname}, Phone: {contactPhone}, Email: {contactEmail}")

        if not contactFname or not contactLname or not contactPhone or not contactEmail :
            flash("Please fill in the needed fields.", "error")
            return redirect(url_for('contact_page')) 

        data = f"BEGIN:VCARD;VERSION:3.0;FN:{contactFname} {contactLname};N:{contactLname};{contactFname};;;TEL;TYPE=CELL:{contactMobile};TEL;TYPE=WORK:{contactPhone};ORG:{contactCompany};EMAIL:{contactEmail};END:VCARD"
        if data:
            generateQRcode(data, "./static/sample.png")
    return render_template("contact.html", active="contact")

@app.route("/wifi", methods=["GET", "POST"])
def wifi_page():
    if request.method == "POST":
        SSID = request.form.get("SSID")
        wifiPassword = request.form.get("wifiPassword")
        encryption = request.form.get("encryption")

        app.logger.debug(f"SSID: {SSID}, wifi: {wifiPassword}, encryption: {encryption}")


        if not SSID or not wifiPassword or not encryption :
            flash("Please fill in all fields.", "error")
            return redirect(url_for('wifi_page'))
        
        # pattern = r'^[\s\S]{1,32}$'
        # if not re.match(pattern, SSID):
        #     flash("please enter a valid wifi address", "error")
        #     return redirect(url_for('wifi_page'))

        data = f"WIFI:S:{SSID};T:{encryption};P:{wifiPassword};;"
        if SSID and wifiPassword and encryption :
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
            data = f"https://twitter.com/{request.form.get('Twitter')}"
        elif request.form.get("Facebook"):
            data = f"https://www.facebook.com/{request.form.get('Facebook')}"
        elif request.form.get("Whatsapp"):
            data = f"https://wa.me/{request.form.get('Whatsapp')}"
        elif request.form.get("Snapchat"):
            data = f"https://www.snapchat.com/add/{request.form.get('Snapchat')}"
        elif request.form.get("Instagram"):
            data = f"https://www.instagram.com/{request.form.get('Instagram')}"
        elif request.form.get("Telegram"):
            data = f"https://t.me/{request.form.get('Telegram')}"
        else:
            data = None

        if data:
            generateQRcode(data, "./static/sample.png")
    
    return render_template("social.html", active="social")
##testing ..