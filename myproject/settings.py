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
MEDIA_ROOT = '%s/media/' % here

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'flls@rf2v#!c-c#a*j7%bwa=fhour%yp^(ksf=i^@=-d8z00j)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

template_dir = here + '/templates'

TEMPLATE_DIRS = (
    template_dir,
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'myproject.pages',
    'myproject.highlights',
    'myproject.news',
)
