"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x2l%+f789(ovt%p4&&js+1d0yceell&q!n8zkdblf-$%oonl-!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT=os.path.join(BASE_DIR,"site_media","media")

MEDIA_URL = "/site_media/media/"

STATIC_ROOT=os.path.join(BASE_DIR,"site_media","static")

STATIC_URL="/site_media/static"

STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]

STATICFILES_FINDERS=[
            "django.contrib.staticfiles.finders.FileSystemFinder",
             "django.contrib.staticfiles.finders.AppDirectoriesFinder",
            ]

TEMPLATE_CONTEXT_PROCESSORS=(
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",)
# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sixfaceapp',
    'django.contrib.humanize',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mydb",
        "USER" :  "myuser",
        "PASSWORD" : "emisdb",
        "HOST": "",
        "PORT" : "",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS=[
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",	
]
TEMPLATE_DIRS= [
    os.path.join(BASE_DIR, "templates"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
