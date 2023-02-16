from flask_wtf import FlaskForm
from wtforms import StringField, validators, EmailField, SubmitField, TextAreaField


class ContactForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.Length(min=6, max=35)])
    message = TextAreaField('Write your message', [validators.Length(min=6, max=300)])
    submit = SubmitField('Send')
