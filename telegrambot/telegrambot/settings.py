"""
Django settings for telegrambot project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
from decouple import Csv
from dj_database_url import parse as db_url
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-zfsl4joj8^-s-d87^$_=y9o@@!!0--6ym$nf7&nt1wk$)#%el@)')
# curl -F "url=https://3824-86-49-182-250.ngrok.io/webhook/" https://api.telegram.org/bot\TELEGRAM_TOKEN/setWebhook
TELEGRAM_TOKEN = config('TELEGRAM_TOKEN', default='')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='https://s*******.eu,https://^^^.com', cast=Csv())

# Application definition
INSTALLED_APPS = [
    # 'grappelli',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_spectacular',
    'django_filters',
    'django_crontab',
    'django.contrib.postgres',
    # https://django-reversion.readthedocs.io/en/latest/index.html
    "reversion",
    # 'simple_history',

    'main',
    'core',
]

# CRONJOBS = [
#     ('1 0 * * *', 'core.tasks.check_deletion_time'),
#     # ('* * * * *', 'core.tasks.dump_data')
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'rest_framework_simplejwt.middleware.token_blacklist_middleware.TokenBlacklistMiddleware',
]

ROOT_URLCONF = 'telegrambot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(
                BASE_DIR,
                'docs',
                '_build'
            )
        ],
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

WSGI_APPLICATION = 'telegrambot.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=30),
    "TOKEN_OBTAIN_SERIALIZER": "core.views.CustomTokenObtainPairSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "core.views.CustomTokenRefreshSlidingSerializer",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",'rest_framework_simplejwt.tokens.SlidingToken'),
    # "BLACKLIST_AFTER_ROTATION": True,
    # "ROTATE_REFRESH_TOKENS": True,
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Silixcon API',
    'DESCRIPTION': 'Silixcon API for development',
    'VERSION': "0.0.0-DV"
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# sudo service postgresql start
# sudo -u postgres createdb mydatabase -O admin
DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='postgres://telegrambot:admin123@127.0.0.1:5432/telegramdb',
        cast=db_url
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# LOGGING = LOG

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE", default='en-us')

TIME_ZONE = config("TIME_ZONE", default='Europe/Prague')

USE_I18N = config("USE_I18N", default=True, cast=bool)

USE_TZ = config("USE_TZ", default=True, cast=bool)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

DEFAULT_FILE_STORAGE = 'core.views.CustomFileSystemStorage'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# DOCS_ROOT = os.path.join(BASE_DIR, 'docs', '_build', 'html')
# DOCS_URL = '/docs/'

# LOG_ROOT = os.path.join(MEDIA_ROOT, 'log')
# LOG_DJANGO_ROOT = os.path.join(LOG_ROOT, 'django')

# BACKUP_ROOT = os.path.join(BASE_DIR, 'backup')
# BACKUP_NAME = "dumpforcontainer.sql"
# SCRIPT_BACKUP_ROOT = os.path.join(BASE_DIR, 'scripts', 'dump_script.sh')
# SCRIPT_LOADDATA = os.path.join(BASE_DIR, 'scripts', 'load_dump.sh')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Telegram Bot",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Welcome to Bot Admin",

    # Welcome text on the login screen
    "welcome_sign": "Log in",

    # Copyright on the footer
    "copyright": config("FOOTOR_NAME", default=f"Bot v0.0.0-DV)"),
}

JAZZMIN_UI_TWEAKS = {
}

# https://github.com/jazzband/django-tinymce/issues/354
X_FRAME_OPTIONS = 'SAMEORIGIN'
# https://issueantenna.com/repo/jazzband/django-tinymce/issues/389
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')