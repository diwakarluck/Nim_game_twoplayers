from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

import json
# from datetime import datetime
with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_pass']
)
mail = Mail(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root6240:@localhost/coding'
app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
db = SQLAlchemy(app)


class Contact(db.Model):
    '''
    id,name,phone_num,mes,date,email....id,title,content,date
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False, primary_key=True)
    phone_num = db.Column(db.String(25), nullable=False)
    mes = db.Column(db.String(200), nullable=False)
    # date = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(40), nullable=False)

class Postes(db.Model):
    title = db.Column(db.String(50),primary_key=True)
    sub_title = db.Column(db.String(70))
    byname = db.Column(db.String(50))
    content = db.Column(db.String(100))
    slug = db.Column(db.String(40))


@app.route("/")
def home():

    return render_template('index.html', params = params)

@app.route("/about")
def about():

    return render_template('about.html', params = params)

@app.route("/post/<string:post_slug>", methods = ['GET'])
def post(post_slug):
    post_pass = Postes.query.filter_by(slug='python-first').first()

    return render_template('post.html',params = params, post = post_pass)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    
    if(request.method=='POST'):
        # id = int(1)
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(name=name, phone_num=phone, mes=message, email=email)
        db.session.add(entry)
        db.session.commit()

        mail.send_message('New contact message from '+name,
                          sender = email,
                          recipients =[params['gmail_user']],
                          body = message + "\n" + phone + "\n" + email)

    return render_template('contact.html', params = params)

app.run(debug=True)
