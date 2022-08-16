"""
Django settings for bestprojectever project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cic-v!_5+5k%u@@en(ksgt3rb8o^!tz+b7!=yj8th7l@wfrzrm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# tutaj dodałem adres lokalnego hosta (na razie zakomentowałem, 
# aby zobaczyć czy jest to niezbędne aby działało)
# ALLOWED_HOSTS = ['127.0.0.1']
ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'blog',
    'debug_toolbar',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'frontend',
]

SITE_ID = 1

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'bestprojectever.urls'

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

WSGI_APPLICATION = 'bestprojectever.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Dodatkowe uwagi:
# Przed dodaniem bazy postgresql do django:
# zrobiłem kroki wg instrukcji z: https://medium.com/@rudipy/how-to-connecting-postgresql-with-a-django-application-f479dc949a11
#   a) utworzyłem bazę danych "best_project_ever_db_01"
#   b) utworzyłem użytkownika postresowego "best_project_ever_db_user_01" z hasłem "password"
#   c) ustawiłem encoding na "utf8" - w sumie warto by zadać sobie pytanie: po co?
#   d) zmieniłem domyślny "transaction isolation scheme" na "read committed" - w sumie warto by zadać sobie pytanie: po co?
#   e) zmieniłem timezone na "UTC" - w sumie warto by zadać sobie pytanie: po co?
#   f) nadałem pełne uprawnienia dotyczące bazy danych "best_project_ever_db_01" dla użytkownika "best_project_ever_db_user_01"
#   g) zainstalowanie w venvie django psycopg2 uwaga, podczas instalacji pojawiły się błędy, pomogło:
#       1) kroki z https://stackoverflow.com/questions/26053982/setup-script-exited-with-error-command-x86-64-linux-gnu-gcc-failed-with-exit
#          w szczególności komenda sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
#       2) dopiero po doinstalowaniu powyższego mogłem wykonać właściwe:
#          pipenv install django psycopg2 (choć ostatecznie chyba zadziałało dopiero pip install psycopg2, nie wiem dlaczego w tutorialu powyżej było podane pipenv install django psycopg2, po co tam "django"  - nie wiem)
#   h) w settings.py projektu w DATABASES dodałęm jak poniżej
#   i) później jeszcze zrobiłem python manage.py createsuperuser - ale po co?
#       1) Python.Maciej.Code@gmail.com
#       2) user_1
#       3) password: password

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # czy zadziałało by z ...postgresql ? - zobaczyć z ciekawości
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'blog.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

REST_USE_JWT = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ]
    }
}

SOCIALACCOUNT_AUTO_SIGNUP = False