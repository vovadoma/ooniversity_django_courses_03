# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c0=_rfezv335j^u211xqh^!)8*=ian0u+fld#v+9h_idm(r+^v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['www.odexy.in.ua', '127.0.0.1', 'odexy.in.ua', '46.101.14.26']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'quadratic',
    'courses',
    'students',
    'coaches',
    'feedbacks'
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

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


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

LOGGING = {
    'version': 1,

    'formatters': {

        'student': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },

        'course': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'handlers': {

        'file_course': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'courses_logger.log'),
            'formatter': 'course'
        },

        'file_student': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'students_logger.log'),
            'formatter': 'student'
        },
    },

    'loggers': {

        'courses': {
            'handlers': ['file_course'],
            'level': 'DEBUG',
        },

        'students': {
            'handlers': ['file_student'],
            'level': 'WARNING',
        },
    },
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'Vova_Doma'
EMAIL_HOST_PASSWORD = 'x3lS1ImDSe6D'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_HOST = 'mail.ukraine.com.ua'
#EMAIL_HOST_USER = 'admin'
#EMAIL_HOST_PASSWORD = '4R2r9NskRy3D'
#EMAIL_PORT = 25

ADMINS = ['x500@ukr.net']



try:
    from local_settings import *
    print "Used local setting."
except ImportError:
    print "Warning! Local setting not define!"