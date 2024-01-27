from flask import Flask, render_template, request
import smtplib
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
data = response.json()

img_url = "https://images.pexels.com/photos/424154/pexels-photo-424154.jpeg"

gmail = "YOUR GMAIL"
password = "YOUR GMAIL PASSWORD"


@app.route("/")
def home():
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<idx>")
def post(idx):
    idx = int(idx)
    return render_template("post.html", card=data[idx-1], img=img_url)

@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        print(type(name))
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        content = f"Subject: New form Filled\n\nName:{name}\nEmail:{email}\nPhone Number:{phone}\nMessage:{message}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=gmail, password=password)
            connection.sendmail(from_addr=gmail, to_addrs=gmail, msg=content.encode('utf-8'))
        return ("<h1>Successfully sent your information</h1>")

if __name__ == "__main__":
    app.run(debug=True)
