from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/')
def render_home():
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def afterLoginClick():
    username = request.form['uname']
    password = request.form['pword']
    print("username",username)
    print("password",password)
    return f"<h1>Name: {username}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
