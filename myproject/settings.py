# Settings file for CycleWorks.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kenny Shen', 'kenny@oktosys.com'),
    ('Adeel Ahmad Khan', 'adeel2@umbc.edu'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'spectrum_ocbc'
DATABASE_USER = 'spectrum_ocbc'
DATABASE_PASSWORD = 'ocbc1233'
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Asia/Singapore'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

here = os.path.dirname(os.path.abspath(__file__))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = here + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'flls@rf2v#!c-c#a*j7%bwa=fhour%yp^(ksf=i^@=-d8z00j)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'myproject.context_processors.load_sponsors',
    'myproject.context_processors.load_ads',
    'myproject.context_processors.load_session',
    'myproject.context_processors.load_friends',
    'myproject.context_processors.days_until'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'facebook.djangofb.FacebookMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATE_DIRS = (
    here + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'sorl.thumbnail',
    'filebrowser',
    'tinymce',
    'myproject.pages',
    'myproject.highlights',
    'myproject.news',
    'myproject.subhighlights',
    'myproject.ads',
    'myproject.sponsors_panel',
    'myproject.search',
    'myproject.entourage',
    'myproject.socialfeed',
    'myproject.oembed',
    'myproject.multimedia',
)

EVENT_DATE="2010-02-09"

TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {'theme': 'advanced',
    'plugins': "table,paste,searchreplace",
    'theme_advanced_buttons3_add': 'tablecontrols'}

FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
FILEBROWSER_PATH_TINYMCE = MEDIA_ROOT + 'js/tiny_mce/'
FILEBROWSER_URL_TINYMCE = MEDIA_URL + 'js/tiny_mce/'

YOUTUBE_KEY = 'AI39si4W-F4EcvN7xZFuexl6dQBTnUvVb1rLuNkKkYtlsPMlvT9zH9HTCgdqx3WpGX-sXU02bcZ6ZqWfXw_G39ITnrG2kKMO_w'

FACEBOOK_API_KEY = 'b1cb2c1a8482b66317dbb77f129229fe'
FACEBOOK_SECRET_KEY = 'a8e5fdd8c395fb04a43025dbb5c1de0f'

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass

