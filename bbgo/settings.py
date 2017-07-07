# -*- coding: utf-8 -*-
"""
Django settings for bbgo project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from collections import namedtuple
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Theme
THEME = 'haru'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
THEME_DIR = os.path.join(BASE_DIR, 'templates', THEME)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if 'DJANGO_DEBUG' in os.environ:
    if os.environ['DJANGO_DEBUG'] == 'Debug':
        DEBUG = True

ALLOWED_HOSTS = ['gencode.me', 'localhost']


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
)
EDITOR_APPS = (
    'django_summernote',
)
LOCAL_APPS = (
    'core',
    'boards',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + EDITOR_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'bbgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(THEME_DIR),
            os.path.join(TEMPLATES_DIR),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.global_settings',
            ],
            # 'string_if_invalid': 'INVALID_EXPRESSION: %s',
        },
    },
]

WSGI_APPLICATION = 'bbgo.wsgi.application'

# Secrets
# Load sensitive data from secrets.json
try:
    with open(os.path.join(BASE_DIR, "secrets.json")) as f:
        data = json.loads(f.read())
    SecretsNamedTuple = \
        namedtuple('SecretsNamedTuple', data.keys(), verbose=False)
    secrets = SecretsNamedTuple(*[data[x] for x in data.keys()])
    SECRET_KEY = getattr(secrets, "SECRET_KEY")
    DB_NAME = getattr(secrets, "DB_NAME")
    DB_USER = getattr(secrets, "DB_USER")
    DB_PASSWORD = getattr(secrets, "DB_PASSWORD")
    EMAIL_HOST = getattr(secrets, "EMAIL_HOST")
    EMAIL_HOST_USER = getattr(secrets, "EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = getattr(secrets, "EMAIL_HOST_PASSWORD")
    DEFAUL_FROM_EMAIL = getattr(secrets, "DEFAUL_FROM_EMAIL")
    SERVER_EMAIL = getattr(secrets, "SERVER_EMAIL")
except IOError:
    SECRET_KEY = 'k8n13h0y@$=v$uxg*^brlv9$#hm8w7nye6km!shc*&bkgkcd*p'
    DB_NAME = ''
    DB_USER = ''
    DB_PASSWORD = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAUL_FROM_EMAIL = ''
    SERVER_EMAIL = ''

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

LOGIN_REDIRECT_URL = 'login'


# Summernote customization
SUMMERNOTE_CONFIG = {
    'lang': 'ko-KR',
    'width': '100%',
    'toolbar': [
        ['style', ['style']],
        ['font', ['bold', 'italic', 'underline', 'strikethrough']],
        ['super', ['superscript', 'subscript']],
        ['fontname', ['fontname', 'fontsize', 'color', 'clear']],
        ['para', ['height', 'paragraph']],
        ['format', ['ul', 'ol', 'hr', 'table']],
        ['insert', ['link', 'picture', 'video']],
        ['misc', ['codeview']],
    ],
    'attachment_filesize_limit': 2 * 1024 * 1024,
    'external_css': (
        '//http://ajax.aspnetcdn.com/ajax/bootstrap/3.3.7/css/bootstrap.min.css',
    ),
    'external_js': (
        '//https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js',
        '//http://ajax.aspnetcdn.com/ajax/bootstrap/3.3.7/bootstrap.min.js',
    ),
}


# Admin information
ADMIN_EMAIL = 'gencode.me@gmail.com'
ADMIN_TWITTER = 'https://twitter.com/'

# Site information
SITE_NAME = 'bbgo'

# Setting for BOARD
BOARD_STATUS = {
    (u'1normal', u'정상'),
    (u'2temp', u'임시저장'),
    (u'3notice', u'공지'),
    (u'4warning', u'신고접수'),
    (u'5hidden', u'숨김'),
    (u'6deleted', u'삭제됨'),
}
# boards/table.py for more settings

# highlight with coding style for <pre> using highlight.js
ENABLE_CODE_HIGHLIGHT = True

FOOTER_TAGS = '<li>문의, 의견 보내기</li>\
<li><a href="mailto:%s"><img src="/static/icons/email24.png"></a></li>\
<li><a href="%s"><img src="/static/icons/twitter24.png" target="_blank"></a></li>'\
% (ADMIN_EMAIL, ADMIN_TWITTER)
