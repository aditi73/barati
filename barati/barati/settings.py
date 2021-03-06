"""
Django settings for barati project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hr&a0391=urx=8bpf!!@uyscs6b2aou)dkq^xgm28(1l4cc^2t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*",]

'''EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER =  'username@gmail.com'
EMAIL_HOST_PASSWORD = 'password' 
DEFAULT_FROM_EMAIL = 'username@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
'''
# Application definition

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'contactus@barati.in'
EMIAL_HOST_PASSWORD = 'Welc0me123!#'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',   
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'crispy_forms',
    'rest_framework',
    'axes', # Defense mechanism against Brute Force attack
    'haystack', #Search mechanism
    'customers',
    'vendors',
    'star_ratings', #Rating system #https://github.com/wildfish/django-star-ratings
    'avatar',
    'el_pagination',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',  #http://psa.matiasaguirre.net/docs/configuration/django.html
)

ROOT_URLCONF = 'barati.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

#http://django-el-pagination.readthedocs.org/en/latest/start.html#installation
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'barati.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'barati',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',          # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")

LOGIN_URL = '/auth/login/'
#LOGIN_REDIRECT_URL = '/dashboard'

STATICFILES_FINDERS = (
	"django.contrib.staticfiles.finders.FileSystemFinder",
	"django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
      	'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
	)
}

#Social Auth plugin: http://psa.matiasaguirre.net/docs/configuration/django.html
AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   #'social.backends.google.GoogleOAuth2',
   #'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_FACEBOOK_KEY = 1710233362554820
SOCIAL_AUTH_FACEBOOK_SECRET = '131c039e7bdc74edaf8b823ce2f2dc3d'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/dashboard'
SOCIAL_AUTH_SANITIZE_REDIRECTS = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/dashboard'
SOCIAL_AUTH_URLOPEN_TIMEOUT = 30 #seconds

AUTH_PROFILE_MODULE = 'Customers.Users'
#Search
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
ES_DISABLED = False
ES_URLS = ['http://127.0.0.1:9200']
# enable signal processor that for every change in the models will run update_index
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


CRISPY_TEMPLATE_PACK = 'bootstrap3'

AVATAR_AUTO_GENERATE_SIZES=(120,120)
