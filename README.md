# MedICI-Website
A PR Site for the MedICI Integration Platform

## Installation

Use python3 to install requirements.

Install 
```
$ pip install -r requirements
```

On your system set these environment variables:


FLASK_APP:
```
export FLASK_APP=medici_website.py
```

SENDGRID_API_KEY:
```
export SENDGRID_API_KEY=<key>
```

MAIL_DEFAULT_SENDER:
```
export MAIL_DEFAULT_SENDER=<default email>
```

Then run either:
```
flask run
```
for a dev server

or

```
gunicorn medici_website:app
```
for a wsgi based application that could be paired with nginx.

## SSL

Cloudfair attempt backup:

1. Log in to your GoDaddy account

Remove these nameservers:

```
ns73.domaincontrol.com

http://medici-codalab-master.eastus.cloudapp.azure.com/ns74.domaincontrol.com
```


2. Replace with Cloudflare's nameservers:
Nameserver 1
```
ines.ns.cloudflare.com
```

Nameserver 2
```
nero.ns.cloudflare.com
```

Check to make sure they’re correct, then **Save your changes**.


Registrars typically process nameserver updates within 24 hours. Once this process completes, Cloudflare confirms your site activation via email.

Learn how to change nameservers in Cloudflare.