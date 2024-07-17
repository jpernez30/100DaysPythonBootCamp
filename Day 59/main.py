from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def receive_data():
    SMTP_ADDRESS = "smtp.gmail.com"
    EMAIL_ADDRESS = "jovensubacc@gmail.com"
    EMAIL_PASSWORD = "bwmg xjqp uthz zwfa"
    data = request.form
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f'This is the header \n\n Name: {data["name"]} Email: {data["email"]} Phone: {data["phone"]}  \n\n Message: {data["message"]}'.encode("utf-8")
        )
    return "<h1>Successfully sent your message</h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
