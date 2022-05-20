import environ
from pathlib import Path
import os


INSTALLED_APPS = [
    'conta.apps.ContaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'dashboard.apps.DashboardConfig',
    'conversor.apps.ConversorConfig',
    'gerador.apps.GeradorConfig',
    'texto.apps.TextoConfig',
    'cores.apps.CoresConfig',
    'tempo.apps.TempoConfig',
    'cotacoes.apps.CotacoesConfig',
    'suporte.apps.SuporteConfig',
    'cookies.apps.CookiesConfig',
    'rest_framework',
    'corsheaders',

]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'conta.authentication.EmailAuthBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easytasks.urls'

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
                'cookies.context_processors.cookies',
            ],
        },
    },
]

WSGI_APPLICATION = 'easytasks.wsgi.application'


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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_REDIRECT_URL = 'dashboard:dashboard_view'
LOGOUT_REDIRECT_URL = 'dashboard:dashboard_view'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

handler404 = 'dashboard.views.notfound_view'


# DJANGO REST FRAMEWORK
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# COOKIES
COOKIES_SESSION_ID = 'cookie'

# WHITENOISE
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# CELERY
CELERY_BEAT_SCHEDULE = {
    'update-cryptocurrency-every-60-seconds': {
        'task': 'cotacoes.tasks.update_cryptocurrency',
        'schedule': 60.0,
        'options': {
            'expires': 45.0,
        },
    },
    'update-currency-every-60-seconds': {
        'task': 'cotacoes.tasks.update_currency',
        'schedule': 60.0,
        'options': {
            'expires': 45.0,
        },
    },
}

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'