# Single-Sign-On Authentication

This project is an SSO Authentication system based on [Oauth2](http://oauth.net/2/) for authorization token exchanges.

It is compatible with _Python 3_ and based on [Django](https://www.djangoproject.com/) (version 1.8).


## Pre-requirements

- _Python 3_ (3.2 or later). (it may also work with Python 2.7 or later)
- _git_.
- _pip_ for _Python 3_.


## Installation

1. Download the sources:
    
    git clone git@github.com:CommonsDev/sso.git

2. Make a virtualenv either using _virtualenvwrapper_ on the basic _mkvirtualenv_:

    virtualenv ./venv
    source ./venv/bin/activate

> Make sure to use a _Python 3_ version of `virtualenv` or `mkvirtualenv`.

3. Install dependencies:

In production

    pip install -r ./sso/requirements.txt

Or in a development environment

    pip install -r ./sso/requirements-local.txt

4. Initialize de database (and the assets):

In production
    
    mkdir ../data && chmod a+rw ../data
    ./manage.py migrate --settings=core.settings.prod
    ./manage.py collectstatic --settings=core.settings.prod

Or in a development environment

    ./manage.py migrate


## Configuration

You should customize the _core/settings/prod.py_ to your context.

Adapting `ALLOWED_HOSTS` to avoir _error 400_.

## Running the project

For local development or testing you can just `python ./manage.py runserver`

For production you should rather a web-server such as _Nginx_ or _Apache_ with _wsgi_.


## Technical details

It is based on these 3rd party libraries:
- https://github.com/evonove/django-oauth-toolkit to deal with the Oauth part.
- https://github.com/macropin/django-registration to manage user accounts.
- https://github.com/ottoyiu/django-cors-headers for CORS compatibility.
