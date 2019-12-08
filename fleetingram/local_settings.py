import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fleetingramdb',
        'USER': 'crincon',
        'PASSWORD': 'Berseker00',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEBUG = True