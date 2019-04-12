import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '5ymxdeav8DyBQvy73SKTxoxBayntuJg5hSZkoPeFY8SuWmwCYD'

DEBUG = False
ALLOWED_HOSTS = ['134.209.71.175', 'steemlogs.info', 'localhost']

PROJECT_APPS = (
    'app',
    'accounts',
)

INSTALLED_APPS = PROJECT_APPS + (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'django_extensions',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# had to change static root to fix the static dev problem, guess they're just the same
STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STEEM_NODES = [
    'https://api.steemit.com',
    'https://steemd.privex.io',
    'https://gtg.steem.house:8090',
    'https://steemd.minnowsupportproject.org',
    'https://rpc.steemliberator.com',
    ]

