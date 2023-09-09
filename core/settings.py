import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
from storages.backends.s3boto3 import S3Boto3Storage

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

MAPBOX_KEY = os.environ.get('MAPBOX_KEY')

ALLOWED_HOSTS = [
    '*',
    '127.0.0.1',
    '8000-jbocciadev-sep2023hackt-y8sdu7s4i9n.ws-eu104.gitpod.io',
    'www.team6.cafabr.online',
    '8000-samobrienol-sep2023hack-n6175f17xly.ws-eu104.gitpod.io',
    '8000-jbocciadev-sep2023hackt-2j9zk58vqyb.ws-eu104.gitpod.io',
    '8000-jbocciadev-sep2023hackt-v6p9qsdicmz.ws-eu104.gitpod.io',
    '8000-jbocciadev-sep2023hackt-ziulmg9562c.ws-eu104.gitpod.io',
    'ecohub.herokuapp.com',
    'ecohub2.herokuapp.com', # just to test
    '8000-jbocciadev-sep2023hackt-plngkesfqdt.ws-eu104.gitpod.io',
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    # 'storages',
    # apps
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'templates', 'home'),
                os.path.join(BASE_DIR, 'theme', 'templates', 'allauth'),
                
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

WSGI_APPLICATION = 'core.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)


class StaticStorage(S3Boto3Storage):
    location = 'static'


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


USE_AWS = os.environ.get('USE_AWS')

STATIC_URL = "/static/"
MEDIA_URL = "/media/"


if USE_AWS is True:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    AWS_STORAGE_BUCKET_NAME = 'ecohubs'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"   
    AWS_S3_FILE_OVERWRITE = True

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Database Config
DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL)
}

# Database Config
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = 'home'
