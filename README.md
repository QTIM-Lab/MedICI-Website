# MedICI-Website
A PR Site for the MedICI Integration Platform

## Installation

Use python3 to install requirements.

Install 
```
$ pip install -r requirements
```

Copy the .env_sample file and call it .env.
```bash
$ cp .env_sample .env
```

Edit the variables and source the file:
```bash
$ source .env
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
> Note you need to give gunicorn the environment variables as unlike ```flask run``` it wil not automatically read ```.env```. Find the line with ```# load_dotenv(os.path.join('.env')) # local dev``` and uncomment it. To use this you need to have put environment variables in a clone of .env_sample called .env.

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