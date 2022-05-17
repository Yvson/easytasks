from .base import *  # noqa

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'settings/.env.production'))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db()
}

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), env("STATIC_ROOT"))
STATIC_URL = env("STATIC_URL")

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

# CACHE
CACHE_MIDDLEWARE_SECONDS = 60

# EMAIL
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = env.int("EMAIL_PORT")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_TIMEOUT = env.int("EMAIL_TIMEOUT")

# CELERY
CELERY_BROKER_URL = env('REDIS_URL')
RESULT_BACKEND = env('REDIS_URL')