# Single-Sign-On Authentication Provider

This project is an <abbr title="Single Sign-On">SSO</abbr> Authentication
(or <abbr title="Identity Provider">IdP</abbr>) system based on
[Oauth2](http://oauth.net/2/) for authorization token exchanges (and therefore authentication also).

It is compatible with _Python 3.2+_ and based on
[Django](https://www.djangoproject.com/) (version 1.10).


## Pre-requirements

- _Python 3_ (3.2 or later)
- _git_
- _pip_ for _Python 3_.


## Installation

1. Download the sources:

```bash
git clone git@github.com:CommonsDev/sso.git
```

2. Make a virtualenv either using _virtualenvwrapper_ on the more basic
_mkvirtualenv_:

```bash
python3 -m venv ./venv
source ./venv/bin/activate
```

3. Install dependencies:

  In production

```bash
pip install -r ./sso/requirements.txt
```

  Or in development

```bash
pip install -r ./sso/requirements_local.txt
```

4. Configure your private infos:

```bash
cp ./sso/core/settings/private.py{.sample,}
```

  And customize the file _./sso/core/settings/private.py_.

5. Initialize the database (and the assets):

  In production

```bash
mkdir ../data && chmod a+rw ../data
./manage.py migrate --settings=core.settings.prod
./manage.py collectstatic --settings=core.settings.prod
```

  > As we are using sqlite3, the _data_ directory itself and the sqlite file
  must be writable by the web-server.

  Or in a development environment

```bash
./manage.py migrate
```

## Configuration

You should customize the _core/settings/prod.py_ to your context.

Adapting `ALLOWED_HOSTS` to avoir _error 400_.


## Running the project

```bash
./manage.py runserver
```

### Using the web interface authentication

1. [Create a _superuser_](https://docs.djangoproject.com/en/1.10/ref/django-admin/#createsuperuser):
`./manage.py createsuperuser`.

2. Go to http://localhost:8000/ and log in.

3. Go to http://localhost:8000/oauth/applications/register/ to create a
  new application with a "confidential" _client type_ and a
  "authorization code" for the _authorization grant type_. Enter your _redirect
  uri_ (URI's that will receive the _authorization token_).

4. Go to localhost:8000/oauth/authorize/?client_id=MY_CLIENT_ID&response_type=code.
Replace _MY\_CLIENT\_ID_ with your actual client_id provided in the
previous step.
You should be prompted to authorize the app you created to share with your SSO,
and redirected to the URI you provided, with an _authorization code_.


### Using the OAuth API authentication

Example with a _client credential_.

1. Register your app (http://localhost:8000/oauth/applications/register/) with
_client credentials_ as _grant type_, _confidential_ for _client type_.

2. Open a client for querying the API (here using [HTTPie](https://httpie.org/)):

```bash
http --auth MY_CLIENT_ID:MY_CLIENT_SECRET -f http://localhost:8000/oauth/token/ grant_type=client_credentials
```

> Replace "MY_CLIENT_ID" and "MY_CLIENT_SECRET" with these given when
  registering your app.

You should get a JSON response containing an _access token_ like:

```json
{
  "access_token": "4cb7pw6aElBGTpGVeCv9a3m7Yver3r",
  "expires_in": 36000,
  "scope": "write read",
  "token_type": "Bearer"
}
```


## Technical details

It is based on these 3rd party libraries:
- https://github.com/evonove/django-oauth-toolkit and
https://github.com/caffeinehit/django-oauth2-provider for dealing with
the _OAuth_ part.
- https://github.com/macropin/django-registration for managing user accounts.
- https://github.com/ottoyiu/django-cors-headers for CORS compatibility.

The _register_ app overrides _django-registration_.
The _oauth_ app overrides _oauthlib_ and _oauth2_provider_.
