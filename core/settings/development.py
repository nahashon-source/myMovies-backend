# core/settings/development.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# CORS for frontend communication during dev
CORS_ALLOW_ALL_ORIGINS = True  # 👈 TEMPORARY for dev only

# Dev database (inherits SQLite unless overridden)
# You could override it here if needed.

# Logging (optional but good for debugging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
