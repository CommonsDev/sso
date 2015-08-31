# Single-Sign-On Authentication Provider

This project is an SSO Authentication (or an IdP) system based on
[Oauth2](http://oauth.net/2/) for authorization token exchanges (and therefore
authentication also).

It is compatible with _Python 3.2+_ and based on
[Django](https://www.djangoproject.com/) (version 1.8).


## Pre-requirements

- _Python 3_ (3.2 or later). (it might also work with Python 2.7 or later).
- _git_.
- _pip_ for _Python 3_.


## Installation

1. Download the sources:

    git clone git@github.com:CommonsDev/sso.git

2. Make a virtualenv either using _virtualenvwrapper_ on the more basic
_mkvirtualenv_:

    virtualenv ./venv  # Python 3 version of virtualenv
    source ./venv/bin/activate

  > Make sure to use a _Python 3_ version of `virtualenv` or `mkvirtualenv`.

3. Install dependencies:

  In production

    pip install -r ./sso/requirements.txt

  Or in development

    pip install -r ./sso/requirements_local.txt

4. Configure your private infos:

    cp ./sso/core/settings/private.py{.sample,}

  And customize the file _./sso/core/settings/private.py_.

5. Initialize the database (and the assets):

  In production

    mkdir ../data && chmod a+rw ../data
    ./manage.py migrate --settings=core.settings.prod
    ./manage.py collectstatic --settings=core.settings.prod

  > As we are using sqlite3, the _data_ directory itself and the sqlite file
  must be writable by the web-server.

  Or in a development environment

    ./manage.py migrate


## Configuration

You should customize the _core/settings/prod.py_ to your context.

Adapting `ALLOWED_HOSTS` to avoir _error 400_.


## Running the project

### For development or testing

    `./manage.py runserver`


### In production

The most convenient way might be to use _wsgi_ with your _Nginx_ or _Apache_
web-server.


## Technical details

It is based on these 3rd party libraries:
- https://github.com/evonove/django-oauth-toolkit to deal with the Oauth part.
- https://github.com/macropin/django-registration to manage user accounts.
- https://github.com/ottoyiu/django-cors-headers for CORS compatibility.

The _register_ app overrides django-registration.
