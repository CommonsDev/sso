"""
Django settings for sso project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from . import private

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

dirname = os.path.dirname
BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = private.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'register',
    'registration',
    'default',
    'oauth',
    'oauth2_provider',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Must be before CommonMiddleware
    # https://github.com/ottoyiu/django-cors-headers/#setup
    'corsheaders.middleware.CorsMiddleware',
    'oauth.middleware.OAuth2TokenMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'register.middleware.NextRedirectMiddleware',
)

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Project specific configuration

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'assets', 'static')
print(STATIC_ROOT)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'assets', 'media')

CORS_ORIGIN_ALLOW_ALL = True


# See http://django-registration-redux.readthedocs.org/en/latest/quickstart.html#settings
# about the next 2 registration settings.
REGISTRATION_AUTO_LOGIN = True

ACCOUNT_ACTIVATION_DAYS = 7

# Name of the URL to redirect for a logged in user
LOGIN_REDIRECT_URL = 'register_profile'

# Use custom URLs instead of the ones form django-registration-remux
INCLUDE_REGISTER_URL = False

# Name of the URL where a user may login
LOGIN_URL = 'auth_login'


AUTH_USER_MODEL = 'register.User'
