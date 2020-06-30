from app import app, Message, mail
from flask import render_template, request

# Views

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/request-challenge')
def request_challenge():
    return render_template('request_challenge.html')

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
                      recipients=["medici.challenge@gmail.com"], # replace with your email for testing
                      body=request.form['message'])
        mail.send(msg)


    return render_template('index.html')
    
