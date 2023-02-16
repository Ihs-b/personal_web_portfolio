from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import os
from contactform import ContactForm
from sendmessage import SendMessage

app = Flask(__name__)
csrf = CSRFProtect(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact_content.db"
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    message = db.Column(db.String)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = Message(name=form.name.data, email=form.email.data, message=form.message.data)
        # send_message = SendMessage(name=form.name.data, their_email=form.email.data, message=form.message.data)
        # send_message.contactme()
        db.session.add(message)
        db.session.commit()
        flash('the message was sent successfully')
        return redirect(url_for('contact'))
        # data = f'{form.name.data}/ {form.email.data} / {form.message.data}'
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)


