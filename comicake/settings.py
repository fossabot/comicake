"""
Django settings for comicake project.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
"""

import os
from django.contrib import admin
import raven

'''
STOP!

Are you setting ComiCake up with your own settings? Place a file named "local_settings.py"
in the root folder (one directory up from here) and add settings there. You can copy every line
below in the "Important configuration" section to start with. Leave out stuff you don't change.
'''
###########################################
### Important configuration vars ##########
###########################################
DEBUG = True # SECURITY WARNING: don't run with debug turned on in production!
SITE_TITLE = 'ComiCake' # Your site's title
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]'] # Add your domain
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # For reverse proxying
## Services
GA_ID = None # Google Analytics ID (starts with "UA-")
SENTRY_DSN = None # e.g. https://abc:123@sentry.example.com/1
SECRET_KEY = 'GENERATE_YOUR_OWN_VERY_IMPORTANT!' # SECURITY WARNING: keep the secret key used in production secret!
## Paths & Static files # https://docs.djangoproject.com/en/2.0/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
STATIC_URL = '/static/' # Set to absolute path of nginx/apache mapped static dir!
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = os.path.join(STATIC_URL, 'comics/')
MEDIA_ROOT = BASE_DIR + MEDIA_URL
COMPRESS_OUTPUT_DIR = 'assets/cache' # Compressed JS/CSS
COMPRESS_OFFLINE = True
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    #os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
## DB
# Recommended you switch off sqlite in production!
DATABASES = { # Database (https://docs.djangoproject.com/en/2.0/ref/settings/#databases)
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
## Caching
# Recommended you switch to memcached or file cache in production!
XCACHE = 'django.core.cache.backends.locmem.LocMemCache'
if DEBUG:
    CACHE_SHORT = 0
    CACHE_MEDIUM = 0
    CACHE_LONG = 0
else:
    CACHE_SHORT = 60
    CACHE_MEDIUM = 300
    CACHE_LONG = 3600
###########################################
### Don't touch anything below this! ######
###########################################

APP_NAME = 'ComiCake' # Pls no change kthx
admin.site.site_title = APP_NAME
admin.site.site_header = SITE_TITLE
admin.site.index_title = APP_NAME + ' Management System'
ADMIN_LOGO = 'img/logo.svg'
MENU_WEIGHT = {
    'Reader': 1,
}
ADMIN_STYLE = {
    'primary-color': '#111',
    'secondary-color': '#527885',
    'secondary-text': 'white',
    'tertiary-color': '#a4bdc4',
    #'tertiary-text': 'blue', TODO tertiary hover is same as tertiary
    'primary-button': '#1e434f',
    'secondary-button': '#44717f',
    'link-color': '#447e9b',
    }
'''
ADMIN_STYLE = {
    'background': 'white',
    'primary-color': '#205280',
    'primary-text': '#d6d5d2',
    'secondary-color': '#3B75AD',
    'secondary-text': 'white',
    'tertiary-color': '#F2F9FC',
    'tertiary-text': 'black',
    'breadcrumb-color': 'whitesmoke',
    'breadcrumb-text': 'black',
    'focus-color': '#eaeaea',
    'focus-text': '#666',
    'primary-button': '#26904A',
    'primary-button-text':' white',
    'secondary-button': '#999',
    'secondary-button-text': 'white',
    'link-color': '#333',
    'link-color-hover': 'lighten($link-color, 20%)'
}
'''
VERSION = "0.0.1"
GENERATOR = "{} v{}".format(APP_NAME, VERSION)

CACHES = {
    'default': {
        'BACKEND': XCACHE,
        'LOCATION': APP_NAME,
    }
}
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Application definition
RAVEN_CONFIG = { # Sentry config for error reports
    #'dsn-frontend': 'TODO',
    'dsn': SENTRY_DSN,
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}
INSTALLED_APPS = [
    'raven.contrib.django.raven_compat',
    'reader.apps.ReaderConfig',
    'admin_menu',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    #'languages',
    #'debug_toolbar',
    'rest_framework',
    'django_filters',
    'django_cleanup',
    'compressor',
    #'django_markdown' not d2 compatible
    'dynamic_preferences',
    'dynamic_preferences.users.apps.UserPreferencesConfig',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'comicake.urls'

'''{
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/reader'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'comicake.jinja2.environment',
        },
    },'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), #/site
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dynamic_preferences.processors.global_preferences',
                'reader.utils.global_settings'
            ],
        },
    },
]
'''
REST_FRAMEWORK = {
    'PAGE_SIZE': 25
}
'''
# Django Preferences addon settings
DYNAMIC_PREFERENCES = {

    # a python attribute that will be added to model instances with preferences
    # override this if the default collide with one of your models attributes/fields
    'MANAGER_ATTRIBUTE': 'preferences',

    # The python module in which registered preferences will be searched within each app
    'REGISTRY_MODULE': 'preferences',

    # Allow quick editing of preferences directly in admin list view
    # WARNING: enabling this feature can cause data corruption if multiple users
    # use the same list view at the same time, see https://code.djangoproject.com/ticket/11313
    'ADMIN_ENABLE_CHANGELIST_FORM': DEBUG,

    # Customize how you can access preferences from managers. The default is to
    # separate sections and keys with two underscores. This is probably not a settings you'll
    # want to change, but it's here just in case
    'SECTION_KEY_SEPARATOR': '__',

    # Use this to disable caching of preference. This can be useful to debug things
    'ENABLE_CACHE': (not DEBUG),

    # Use this to disable checking preferences names. This can be useful to debug things
    'VALIDATE_NAMES': DEBUG,
}

WSGI_APPLICATION = 'comicake.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Logging
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                        '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'root': {
                'level': 'WARNING',
                'handlers': ['sentry'],
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

USE_I18N = True
USE_L10N = True
USE_TZ = True


#COMPRESS_ROOT = os.path.join(BASE_DIR, 'static/')
#COMPRESS_ENABLED = True

INTERNAL_IPS = '127.0.0.1'
SITE_ID = 1

# Get settings from the file users should be using
try:
    from local_settings import *
except ImportError:
    pass