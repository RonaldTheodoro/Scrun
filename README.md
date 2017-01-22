# Basic Project

This is just a basic sample for django projects

## How to develop?

1) Clone the repository

2) Create a virtualenv with Python 3.5

3) Activate the virtualenv

4) Install dependencies

5) Configure the instance with .env

```console
mkdir ProjectName
cd ProjectName
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install django
django-admin.py startproject ProjectName . --template=https://github.com/RonaldTheodoro/Basic-Django-Project/archive/master.zip --name=ProjectName
pip install -r requirements-dev.txt
cp contrib/env-sample .env
```

## How to deploy?

1) Create an instance in Heroku

2) Send the configurations to Heroku

3) Define a SECRET_KEY for the instance

4) Define DEBUG=False

6) Send the source code to heroku

```console
heroku create MyApp
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku master --force
```
