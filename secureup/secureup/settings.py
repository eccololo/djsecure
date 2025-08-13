from pathlib import Path
from decouple import config
from datetime import timedelta

# Django envvars
import environ

# Setting up envvars
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# Uncomment this to run the app on you machine.
# SECRET_KEY = 'django-insecure-2!h05peorzkxp)^dzu73r85ip()sky)nx51@a8%cysnf=hae12'
SECRET_KEY = env("MY_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'secureapp',
    'crispy_forms', # for signup form
    'django_recaptcha', # For reCaptcha
    'django_otp', # for 2FA
    'django_otp.plugins.otp_static', # for 2FA
    'django_otp.plugins.otp_totp', # for 2FA
    'two_factor', # for 2FA
    'axes', # Anti-Brute-Force Attacks
]

# reCaptcha
RECAPTCHA_PUBLIC_KEY = '6LdS4YApAAAAAPmIAySLA7_IvSZa08KN5o7ukiCM'
RECAPTCHA_PRIVATE_KEY = config("RECAPTCHA_PRIVATE_KEY")

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'dashboard'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware', # 2FA
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout', # Auto-Logout
    'axes.middleware.AxesMiddleware', # For Anti-Brute-Force Attacks
]

# For Anti-Brute-Force Attacks
AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'secureup.urls'

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
                'django_auto_logout.context_processors.auto_logout_client', # Auto-Logout
            ],
        },
    },
]

WSGI_APPLICATION = 'secureup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR / 'static/images'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auto-Logout
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=1),
    'SESSION_TIME': timedelta(minutes=2),
    'MESSAGE': 'The session has expired. Please login again to continue.',
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}

# Anti-Brute-Force Attacks configuration settings.
AXES_FAILURE_LIMIT: 3 # How many times user can fail in login.
AXES_COOLOFF_TIME: 2 # Wait 1 hour before user can attempt to login again.
AXES_RESET_ON_SUCCESS = True # Reset failed login attempts when login correctly.
AXES_LOCKOUT_TEMPLATE = 'account-locked.html' # Add a custom template on failure.
AXES_LOCKOUT_PARAMETERS = ["username"] # Admin users are not influenced by failed login attempts.

# Password Management - Reset

# 1. Mandatory Parameters.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_USE_TLS = "True"

# 2. Other parameters.
EMAIL_HOST_USER = "mateusz.hyla.job@gmail.com" # Your email address.
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD") # Your gmail App Password.
DEFAULT_FROM_EMAIL = "mateusz.hyla.job@gmail.com" # Your email address.

# Deployment Settings (Must be https enabled on hosting - doesn't work on localhost where
# there is http only).

# UNCOMMENT ON PRODUCTION
# 1. Protection Against XSS Attacks.
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

# 2. CSRF Token Protection
# SESSION_COOKIE_SECURE = True 
# CSRF_COOKIES_SECURE = True

# 3. SSL Redirect
# SECURE_SSL_REDIRECT = True

# 4. Enable HSTS (Anti Man-In-The-Middle Attack - force connection over https)
# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# 5. CSP (Content Security Policy - when web app has a lot of styles and inline styles
# - prevents code injectings and XSS attacks).

