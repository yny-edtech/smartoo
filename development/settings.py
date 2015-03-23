"""
Django settings for smartoo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '24o@tak8xtx)mr*@uia!_(abl5jnru(@-_u^4&t@0c$t$zy=a1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ADMINS = (('Tomas Effenberger', 'xeffenberger@gmail.com'))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'django_extensions',

    # my apps
    'common',
    'abstract_component',
    'knowledge',
    'exercises',
    'practice',
    'smartoo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'smartoo.urls'

WSGI_APPLICATION = 'development.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# we don't need timezone awereness
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Global templates
#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Sessions
#SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# Caches
# TODO: use Memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        #'LOCATION': 'unique-snowflake'
    }
}


# ===== django_extensions settings =====

# Always use IPython for shell_plus
SHELL_PLUS = "ipython"
