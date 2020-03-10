# base packages
import os

# flask packages
from flask import Flask, render_template, request
from flask_mail import Mail, Message


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




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_mail', methods = ['POST'])
def send_mail():
    print("""
    {}
    {}
    {}
    {}
    """.format(request.form['name'],request.form['email'],request.form['subject'],request.form['message']))

    with app.app_context():
        msg = Message(subject=request.form['subject'],
                      sender=request.form['email'],#app.config.get("MAIL_USERNAME"),
                      recipients=["bbearce@mgh.harvard.edu"], # replace with your email for testing
                      body=request.form['message'])
        mail.send(msg)


    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
