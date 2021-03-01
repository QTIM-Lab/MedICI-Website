# base packages
import os

# flask packages
from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv

# load_dotenv(os.path.join('.env')) # local dev

# import pdb; pdb.set_trace()

app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.sendgrid.net',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'apikey',
    "MAIL_PASSWORD": os.environ['SENDGRID_API_KEY'],
    "MAIL_DEFAULT_SENDER": os.environ['MAIL_DEFAULT_SENDER']
}

app.config.update(mail_settings)
mail = Mail(app)
#https://www.twilio.com/blog/using-twilio-sendgrid-to-send-emails-from-python-flask-applications

# routes (needs to be last)
from app import routes