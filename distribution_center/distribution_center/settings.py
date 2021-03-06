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
    
    'rest_framework',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'allauth.socialaccount.providers.microsoft',
    'magiclink',
    'django_extensions',
    'microsoft_auth',



]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',



    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",

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
                'microsoft_auth.context_processors.microsoft',

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
        'HOST': '192.168.64.100', ###db for docker container  192.168.0.38
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
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

AUTHENTICATION_BACKENDS = [
   
   'magiclink.backends.MagicLinkBackend',

    'django.contrib.auth.backends.ModelBackend',

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    'microsoft_auth.backends.MicrosoftAuthenticationBackend',

]

OGIN_REDIRECT_URL = "/"

SOCIALACCOUNT_PROVIDERS = {
    'google':{
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS':{
            'access_type': 'online',
        }
    }
}

#EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST = 'smtp.pop-os.domain'
EMAIL_HOST_USER = 'milankrka@gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_PASSWORD = 'milanradic4102'
EMAIL_USE_SSL = True
#from django.core.mail import send_mail

#send_mail(subject, content, from_email, to_list, fail_silently=False)

# Set Djangos login URL to the magiclink login page
LOGIN_URL = 'magiclink:login'

MAGICLINK_LOGIN_TEMPLATE_NAME = 'magiclink/login.html'
MAGICLINK_LOGIN_SENT_TEMPLATE_NAME = 'magiclink/login_sent.html'
MAGICLINK_LOGIN_FAILED_TEMPLATE_NAME = 'magiclink/login_failed.html'

# Optional:
# If this setting is set to False a user account will be created the first
# time a user requests a login link.
MAGICLINK_REQUIRE_SIGNUP = True
MAGICLINK_SIGNUP_TEMPLATE_NAME = 'magiclink/signup.html'


# Override the login page template. See 'Login page' in the Setup section
MAGICLINK_LOGIN_TEMPLATE_NAME = 'magiclink/login.html'

# Override the login page template. See 'Login sent page' in the Setup section
MAGICLINK_LOGIN_SENT_TEMPLATE_NAME = 'magiclink/login_sent.html'

# Override the template that shows when the user tries to login with a
# magic link that is not valid. See 'Login failed page' in the Setup section
MAGICLINK_LOGIN_FAILED_TEMPLATE_NAME = 'magiclink/login_failed.html'


# If this setting is set to False a user account will be created the first time
# a user requests a login link.
MAGICLINK_REQUIRE_SIGNUP = True
# Override the login page template. See 'Login sent page' in the Setup section
MAGICLINK_SIGNUP_TEMPLATE_NAME = 'magiclink/signup.html'

# Set Djangos login redirect URL to be used once the user opens the magic link
# This will be used whenever a ?next parameter is not set on login
LOGIN_REDIRECT_URL = '/accounts/profile/'

# If a new user is created via the signup page use this setting to send them to
# a different url than LOGIN_REDIRECT_URL when clicking the magic link
# This will fall back to LOGIN_REDIRECT_URL
MAGICLINK_SIGNUP_LOGIN_REDIRECT = '/welcome/'

# Change the url a user is redirect to after requesting a magic link
MAGICLINK_LOGIN_SENT_REDIRECT = 'magiclink:login_sent'

# Ensure the branding of the login email is correct. This setting is not needed
# if you override the `login_email.html` template
MAGICLINK_EMAIL_STYLES = {
    'logo_url': '',
    'background-colour': '#ffffff',
    'main-text-color': '#000000',
    'button-background-color': '#0078be',
    'button-text-color': '#ffffff',
}

# If you want to use your own email templates you can override the text and
# html templates used with:
MAGICLINK_EMAIL_TEMPLATE_NAME_TEXT = 'magiclink/login_email.txt'
MAGICLINK_EMAIL_TEMPLATE_NAME_HTML = 'magiclink/login_email.html'

# How long a magic link is valid for before returning an error
MAGICLINK_AUTH_TIMEOUT = 300  # In second - Default is 5 minutes

# Email address is not case sensitive. If this setting is set to True all
# emails addresses will be set to lowercase before any checks are run against it
MAGICLINK_IGNORE_EMAIL_CASE = True

# When creating a user assign their email as the username (if the User model
# has a username field)
MAGICLINK_EMAIL_AS_USERNAME = True

# Allow superusers to login via a magic link
MAGICLINK_ALLOW_SUPERUSER_LOGIN = True

# Allow staff users to login via a magic link
MAGICLINK_ALLOW_STAFF_LOGIN = True

# Ignore the Django user model's is_active flag for login requests
MAGICLINK_IGNORE_IS_ACTIVE_FLAG = True

# Override the default magic link length
# Warning: Overriding this setting has security implications, shorter tokens
# are much more susceptible to brute force attacks*
MAGICLINK_TOKEN_LENGTH = 50

# Require the user email to be included in the verification link
# Warning: If this is set to false tokens are more vulnerable to brute force
MAGICLINK_VERIFY_INCLUDE_EMAIL = True

# Ensure the user who clicked magic link used the same browser as the
# initial login request.
# Note: This can cause issues on devices where the default browser is
# different from the browser being used by the user such as on iOS)
MAGICLINK_REQUIRE_SAME_BROWSER = True

# Ensure the user who clicked magic link has the same IP address as the
# initial login request.
MAGICLINK_REQUIRE_SAME_IP = True

# The number of times a login token can be used before being disabled
MAGICLINK_TOKEN_USES = 1

# How often a user can request a new login token (basic rate limiting).
MAGICLINK_LOGIN_REQUEST_TIME_LIMIT = 30  # In seconds

# Disable all other tokens for a user when a new token is requested
MAGICLINK_ONE_TOKEN_PER_USER = True

# Include basic anti spam form fields to help stop bots. False by default
# Note: IF you use the default forms you will need to add CSS to your
# page / stylesheet to hide the labels for the anti spam fields.
# See the login.html or signup.html for an example
MAGICLINK_ANTISPAM_FORMS = False
# The shortest time a user can fill out each field and submit a form without
# being considered a bot. The time is per field and defaults to 1 second.
# This means if the form has 3 fields and the user will need to make more than
# 3 seconds to fill out a form.
MAGICLINK_ANTISPAM_FIELD_TIME = 1


# values you got from step 2 from your Mirosoft app
MICROSOFT_AUTH_CLIENT_ID = '78d2209f-56e5-4032-aba0-e998806f3643'
MICROSOFT_AUTH_CLIENT_SECRET = 'e1cb9869-16c7-4c68-b69c-85adc6dd9911'
# Tenant ID is also needed for single tenant applications
MICROSOFT_AUTH_TENANT_ID = 'f8cdef31-a31e-4b4a-93e4-5f571e91255a'
AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

# pick one MICROSOFT_AUTH_LOGIN_TYPE value
# Microsoft authentication
# include Microsoft Accounts, Office 365 Enterpirse and Azure AD accounts
MICROSOFT_AUTH_LOGIN_TYPE = 'ma'

# Xbox Live authentication
MICROSOFT_AUTH_LOGIN_TYPE = 'xbl'  # Xbox Live authentication











