# Single-Sign-On Authentication Provider

This project is an SSO Authentication (or an IdP) system based on
[Oauth2](http://oauth.net/2/) for authorization token exchanges (and therefore
authentication also).

It is compatible with _Python 3.2+_ and based on
[Django](https://www.djangoproject.com/) (version 1.8).


## Pre-requirements

- _Python 3_ (3.2 or later). (it might also work with Python 2.7 or later)
- _git_
- _pip_ for _Python 3_.


## Installation

1. Download the sources:

        git clone git@github.com:CommonsDev/sso.git

2. Make a virtualenv either using _virtualenvwrapper_ on the more basic
_mkvirtualenv_:

        python3 -m venv ./venv
        source ./venv/bin/activate

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

      ./manage.py runserver


### In production

The most convenient way might be to use _wsgi_ with your _Nginx_ or _Apache_
web-server.


## Testing

### Prerequirements

1. Run this current project:

      ./manage.py runserver


2. Go to http://localhost:8000/registration/register/profile/, register an account if necessary (check your terminal to have a email validation URL).

### with a _confidential client credientials_ grant type

1. Go to http://localhost:8000/oauth/applications/register/ to create a
  new application with a "confidential" _client type_
  and a "client credientials" for the _authorization grant type_.

2. Request a _Bearer token_:

        http --auth MY_CLIENT_ID:MY_CLIENT_SECRET -f http://localhost:8000/oauth/token/ grant_type=client_credentials

  Replace "MY_CLIENT_ID" and "MY_CLIENT_SECRET" with these given when
  registering your app.

  You should get a JSON response like:

      {
        "access_token": "4cb7pw6aElBGTpGVeCv9a3m7Yver3r",
        "expires_in": 36000,
        "scope": "write read",
        "token_type": "Bearer"
      }

> I use [HTTPie](https://github.com/jkbrzt/httpie#installation) here.
  Feel free to adapt it to your favorite (cURL, Postman, etc).


### with a _confidential client credientials_ grant type

Let's use a graphical interface this time.

1. Go to http://localhost:8000/oauth/applications/register/ to create a
  new application with a "confidential" _client type_
  and an "authorization code" for the _authorization grant type_.

2. go to http://django-oauth-toolkit.herokuapp.com/consumer/ and follow
  the instructions.

## Technical details

It is based on these 3rd party libraries:
- https://github.com/evonove/django-oauth-toolkit to deal with the Oauth part.
- https://github.com/macropin/django-registration to manage user accounts.
- https://github.com/ottoyiu/django-cors-headers for CORS compatibility.

The _register_ app overrides django-registration.
