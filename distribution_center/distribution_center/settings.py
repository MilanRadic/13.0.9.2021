"""
Django settings for distribution_center project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '69#g#qz3otydrxn13%h_oo!_vs*(wlvlxt-9=29w&y=defgwb+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#
#THIRD_PARTY_APPS = [
    #'social_django',
#]






INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'landingpad',
    
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'distribution_center.urls'

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


WSGI_APPLICATION = 'distribution_center.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'baza',
        'USER': 'postgres',
        'PASSWORD': '123',#visionect
        'HOST': '192.168.64.102', ###db for docker container  192.168.0.38
        'PORT': '5432', ###5432 in docker 8888
    }
}

if os.environ.get('DATABASE.NAME') != None:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("DATABASE.NAME"),
            'USER': os.environ.get("DATABASE.USER"),
            'PASSWORD': os.environ.get("DATABASE.PASSWORD"),
            'HOST': os.environ.get("DATABASE.HOST"),
            'PORT': os.environ.get("DATABASE.PORT"),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
#   {
#        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#    },
#    {
#        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "dashboard"



# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='milankrka@gmail.com',
    to_emails='remzohotic@gmail.com',
    subject='SendGrid test',
    html_content='<strong>DELAAAAAAA</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.body)


LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "dashboard"
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025


REST_FRAMEWORK = {
    'NON:FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

EMAIL_USER_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'milankrka@gmail.com' #os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = 'milanradic4102' #os.environ.get('EMAIL_HOST_PASSWORD')

