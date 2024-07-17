from flask import Flask, render_template
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms.fields.simple import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
'''
On Windows type:
python -m pip install -r requirements.txt
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = 'some secret'

class LoginForm(FlaskForm):
    name = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if(form.name.data  == 'admin@email.com' and form.password.data  =='123456'):
            return redirect('/success')
        else:
            return redirect('denied')
    return render_template('login.html', form=form)

@app.route("/denied")
def denied():
    return render_template('denied.html')

@app.route("/success")
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True,port=5001)
