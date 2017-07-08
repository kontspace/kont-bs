#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from django.conf import settings


# LOG
DJANGO_LOG_PATH = os.path.join(settings.BASE_DIR, 'logs', 'django.log')
DJANGO_LOG_LEVEL = 'INFO'

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': DJANGO_LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': DJANGO_LOG_LEVEL,
            'class': 'logging.FileHandler',
            'filename': DJANGO_LOG_PATH,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': DJANGO_LOG_LEVEL,
            'propagate': True,
        },
    }
}

if settings.DEBUG:
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']
