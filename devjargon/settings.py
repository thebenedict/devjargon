"""
Django settings for devjargon project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DEVJARGON_SECRET_KEY"),

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  bool(os.environ.get('DEVJARGON_DJANGO_DEBUG', ''))

TEMPLATE_DEBUG = bool(os.environ.get('DEVJARGON_TEMPLATE_DEBUG', ''))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()

ADMINS = (('MB', 'thebenedict@gmail.com'),  )

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@devjargon.org'
EMAIL_HOST_PASSWORD = os.environ.get("DEVJARGON_EMAIL_HOST_PASSWORD", '')
SERVER_EMAIL = 'robot@devjargon.org'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',
    'detect'
)

CORS_ORIGIN_WHITELIST = (
    'devjargon.org',
    'api.devjargon.org'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'devjargon.exception_logging_middleware.ExceptionLoggingMiddleware',
)

ROOT_URLCONF = 'devjargon.urls'

WSGI_APPLICATION = 'devjargon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DEVJARGON_DB_NAME", ''),
        'USER': os.environ.get("DEVJARGON_DB_USER", ''),
        'PASSWORD': os.environ.get("DEVJARGON_DB_PASSWORD", ''),
        'HOST': os.environ.get("DEVJARGON_DB_HOST", ''),
        'PORT': os.environ.get("DEVJARGON_DB_PORT", ''),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
