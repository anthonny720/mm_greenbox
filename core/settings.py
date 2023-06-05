import os
from datetime import timedelta
from pathlib import Path

import environ

SITE_NAME = 'GreenBox'

# Environ
env = environ.Env()
environ.Env.read_env()
ENVIRONMENT = env

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mm.greenbox.pe', 'www.mm.greenbox.pe', 'greenbox.pe', 'www.greenbox.pe', 'localhost', ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

if not DEBUG:
    CORS_ORIGIN_WHITELIST = ['https://mm.greenbox.pe', 'https://www.mm.greenbox.pe']
    CSRF_TRUSTED_ORIGINS = ['https://mm.greenbox.pe', 'https://www.mm.greenbox.pe']

# Application definition

# Application definition
DJANGO_APPS = ['django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions',
               'django.contrib.messages', 'django.contrib.staticfiles', ]

PROJECT_APPS = ['apps.users', 'apps.config', 'apps.assets', 'apps.management', 'apps.store', ]

THIRD_PARTY_APPS = ['corsheaders', 'simple_history', 'rest_framework', 'import_export', 'djoser',
                    'rest_framework_simplejwt', 'rest_framework_simplejwt.token_blacklist', ]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = ['django.middleware.security.SecurityMiddleware', 'whitenoise.middleware.WhiteNoiseMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware', 'corsheaders.middleware.CorsMiddleware',
              'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware',
              'simple_history.middleware.HistoryRequestMiddleware', ]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'DIRS': [os.path.join(BASE_DIR, 'build')],
              'APP_DIRS': True, 'OPTIONS': {
        'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages', ], }, }, ]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'greenbox_mm',
                         'USER': 'anthonny', 'PASSWORD': 'lO0sBzg&@7Kayr0H^PeT', 'HOST': 'localhost', 'PORT': 5432, }}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
PASSWORD_HASHERS = ["django.contrib.auth.hashers.Argon2PasswordHasher",
                    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
                    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
                    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher", ]
AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
                            {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
                            {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
                            {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', }, ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# Internationalization
LANGUAGE_CODE = 'es-PE'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Rest Framework
REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
                  'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',), }

# JWT

SIMPLE_JWT = {'AUTH_HEADER_TYPES': ('JWT',), 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
              'REFRESH_TOKEN_LIFETIME': timedelta(days=30), 'ROTATE_REFREHS_TOKENS': True,
              'BLACKLIST_AFTER_ROTATION': True, 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',)}

# Djoser
DJOSER = {'LOGIN_FIELD': 'email', 'SERIALIZERS': {'user_create': 'apps.users.serializers.UserCreateSerializer',
                                                  'user': 'apps.users.serializers.UserCreateSerializer',
                                                  'current_user': 'apps.users.serializers.UserCreateSerializer',
                                                  'user_delete': 'djoser.serializers.UserDeleteSerializer', },
          'HIDE_USERS': False, }
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "users.UserAccount"
