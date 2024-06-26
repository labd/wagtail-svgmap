import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAR_DIR = os.path.join(PROJECT_DIR, 'var')
if not os.path.isdir(VAR_DIR):  # pragma: no cover
    os.makedirs(VAR_DIR)

INSTALLED_APPS = [
    'wsm_test',
    'wagtail_svgmap',
]

# wagtail2
INSTALLED_APPS.extend([
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'wagtail_modeladmin',
    'modelcluster',
    'taggit',
])


INSTALLED_APPS.extend([
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
])

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'wsm_test.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
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
WSGI_APPLICATION = 'wsm_test.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'wsm_test.sqlite3'),
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATICFILES_FINDERS = ['django.contrib.staticfiles.finders.AppDirectoriesFinder']
STATIC_ROOT = os.path.join(VAR_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(VAR_DIR, 'media')
MEDIA_URL = '/media/'
WAGTAIL_SITE_NAME = "wsm_test"
BASE_URL = 'http://example.com'
DEBUG = True
SECRET_KEY = 'x'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
WAGTAIL_APPEND_SLASH = False
